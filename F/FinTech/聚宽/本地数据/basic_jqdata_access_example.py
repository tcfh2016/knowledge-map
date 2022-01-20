import matplotlib.pyplot as plt
from jqdatasdk import *
plt.rcParams['font.family']=['SimHei']
auth('','')

# 000001.XSHG 	上证指数
# 000016.XSHG 	上证50
# 000300.XSHG 	沪深300
# 000905.XSHG 	中证500
# 399001.XSHE 	深证成指
# 399330.XSHE 	深证100
index_list = ['000001.XSHG', '000016.XSHG', '000300.XSHG', '000905.XSHG', '399001.XSHE', '399330.XSHE']
index_name_list = ['上证指数', '上证50', '沪深300', '中证500', '深证成指', '深证100']

history_price_panel = get_price(index_list, '2009-05-15', '2019-05-15', 'daily', 'close')
history_price_close = history_price_panel['close']
history_price_close.columns = index_name_list

history_price_panel['close'].plot(subplots=False, grid=True, legend=True)
plt.show()
