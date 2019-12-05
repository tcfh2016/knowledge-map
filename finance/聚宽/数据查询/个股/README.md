# 获取单只股票的历史行情

获取单只股票的基本信息可以使用`get_security_info(code)`，但在这之前必须解决该只股票对
应的`code`是什么的问题。

## 首先需要获取股票对应的证券代码

先使用`get_all_securities()`获取当前A股市场上所有的上市股票基本信息，如下：

```
参数

    types：默认为stock，这里请在使用时注意防止未来函数。
    date: 日期, 一个字符串或者 [datetime.datetime]/[datetime.date] 对象, 用于获取某日期还在上市的股票信息. 默认值为 None, 表示获取所有日期的股票信息

返回

    display_name # 中文名称
    name # 缩写简称
    start_date # 上市日期
    end_date # 退市日期，如果没有退市则为2200-01-01
    type # 类型，stock(股票)

结果

    display_name 	name 	start_date 	end_date 	type
    000001.XSHE 	平安银行 	PAYH 	1991-04-03 	2200-01-01 	stock
    000002.XSHE 	万科A 	WKA 	1991-01-29 	2200-01-01 	stock
    000004.XSHE 	国农科技 	GNKJ 	1990-12-01 	2200-01-01 	stock
    000005.XSHE 	世纪星源 	SJXY 	1990-12-10 	2200-01-01 	stock
            ... 	 ... 	... 	... 	... 	...
    688101.XSHG 	三达膜 	SDM 	2019-11-15 	2200-01-01 	stock
    688108.XSHG 	赛诺医疗 	SNYL 	2019-10-30 	2200-01-01 	stock
    688111.XSHG 	金山办公 	JSBG 	2019-11-18 	2200-01-01 	stock
    688116.XSHG 	天奈科技 	TNKJ 	2019-09-25 	2200-01-01 	stock
            ... 	 ... 	... 	... 	... 	...
```

再从中查询某只股票对应的股票代码：

```
stock_name = '洋河股份'
stocks_df = get_all_securities()
stock_code = stocks_df[stocks_df['display_name'] == stock_name].index.item()
```

## 调用 get_price()

使用`get_price()`来获取历史数据，可查询多个标的多个数据字段，返回数据格式为 DataFrame。

```
get_price(security, start_date=None, end_date=None, frequency='daily', fields=None, skip_paused=False, fq='pre', count=None, panel=True)


参数

    security: 一支股票代码或者一个股票代码的list

    count: 与 start_date 二选一，不可同时使用. 数量, 返回的结果集的行数, 即表示获取 end_date 之前几个 frequency 的数据

    start_date: 与 count 二选一，不可同时使用. 字符串或者 datetime.datetime/datetime.date 对象, 开始时间.

    end_date: 格式同上, 结束时间, 默认是'2015-12-31', 包含此日期. 注意: 当取分钟数据时, 如果 end_date 只有日期, 则日内时间等同于 00:00:00, 所以返回的数据是不包括 end_date 这一天的.

    frequency: 单位时间长度, 几天或者几分钟, 现在支持'Xd','Xm', 'daily'(等同于'1d'), 'minute'(等同于'1m'), X是一个正整数, 分别表示X天和X分钟(不论是按天还是按分钟回测都能拿到这两种单位的数据), 注意, 当X > 1时, fields只支持['open', 'close', 'high', 'low', 'volume', 'money']这几个标准字段,合成数据的逻辑见下文. 默认值是daily

    fields: 字符串list, 选择要获取的行情数据字段, 默认是None(表示['open', 'close', 'high', 'low', 'volume', 'money']这几个标准字段), 支持SecurityUnitData里面的所有基本属性,，包含：['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit','low_limit', 'avg', 'pre_close', 'paused'],其中paused为1表示停牌。

    skip_paused: 是否跳过不交易日期

    fq: 复权选项: ‘pre’, 'None', 'post'，默认为前复权

    panel：在pandas 0.25版后，panel被彻底移除。获取多标的数据时建议设置panel为False，返回等效的dataframe

```

df = get_price('510300.XSHG', start_date='2014-01-01', end_date='2015-01-31', frequency='daily', fields=['open','close'])
df
