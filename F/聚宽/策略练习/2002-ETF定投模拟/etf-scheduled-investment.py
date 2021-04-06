# 导入函数库
from jqdata import *
import numpy as np

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
    return df2


def initialize(context):
    set_benchmark('000300.XSHG')
    set_option('use_real_price', True)
    log.set_level('order', 'error')

    set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5), type='stock')
    run_monthly(before1_market_open, 1, time='before_open', reference_security='000300.XSHG')
    run_monthly(market_open, 1, time='open', reference_security='000300.XSHG')
    run_monthly(after_market_close, 1, time='after_close', reference_security='000300.XSHG')

    g.cash_income = []
    log.info('策略执行开始总资产 = ' + str(context.portfolio.total_value))


def before1_market_open(context):
    # 给微信发送消息（添加模拟交易，并绑定微信生效）
    # send_message('美好的一天~')
    # 要操作的股票：500ETF - 510500.XSHG（g.为全局变量）
    g.security = '510500.XSHG'


def try_trade(pe, positions_value):
    security = g.security
    invested_cash = 0.0
    res = None

    if (pe < 20):
        res = order_value(security, 10000)
    elif (pe < 30):
        res = order_value(security, 5000)
    elif (pe < 40):
        res = order_value(security, 1000)
    elif (pe > 50 and positions_value > 0):
        res = order_target_value(security, 0)

    if (None != res):
        invested_cash = res.amount * res.price
        if (res.action == 'open'):
            invested_cash = -invested_cash

    return invested_cash


def market_open(context):
    # 获取中证500 最近交易日的指数
    df_with_two_index_level = get_zz_quote(['000905.XSHG'], end_date=context.current_dt, count=1)
    df_905 = df_with_two_index_level.xs('000905', level='SecuCode')
    index_pe = df_905['IndexPERatio1'][0]

    log.info('策略执行日期：' + str(context.current_dt) + '中证500指数：' + str(index_pe))
    g.cash_income.append(try_trade(index_pe, context.portfolio.positions_value))

    #log.info('账户可用余额：' + str(context.portfolio.cash))


def after_market_close(context):
    trades = get_trades()
    for _trade in trades.values():
        log.info('成交记录：'+str(_trade))


def on_strategy_end(context):
    g.cash_income.append(context.portfolio.positions_value)
    month_rate = np.irr(g.cash_income)
    year_rate = (1 + month_rate)**12 - 1
    log.info('回测结束，策略按月内部收益率 = ' + str(month_rate) + '，实际年收益率 = ' + str(year_rate))
    log.info('策略执行结束总资产 = ' + str(context.portfolio.total_value))
