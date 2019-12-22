from jqdata import jy
from jqdata import *
import pandas as pd

#############################################################################
# Copy聚宽已有的共享函数
# https://www.joinquant.com/view/community/detail/16656
#############################################################################
def get_zz_quote(code,end_date=None,count=None,start_date=None):
    '''获取中证指数行情,返回panel结构'''
    if isinstance(code,str):
        code=[code]
    code.sort()

    code = [x[:6] for x in code]
    days = get_trade_days(start_date,end_date,count)
    code_df = jy.run_query(query(
         jy.SecuMain.InnerCode,jy.SecuMain.SecuCode,jy.SecuMain.ChiName
        ).filter(
        jy.SecuMain.SecuCode.in_(code)).order_by(jy.SecuMain.SecuCode))
    df = jy.run_query(query(
             jy.QT_CSIIndexQuote).filter(
            jy.QT_CSIIndexQuote.IndexCode.in_(code_df.InnerCode),
            jy.QT_CSIIndexQuote.TradingDay.in_(days),
            ))
    df2  = pd.merge(code_df, df, left_on='InnerCode',right_on='IndexCode').set_index(['TradingDay','SecuCode'])
    df2.drop(['InnerCode','IndexCode','ID','UpdateTime','JSID','OpenInterest','SettleValue','IndexCSIType'],axis=1,inplace=True)
    return df2.to_panel()


#############################################################################
# 编写代码进行指数数据获取，聚宽提供的共享函数获取指数中包括如下14列的数据：
# ChiName  OpenPrice  HighPrice  LowPrice      ClosePrice    TurnoverVolume TurnoverValue
# ChangeOF ChangePCT  TotalMV    IndexPERatio1 IndexPERatio2 IndexDYRatio1  IndexDYRatio2
#
# 其中：
#   IndexPERatio1 : 指数市盈率（I）是按总股本计算的市盈率
#   IndexPERatio2 : 指数市盈率（II）是按照中证指数调整后的股本计算的市盈率
#############################################################################

# 中证500，指数代码 = 000905.XSHG
panel = get_zz_quote(['000905.XSHG'], end_date='2019-12-22', start_date='2009-12-22')
df_905 = panel.ix[:, :, '000905']
print (df_905[['ClosePrice', 'IndexPERatio1', 'IndexPERatio2']].tail())
df_905.plot(y = ['ClosePrice', 'IndexPERatio1', 'IndexPERatio2'], secondary_y = 'ClosePrice', figsize=(20,10))
