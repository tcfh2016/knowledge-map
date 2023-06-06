from jqdata import jy
from jqdata import *
import pandas as pd

#pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 12)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

#############################################################################
# 仿照 get_prince()的原型进行设计,
# 1. 支持按天的统计的区间
# 2. 支持成交量（volumn）和成交额（money）的统计
#############################################################################
def get_trade_info(security, start_date=None, end_date=None, field=None):
    trade_days = get_trade_days(start_date, end_date)
    df_list = [get_ticks(security,start_dt=None,end_dt=day+datetime.timedelta(days=1),count=1, df=True) for day in trade_days]
    df = pd.concat(df_list).set_index('time')
    return df[field].sum()

print(get_trade_info('159915.XSHE', start_date='2020-02-17', end_date='2020-02-17', field='volume'))
print(get_trade_info('159915.XSHE', start_date='2020-02-17', end_date='2020-02-17', field='money'))

#############################################################################
# 参考：https://www.joinquant.com/help/api/help?name=fund#%E8%8E%B7%E5%8F%96%E5%9C%BA%E5%86%85%E5%9F%BA%E9%87%91tick%E6%95%B0%E6%8D%AE
#
#      get_ticks(security,end_dt,start_dt,count, fields, skip)
#
# fields: 选择要获取的行情数据字段，默认为None，返回结果如下场内基金tick返回结果。
#  -> volume 累计成交量（股） float
#  -> money 累计成交额 float
#############################################################################

# 能源ETF，基金代码 = 159930.XSHE 指数代码 = 000928.XSHG 中证能源
# 资源ETF，基金代码 = 510410.XSHG 指数代码 = 000068.XSHG 上证资源
# 中证500，基金代码 = 510500.XSHG 指数代码 = 000905.XSHG 中证500
# 创业板， 基金代码 = 159915.XSHE 指数代码 = 399006.XSHG 创业板

print("参考值:")
df = get_ticks('159915.XSHE',start_dt=None,end_dt='2020-02-18',count=1, df=True)
print(df)
print(df['volume'])
