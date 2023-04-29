from jqdata import *
import pandas as pd

# pd.set_option('display.max_columns', 500)

# 获取指数估值指标，包括指数总市值、静态市盈率、动态市盈率、市净率、股息率等指标
#   TotalMV        -- 指数总市值(元)
#   PE_TTM         -- 动态市盈率
#   PE_LYR         -- 静态市盈率(LYR)
#   PB_LF          -- 市净率(LF)
#   DividendRatio  -- 股息率(%)
#   PCF_LYR        -- 静态市现率
#   PCF_TTM        -- 动态市现率
#   PS_LYR         -- 静态市销率
#   PS_TTM         -- 动态市销率

def get_index_derivative(code,start_date=None,end_date=None,count=None):
    if isinstance(code,str):
        code=[code]
    code.sort()

    code = [x[:6] for x in code]
    days = get_trade_days(start_date,end_date,count)

    basic_info_df = jy.run_query(query(
         jy.SecuMain.InnerCode,jy.SecuMain.SecuCode,jy.SecuMain.ChiName
        ).filter(
        jy.SecuMain.SecuCode.in_(code)).order_by(jy.SecuMain.SecuCode))
    #print(basic_info_df)

    derivative_info_df = jy.run_query(query(
             jy.LC_IndexDerivative).filter(
            jy.LC_IndexDerivative.IndexCode.in_(basic_info_df.InnerCode),
            jy.LC_IndexDerivative.TradingDay.in_(days),
            ))

    df = pd.merge(basic_info_df, derivative_info_df, left_on='InnerCode',right_on='IndexCode').set_index(['TradingDay','SecuCode'])
    df.drop(['InnerCode','IndexCode','ID','InsertTime','UpdateTime','JSID'],axis=1,inplace=True)
    return df

# 399006.XSHE 	创业板指
# 399102.XSHE 	创业板综合指数
# 000001.XSHG 	上证指数
# 000905.XSHG 	中证500
# 000928.XSHG 	中证能源
# 000068.XSHG 	上证资源
code = ['000928.XSHG']
two_index_level_df = get_index_derivative(code,start_date='2010-01-01',end_date='2020-02-28')
print(two_index_level_df)
df = two_index_level_df.xs('000928', level='SecuCode')
print (df)

df.plot(y = ['PE_TTM', 'PE_LYR', 'PB_LF', 'TotalMV'], secondary_y = 'TotalMV', figsize=(20,10))

 
