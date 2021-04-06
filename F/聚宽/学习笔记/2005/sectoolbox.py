from jqdata import *
import pandas as pd
import datetime as dt
from six import BytesIO

import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText


class Utility(object):
    def calc_historic_height(arr):
        ''' 计算历史估值高度

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


    def load_local_db(file_name, field):
        '''从本地导入之前保存在./etf-db目录中的成交量数据。

        参数
        ====
        etf: etf代码

        返回值
        ======
        df : DataFrame，从本地保存的csv里面导入的成交量数据
        '''
        try:
            df = pd.read_csv(BytesIO(read_file(file_name)), index_col=field, parse_dates=True)
            print("\t找到了本地缓存文件 %s" % (file_name))
            return df
        except:
            print("\t没有找到本地缓存文件 %s" % (file_name))
            return pd.DataFrame()


    def save_to_db(file_name, new, old=pd.DataFrame()):
        '''将计算得到的成交量数据保存到./etf-db目录中的成交量数据，提高数据查询效率。

        参数
        ====
        etf : 指数代码
        new : 计算得到的最新一段时间的成交量数据
        old : 获取之前保存在本地的成交量数据
        '''
        if len(old) <= 0:
            write_file(file_name, new.to_csv(), append=False)
        else:
            df = old.append(new)
            write_file(file_name, df.to_csv(), append=False)


class EtfSelector(object):
    def __init__(self):
        self._etf_db_path = './etf-db/'


    def get_precheck_list(self):
        '''选择符合条件的ETF：于2015-01-01前发行，并且截止今日依然在交易的基金

        返回值
        ======
        DataFrame: 包含符合条件ETF的DataFrame
        '''
        etf = get_all_securities(['etf'])
        return etf[(etf['start_date'] < dt.date(2015,1,1)) & (etf['end_date'] > dt.date.today())]


    def get_volumn_perday(self, etf):
        '''计算etf成交量（股为单位）。参考：https://www.joinquant.com/help/api/help?name=fund

        参数
        ====
        etf: 指定的etf
        start: 起始日期
        end: 结束日期

        返回值
        ======
        1. 最新累计净值相对于历史最高值的百分比
        2. 最新累计净值的历史百分位
        '''
        trade_days = get_trade_days(count=100)
        file_name = self._etf_db_path + get_security_info(etf).display_name + '_volumn.csv'

        print('开始获取{}的估值数据:'.format(etf))
        df_old = Utility.load_local_db(file_name, 'time')
        if len(df_old) <= 0:
            start_date = trade_days[0]
            print('\t本地无缓存，需要计算从{}至{}的交易量。'.format(start_date, trade_days[-1]))
        else:
            start_date = df_old.index[-1] + datetime.timedelta(days=1) # 否则，将本地存储估值数据的最后一个日期做为新的起始日期
            print('\t本地有缓存从{}至{}的数据。'.format(df_old.index[0], df_old.index[-1]))

        trade_days_news = get_trade_days(start_date, trade_days[-1])
        if(len(trade_days_news) > 0):
            df_list = [get_ticks(etf,start_dt=None,end_dt=day+datetime.timedelta(days=1),count=1, df=True) for day in trade_days_news]
            df_new = pd.concat(df_list).set_index('time')

            fmt = '%Y%m%d%H%M%S.%f'
            df_new.index = [dt.datetime.strptime(str(t), fmt).date() for t in df_new.index]
            df_new.index.name = 'time'
            Utility.save_to_db(file_name, new=df_new, old=df_old)

        df = Utility.load_local_db(file_name, 'time')
        print("近100个交易日平均值 %f" % df['volume'][-100:].mean())
        return df['volume'][-100:].mean()


    def calc_historic_quantile(self, etf, start, end):
        '''计算etf累计净值的历史百分位。参考：https://www.joinquant.com/help/api/help?name=fund

        参数
        ====
        etf: 指定的etf
        start: 起始日期
        end: 结束日期

        返回值
        ======
        1. 最新累计净值相对于历史最高值的百分比
        2. 最新累计净值的历史百分位
        '''
        acc_value = get_extras('acc_net_value', etf, start_date=start, end_date=end, df=True)
        acc_value['acc_history'] = acc_value[etf].rolling(5 * 244).apply(lambda x: Utility.calc_historic_height(x), raw=True)

        return acc_value[etf][-1]/acc_value[etf].max(), acc_value['acc_history'][-1]


    def get_acc_status(self, ind1, ind2):
        '''评估etf当前的累计净值状态，是高位还是低位

        参数
        ====
        ind1: 参考指标1，代表“ETF当前累计净值近5年的百分位”
        ind2: 参考指标2，代表“ETF当前累计净值相对于自发布日以来累计净值最大值的百分比”。

        返回值
        ======
        1. 低位：两个指标均小于60%
        2. 高位：两个指标均大于80%
        '''
        if (ind1 < 0.60 and ind2 < 0.60):
            return "low"

        if (ind1 > 0.80 and ind2 > 0.80):
            return "high"


    def select_etf(self):
        etf = self.get_precheck_list()

        valuation_di = dict()
        for i in range(len(etf.index)):
            volumn_day = self.get_volumn_perday(etf.index[i])
            if (volumn_day < 5000000):
                print("skip %s" % etf.index[i])
                continue
            m, q = self.calc_historic_quantile(etf.index[i], start=etf.start_date[i], end=dt.date.today()-dt.timedelta(days=1))
            valuation_di[etf.index[i]] = {'percent_of_max':m, 'quantile':q, 'day_volumn':volumn_day/1000000}

        valuation_df = pd.DataFrame(valuation_di).T.dropna()
        return valuation_df.sort_values(['quantile', 'percent_of_max'])


class IndexValuator(object):
    def __init__(self):
        self._index_db_path = './index-db/'


    def valuate(self, index_code, start_date, end_date=datetime.datetime.now().date() - datetime.timedelta(days=1)):
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
            return pd.DataFrame()

        def iter_pe_pb(): # 这是一个生成器函数
            trade_date = get_trade_days(start_date=start_date, end_date=end_date)

            for date in trade_date:
                stocks = get_index_stocks(index_code, date)
                q = query(valuation.pe_ratio,
                          valuation.pb_ratio,
                          valuation.market_cap,
                          (valuation.market_cap/valuation.pe_ratio).label('value'),
                         ).filter(
                                  valuation.pe_ratio != None,
                                  valuation.pb_ratio != None,
                                  valuation.code.in_(stocks))
                df = get_fundamentals(q, date)
                if (len(df.index) == 0):
                    continue
                market_value = df.market_cap.sum()/df.value.sum()

                yield date, df.pe_ratio.median(), df.pb_ratio.median(), market_value, df.market_cap.sum()

        dict_result = [{'date': value[0], 'pe_median': value[1], 'pb_median':value[2], 'pe': value[3], 'TotalMV':value[4]} for value in iter_pe_pb()]
        print('\t计算完成。')
        if (len(dict_result) == 0):
            return pd.DataFrame()
        else:
            df = pd.DataFrame(dict_result)
            df.set_index('date', inplace=True)
            return df


    def get_valuation(self, index_code, start_date):
        '''获取从某个日期开始的估值pe/pb。

        参数
        ====
        index_code: 指数代码
        start_date: 起始日期
        '''
        print('开始获取{}的估值数据:'.format(index_code))
        file_name = self._index_db_path + get_security_info(index_code).display_name + '_pe_pb.csv'

        df_old = Utility.load_local_db(file_name, 'date')
        if len(df_old) <= 0:
            start_date = start_date # 本地没有保存估值数据，从指定的日期开始获取
            print('\t本地无缓存，需要计算从{}开始的估值数据。'.format(start_date))
        else:
            start_date = df_old.index[-1] + datetime.timedelta(days=1) # 否则从本地存储估值数据的最后一个日期后开始计算
            print('\t本地有缓存从{}至{}的数据，需要计算从{}开始的数据。'.format(df_old.index[0], df_old.index[-1], start_date))
        df_new = self.valuate(index_code, start_date=start_date)
        Utility.save_to_db(file_name, new=df_new, old=df_old)
        return Utility.load_local_db(file_name, 'date')


    def collect_valuations(self, indexes=None):
        '''获取多只指数的pe数据。

        参数
        ====
        indexes: 指数代码，支持多支指数

        返回值
        ======
        dict: dict，由{指数代码：指数多天pe/pb的DataFrame}组成的字典。
        '''

        def is_only_stock(index):
            securities = get_index_stocks(index)
            if (len(securities) > 0):
                info = get_security_info(securities[0])
                return (info.type == 'stock')
            return False

        if indexes == None:
            indexes = ['000016.XSHG', '000300.XSHG', '399905.XSHE'] # 默认获取上证50，沪深300，中证500三支指数
        index_pe = {index : self.get_valuation(index, get_security_info(index).start_date) for index in indexes if is_only_stock(index) == True}
        print("获取数据完成。")

        return index_pe


    def draw_quantile_diagram(self, index, indicator, years, valuation):
        '''绘制基于pe的百分位估值图

        参数
        ====
        index     : 指数代码，支持单支指数
        indicator : 百分位参考指标，包括'pe_median', 'pb_median', 'pe', 'TotalMV'
        years     : 最近多少年度的数据
        valuation : 估值数据

        返回值
        ======
        dict: dict，由{指数代码：指数多天pe/pb的DataFrame}组成的字典。
        '''
        # 先拷贝一份数据，避免影响原始数据，因为该数据会写入文件中保存起来
        df = valuation.copy()
        df.index.name = None

        # 一、计算估值百分位：选取指数自成立以来的估值数据，再分别计算出30%，50%，70%的估值百分位
        i_df = df

        # 二、计算前years年的历史百分位高度，用于在图形中展示基于百分位的历史估值趋势
        i_df['pe_history'] = df[indicator].rolling(years * 244).apply(lambda x: Utility.calc_historic_height(x), raw=True)
        i_df['mv_history'] = df['TotalMV'].rolling(years * 244).apply(lambda x: Utility.calc_historic_height(x), raw=True)

        # 三、计算当前（最近一个交易日）的近years年的百分位高度，用于估值
        quantile_pe = Utility.calc_historic_height(i_df['pe'])
        quantile_mv = Utility.calc_historic_height(i_df['TotalMV'])
        assessment_pe = Utility.get_valuation_status(quantile_pe)

        title = '{}，{}, 近{}年pe历史百分位{}/{} {}，近{}年market value历史百分位{}/{}'.format(
            get_security_info(index).display_name, valuation.index[-1],
            years, str(round(i_df['pe_history'][-1]*100, 2))+'%', str(round(quantile_pe * 100, 2)) + '%', assessment_pe,
            years, str(round(i_df['mv_history'][-1]*100, 2))+'%', str(round(quantile_mv * 100, 2)) + '%')

        i_df.plot(y=['pe','pe_history', 'mv_history'], secondary_y=['pe'], figsize=(20, 10), style=['-', '-', '-', '-', 'y-'])
        picture_name = get_security_info(index).display_name + '.png'
        plt.savefig(picture_name)

        return title

    def get_indexes_pe_quantile(self, indexes):
        '''绘制基于pe的百分位估值图

        参数
        ====
        index     : 指数代码，支持单支指数
        indicator : 百分位参考指标，包括'pe_median', 'pb_median', 'pe', 'TotalMV'
        years     : 最近多少年度的数据
        valuation : 估值数据

        返回值
        ======
        dict: dict，由{指数代码：指数多天pe/pb的DataFrame}组成的字典。
        '''
        dic = self.collect_valuations(indexes)
        for index, data in dic.items():
            self.draw_quantile_diagram(index, 'pe', 5, data)


    def get_latest_quantile(self, index, indicator, years, valuation):
        '''获取指数最近一个交易日的估值百分位

        参数
        ====
        index     : 指数代码，支持单支指数
        indicator : 百分位参考指标
        years     : 最近多少年度的数据
        valuation : 估值数据

        返回值
        ======
        i_df[p].iloc[-1], quantile[-1]: 指数当天的pe、估值百分位。
        '''
        i_df = pd.DataFrame()
        i_df[indicator] = valuation[indicator]
        i_df = i_df.iloc[-years * 244:] # 244代表每年的交易日
        quantile = i_df[indicator].rank() / i_df.shape[0]
        return i_df[indicator].iloc[-1], quantile[-1]


    def get_valuation_table(self):
        all_index = list(get_all_securities(['index']).index.values)
        valuation_dict = self.collect_valuations(all_index)

        quantile_dict = dict()
        for ind, val in valuation_dict.items():
            # 过滤空的DataFrame
            if (len(val.index) != 0):
                pe, pe_quantile = self.get_latest_quantile(ind, 'pe', 5, val)
                pb, pb_quantile = self.get_latest_quantile(ind, 'pb_median', 5, val)
                quantile_dict[ind] = {'pe': pe, 'pe_quantile': pe_quantile, 'pb': pb, 'pb_quantile': pb_quantile}
        df = pd.DataFrame(quantile_dict).T
        return df.sort_values(['pe_quantile', 'pb_quantile'])


class HtmlReporter(object):
    def __init__(self):
        self._ETF_selector = EtfSelector()
        self._index_valuator = IndexValuator()

        self._head = '''
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title></title>
            <style media="screen">
              body {
                background-color: LightYellow;
                width: 900px;
              }
              header {
                text-align: center;
              }
              div {
                text-align: center;
              }
              section {
                height: 50px;
                text-align: center;
              }
              article {
                font-size: 12px;
                text-align: center;
                color: blue;
                width: 900px;
                margin-left: auto;
                margin-right: auto;
              }
              figure {
                background-color: Cornsilk;
                width: 900px;
                margin-left: auto;
                margin-right: auto;
              }
              footer {
                text-align: center;
                padding: 3px;
                background-color: white;
                color: blue;
              }
              table {
                width: 900px;
                text-align:right;
                border-collapse: collapse;
                margin-left: auto;
                margin-right: auto;
              }
              th {
                background-color: Brown;
                color: white;
              }
              .img {
                width: 900px;
              }
              .low {
                background-color: lightgreen;
              }
              .high {
                background-color: tomato;
              }
              .超高估{
                background: rgb(128,128,128);
              }
                .高估{
                background: rgb(220,20,60);
              }
                .适中偏高{
                background: rgb(255,165,0);
              }
                .适中{
                background: rgb(255,215,0);
              }
                .适中偏低{
                background: rgb(240,230,140)
              }
                .低估{
                background: rgb(144,238,144);
              }
                .超低估{
                background: rgb(60,179,113);
              }
              .valuation_table {
                text-align:right;
              }
            </style>
          </head>
          <body>
        '''
        self._tail = '''
            <footer>
              <p> 以上信息仅供参考。 </p>
            </footer>
          </body>
        </html>
        '''


    def construct_ETF_list(self):
        etf = self._ETF_selector.select_etf()

        etf_table = """
        <header>
            <h3>ETF海选列表</h3>
        </header>
        <div>
            <table>
              <tr>
                <th>基金代码</th>
                <th>基金名称</th>
                <th>成交量</th>
                <th>评估系数①</th>
                <th>评估系数②</th>
              </tr>
        """

        for i in range(etf.shape[0]):
            indicator1 = etf.percent_of_max[i]
            indicator2 = etf['quantile'][i]
            acc_status = self._ETF_selector.get_acc_status(indicator1, indicator2)

            etf_table += """
            <tr  class="{}">
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
            """.format(acc_status,
                       etf.index[i],
                       get_security_info(etf.index[i]).display_name,
                       str(round(etf.day_volumn[i], 2)),
                       str(round(indicator1 * 100, 2)) + '%',
                       str(round(indicator2 * 100, 2)) + '%')

        etf_table += """
        </table>
        <article>
          <p>注1：表格中的“评估系数①”代表“ETF当前累计净值近5年的百分位”，而“评估系数②”代表“ETF当前累计净值相对于自发布日以来累计净值最大值的百分比”。</p>
          <p>注2：表格中以两个评估系数均小于60%作为“低位”的判断标准，将两个评估系数均大于80%作为处在“高位”的判断标准。此处的“低位”和“高位”的判别仅仅是按照经验来定义的，对于该基金是否高估还是低估可以进一步从基金对应的指数来进行判断。</p>
          <p>注3：如下展示的是当前正在定投的基金对应指数的估值状态。</p>
        </article>
        </div>
        <section> </section>
        """

        return etf_table


    def construct_valuation_diagrame(self, indexes):
        dic = self._index_valuator.collect_valuations(indexes)

        diagrame_div = "<div>"
        for index, data in dic.items():
            title = self._index_valuator.draw_quantile_diagram(index, 'pe', 5, data)
            diagrame_div += """
            <figure>
                <figcaption>{}</figcaption>
                <img src="cid:{}" alt="" class="img">
            </figure>
            """.format(title, get_security_info(index).name)
        diagrame_div += '</div><section> </section>'

        return diagrame_div

    def construct_valuation_table(self):
        valuations = self._index_valuator.get_valuation_table()

        val_table = """
        <header>
          <h3>全网指数估值</h3>
        </header>
        <div>
            <table>
              <tr>
                  <th>指数代码</th>
                  <th>指数名称</th>
                  <th>pe百分位</th>
                  <th>pb百分位</th>
              </tr>
        """

        for i in range(valuations.shape[0]):
            val_status = Utility.get_valuation_status(valuations.pe_quantile[i])

            val_table += """
            <tr  class="{}">
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
            """.format(val_status,
                       valuations.index[i],
                       get_security_info(valuations.index[i]).display_name,
                       str(round(valuations.pe_quantile[i] * 100, 2)) + '%',
                       str(round(valuations.pb_quantile[i] * 100, 2)) + '%')

        val_table += """
        </table>
        </div>
        <section> </section>
        """

        return val_table


    def send_email(self):
        msg = EmailMessage()
        sender = 'lianbch@163.com'
        receiver = 'lianbch@163.com'

        # 填充邮件头部
        msg['Subject'] = '基金筛选结果'
        msg['From'] = sender
        msg['To'] = receiver

        # 填充邮件正文
        indexes = ['000905.XSHG', '000928.XSHG']
        html = self._head \
               + self.construct_ETF_list() \
               + self.construct_valuation_diagrame(indexes) \
               + self.construct_valuation_table() \
               + self._tail
        msg.add_attachment(html, subtype='html')

        for index in indexes:
            picture_name = get_security_info(index).display_name + '.png'
            with open(picture_name, 'rb') as f:
                msg.add_attachment(f.read(), maintype='image', subtype='png', cid=get_security_info(index).name)

        # 发送邮件
        try:
            mail_server = smtplib.SMTP_SSL('smtp.163.com',port=465)
            mail_server.login(sender, 'FVVFEMTFLXCRLQXS')
            mail_server.send_message(msg)
        except smtplib.SMTPException as ex:
            print("Error: send failure = ", ex)
