from jqdata import *


def initialize(context):
    set_benchmark('000300.XSHG')
    set_option('use_real_price', True)

    set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5), type='stock')
    run_monthly(before_market_open, monthday=1, time='before_open', reference_security='000300.XSHG')
    run_monthly(market_open, monthday=1, time='open', reference_security='000300.XSHG')

    g.underestimate_model = {'510050.XSHG' : 1.0} # 50ETF
    g.overestimate_model  = {'000012.XSHG' : 0.8, '510050.XSHG' : 0.2} # 国债ETF + 50ETF
    g.model = {}

def before_market_open(context):
    log.info('函数运行时间(before_market_open)：'+str(context.current_dt))

    # 计算前一个交易日沪深300指数对应的估值（市盈率）
    stocks = get_index_stocks('000300.XSHG')
    df = get_fundamentals(query(
        valuation.code,
        valuation.market_cap,
        valuation.pe_ratio,
        (valuation.market_cap/valuation.pe_ratio).label('value'),
    ).filter(
        valuation.code.in_(list(stocks)),
    )).dropna()

    g.market_value = df.market_cap.sum()/df.value.sum()
    if g.market_value > 30:
        g.model = g.overestimate_model
    elif g.market_value < 15:
        g.model = g.underestimate_model

    log.info('沪深300指数市盈率 = '+str(g.market_value))


def market_open(context):
    log.info('函数运行时间(market_open):'+str(context.current_dt))

    sell_list = set(context.portfolio.positions.keys()) - set(g.model.keys())
    for stock in sell_list:
        order_target_value(stock, 0)

    # 跟最着账户的总市值执行再平衡策略。
    for stock in g.model.keys():
        # 计算“最新模型建议的持有市值”
        position = g.model[stock] * context.portfolio.total_value
        # 如果“当前持有该证券的市值” = 0，直接执行买入
        if not context.portfolio.positions.has_key(stock):
            order_target_value(stock, position)
        # 如果“当前持有该证券的市值”与“模型里面建议持有的市值”不匹配，那么执行再平衡。
        elif abs(context.portfolio.positions[stock].value - position) > 0.2*context.portfolio.total_value:
            order_target_value(stock, position)
