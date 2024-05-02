def initialize(context):
    log.set_level('order', 'error')
    set_option('use_real_price', True)

def after_code_changed(context):
    g.index = '000300.XSHG'
    g.market_bubble = False # 市场状态
    g.bubble_weight = {
        # 防御组合
        '000012.XSHG' : 0.8, #国债指数，仅限于测试
        # 模拟盘及实盘请选择真实债券基金，比如国债ETF
        '510050.XSHG' : 0.2, #上证50
        # 模拟盘及实盘优选更强的大盘指数基金，比如300ETF
        }
    g.value_weight = {
        '510050.XSHG' : 1.0, #上证50
        # 模拟盘及实盘优选更强的大盘指数基金，比如300ETF
        }

def before_trading_start(context):
    # stock pool
    stocks = get_index_stocks(g.index)
    df = get_fundamentals(query(
            valuation.code,
            valuation.market_cap,
            (valuation.market_cap/valuation.pe_ratio).label('earn')
        ).filter(
            valuation.code.in_(stocks),
        )).dropna()
    index_pe = df.market_cap.sum()/df.earn.sum()
    # update market status
    if g.market_bubble and index_pe < 15:
        g.market_bubble = False
    elif not g.market_bubble and index_pe > 30:
        g.market_bubble = True
    record(mpv=index_pe, z=30*g.market_bubble)

def position_management(context, weight):
    # clear non-choice
    for stock in context.portfolio.positions.keys():
        if not weight.has_key(stock):
            log.info('sell out ', stock)
            order_target(stock, 0);
    # buy and rebalance
    for stock in weight.keys():
        position = weight[stock] * context.portfolio.total_value
        if not context.portfolio.positions.has_key(stock):
            log.info('buy ', stock)
            order_target_value(stock, position) # buy
        elif abs(position - context.portfolio.positions[stock].value) > 0.1*position:
            log.info('rebalance ', stock)
            order_target_value(stock, position) # rebalance

def handle_data(context, data):
    if g.market_bubble:
        position_management(context, g.bubble_weight)
    else:
        position_management(context, g.value_weight)
# end
