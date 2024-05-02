import pandas as pd
import sys
from six import BytesIO
from jqdata import *


#database_path = './db/'
database_path = './db2/'


def H_V_H(arr):
    ''' historic_valuation_height: 计算历史估值高度

    参数
    ====
    arr : ndarry类型，此时是一维的估值数据

    返回值
    ======
    返回“小于最后一天估值数据的天数”占“总的天数”的百分比
    '''
    low = arr[arr < arr[-1]]
    return(low.shape[0] / arr.shape[0])


def get_valuation_status(quantile):
    ''' 获取估值状态

    参数
    ====
    quantile : 估值所处的百分位

    返回值
    ======
    assessment : 估值状态
    '''
    assessment = ''
    if 0 <= quantile < 0.1:
        assessment = '超低估'
    elif 0.1 < quantile < 0.3:
        assessment = '低估'
    elif 0.3 < quantile < 0.4:
        assessment = '适中偏低'
    elif 0.4 < quantile < 0.6:
        assessment = '适中'
    elif 0.6 < quantile < 0.7:
        assessment = '适中偏高'
    elif 0.7 < quantile < 0.9:
        assessment = '高估'
    elif 0.9 < quantile <= 1:
        assessment = '超高估'

    return assessment


def calc_index_valuation(index_code, start_date, end_date=datetime.datetime.now().date() - datetime.timedelta(days=1)):
    '''计算指数的估值数据。

    参数
    ====
    index_code: 指数代码
    start_date：起始日期
    end_date  : 结束日期（默认为今天）

    返回值
    ======
    df: DataFrame，包含了指定日期区间每天的pe, pb数据
    '''
    if (isinstance(start_date, pd.Timestamp)):
        start_date = start_date.date()
    if (start_date <= end_date):
        print('\t计算{}自{}到{}的估值数据...'.format(index_code, start_date, end_date))
    else:
        print('\t没有新的数据需要获取。')

    def iter_pe_pb(): # 这是一个生成器函数
        trade_date = get_trade_days(start_date=start_date, end_date=end_date)

        for date in trade_date:
            stocks = get_index_stocks(index_code, date)
            q = query(valuation.market_cap,
                      (valuation.market_cap/valuation.pe_ratio).label('value'),
                     ).filter(
                              valuation.pe_ratio != None,
                              valuation.pb_ratio != None,
                              valuation.code.in_(stocks))
            df = get_fundamentals(q, date)
            if (len(df.index) == 0):
                continue
            market_value = df.market_cap.sum()/df.value.sum()

            yield date, market_value, df.market_cap.sum()

    dict_result = [{'date': value[0], 'pe': value[1], 'TotalMV':value[2]} for value in iter_pe_pb()]
    print('\t计算完成。')
    if (len(dict_result) == 0):
        return pd.DataFrame()
    else:
        df = pd.DataFrame(dict_result)
        df.set_index('date', inplace=True)
        return df


def load_local_db(index_code):
    '''从本地导入之前保存在./database目录中的估值数据。

    参数
    ====
    index_code: 指数代码

    返回值
    ======
    df : DataFrame，从本地保存的csv里面导入的估值数据
    '''
    file_name = database_path + get_security_info(index_code).display_name + '_pe_pb.csv'
    try:
        df_loc_pe_pb = pd.read_csv(BytesIO(read_file(file_name)), index_col='date', parse_dates=True)
        print("\t找到了本地缓存文件 %s" % (file_name))
        return df_loc_pe_pb
    except:
        print("\t没有找到本地缓存文件 %s" % (file_name))
        return pd.DataFrame()


def save_to_db(index_code, new, old=pd.DataFrame()):
    '''将计算得到的估值数据保存到./database目录中的估值数据，提高数据查询效率。

    参数
    ====
    index_code: 指数代码
    new       : 计算得到的最新一段时间的估值数据
    old       : 获取之前保存在本地的估值数据
    '''
    file_name = database_path + get_security_info(index_code).display_name + '_pe_pb.csv'
    if len(old) <= 0:
        write_file(file_name, new.to_csv(), append=False)
    else:
        df = old.append(new)
        write_file(file_name, df.to_csv(), append=False)


def get_pe_pb(index_code, start_date):
    '''获取从某个日期开始的估值pe/pb。

    参数
    ====
    index_code: 指数代码
    start_date: 起始日期
    '''
    print('开始获取{}的估值数据:'.format(index_code))
    df_old = load_local_db(index_code)
    if len(df_old) <= 0:
        start_date = start_date # 本地没有保存估值数据，从指定的日期开始获取
        print('\t本地无缓存，需要计算从{}开始的估值数据。'.format(start_date))
    else:
        start_date = df_old.index[-1] + datetime.timedelta(days=1) # 否则，将本地存储估值数据的最后一个日期做为新的起始日期
        print('\t本地有缓存从{}至{}的数据。'.format(df_old.index[0], df_old.index[-1]))
    df_new = calc_index_valuation(index_code, start_date=start_date)
    save_to_db(index_code, new=df_new, old=df_old)
    return load_local_db(index_code)
