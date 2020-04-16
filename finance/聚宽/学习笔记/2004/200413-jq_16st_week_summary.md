# 聚宽学习周记十六：详解@东南有大树的“指数估值自动报表系统”（上）

很巧，按照盈科后进、学以致用的基本学习原则，本周选择了@东南有大树的[指数估值自动报表系统——源代码](https://www.joinquant.com/view/community/detail/20497)来学习。


## 一、研究部分代码解释

```
def get_pe_pb(index_code, start_date, end_date=datetime.datetime.now().date()):
    '''获取PE/PB'''
    def iter_pe_pb():
        '''一个获取PE/PB的生成器'''
        trade_date = get_trade_days(start_date=start_date, end_date=end_date)   

        for date in trade_date:
            stocks = get_index_stocks(index_code, date)
            q = query(valuation.pe_ratio,
                      valuation.pb_ratio
                     ).filter(valuation.pe_ratio != None,
                              valuation.pb_ratio != None,
                              valuation.code.in_(stocks))
            df = get_fundamentals(q, date)
            quantile = df.quantile([0.25, 0.75])
            df_pe = df.pe_ratio[(df.pe_ratio > quantile.pe_ratio.values[0]) &\
                                (df.pe_ratio < quantile.pe_ratio.values[1])]
            df_pb = df.pb_ratio[(df.pb_ratio > quantile.pb_ratio.values[0]) &\
                                (df.pb_ratio < quantile.pb_ratio.values[1])]
            yield date, df_pe.median(), df_pb.median()

    dict_result = [{'date': value[0], 'pe': value[1], 'pb':value[2]} for value in iter_pe_pb()]
    df_result = pd.DataFrame(dict_result)
    df_result.set_index('date', inplace=True)
    return df_result


def loc_pe_pb(index_code):
    '''获取保存在本地的PE/PB数据'''
    file_name = get_security_info(index_code).display_name +'_pe_pb.csv'
    if os.path.exists(file_name):
        df_loc_pe_pb = pd.read_csv(file_name, index_col='date', parse_dates=True)

        return df_loc_pe_pb
    else:
        return pd.DataFrame()


def save_pe_pb(index_code, df_new, df_old=pd.DataFrame()):
    '''将数据保存或更新到本地，避免重复生成计算'''
    file_name = get_security_info(index_code).display_name +'_pe_pb.csv'
    if len(df_old) <= 0:
        df_new.to_csv(file_name)

    else:
        df = df_old.append(df_new)
        df.to_csv(file_name)


def GetPePb(index_code, start_date):
    df_old = loc_pe_pb(index_code)  # 判断本地是否有历史数据
    if len(df_old) <= 0:
        start_date = start_date  # 给定一个默认的起始时间
    else:

        start_date = df_old.index[-1]
    df_new = get_pe_pb(index_code,start_date=start_date)
    save_pe_pb(index_code, df_new=df_new, df_old=df_old)
    return loc_pe_pb(index_code)


def show_quantile(index_code, p, n, data):
    '''
    展示估值图
    '''
    _df = pd.DataFrame()
    df = data.copy()
    df.index.name = None

    # 一、计算当前百分位高度
    _df[p] = df[p]
    _df = _df.iloc[-n * 244:]
    p_high = [_df[p].quantile(i / 10.0) for i in [3, 5, 7]]
    for p_h, i in zip(p_high, [3, 5, 7]):
        _df[str(i / 10 * 100)+'%'] = p_h

    # 二、计算历史百分位高度
    def _func(c):
        low_p = c[c < c[-1]]
        value = low_p.shape[0] / c.shape[0]
        return value
    _df['history'] = df[p].rolling(n * 244).apply(lambda x: _func(x), raw=True)[-n*244:]

    # 三、计算评估语句
    low_p = _df[_df[p] < _df[p].iloc[-1]]
    quantile_now = low_p.shape[0] / _df.shape[0]  # 当前百分位值
    last_p = _df[p][-1]
    assessment = ''
    if 0 <= quantile_now < 0.1:
        assessment = '超低估'
    elif 0.1 < quantile_now < 0.3:
        assessment = '低估'
    elif 0.3 < quantile_now < 0.4:
        assessment = '适中偏低'
    elif 0.4 < quantile_now < 0.6:
        assessment = '适中'
    elif 0.6 < quantile_now < 0.7:
        assessment = '适中偏高'   
    elif 0.7 < quantile_now < 0.9:
        assessment = '高估'   
    elif 0.9 < quantile_now <= 1:
        assessment = '超高估'   

    title = '{}，当前{}{}，近{}年历史百分位{}，{}'.format(get_security_info(index_code).display_name,
                                              p, round(last_p, 2), n,
                                              str(round(quantile_now * 100, 2)) + '%', assessment)

    _df.plot(secondary_y=['history'], figsize=(18, 10), style=['-', '--', '--', '--', 'y-'], title=title)


def show_quantile2(index_code, p, data):
    '''
    展示估值图
    '''
    fig, _ax = plt.subplots(figsize=(18, 4), ncols=3, nrows=1)

    for n, ax in zip([3, 5, 7], _ax):
        _df = pd.DataFrame()
        df = data.copy()
        df.index.name = None

        # 一、计算当前百分位高度
        _df[p] = df[p]
        _df = _df.iloc[-n * 244:]
        p_high = [_df[p].quantile(i / 10.0) for i in [3, 5, 7]]
        for p_h, i in zip(p_high, [3, 5, 7]):
            _df[str(i / 10 * 100)+'%'] = p_h

        # 二、计算历史百分位高度
        def _func(c):
            low_p = c[c < c[-1]]
            value = low_p.shape[0] / c.shape[0]
            return value
        _df['history'] = df[p].rolling(n * 244).apply(lambda x: _func(x), raw=True)[-n*244:]

        # 三、计算评估语句
        low_p = _df[_df[p] < _df[p].iloc[-1]]
        quantile_now = low_p.shape[0] / _df.shape[0]  # 当前百分位值
        last_p = _df[p][-1]
        assessment = ''
        if 0 <= quantile_now < 0.1:
            assessment = '超低估'
        elif 0.1 < quantile_now < 0.3:
            assessment = '低估'
        elif 0.3 < quantile_now < 0.4:
            assessment = '适中偏低'
        elif 0.4 < quantile_now < 0.6:
            assessment = '适中'
        elif 0.6 < quantile_now < 0.7:
            assessment = '适中偏高'   
        elif 0.7 < quantile_now < 0.9:
            assessment = '高估'   
        elif 0.9 < quantile_now <= 1:
            assessment = '超高估'   

        title = '{}，当前{}{}，近{}年历史百分位{}，{}'.format(get_security_info(index_code).display_name,
                                                  p, round(last_p, 2), n,
                                                  str(round(quantile_now * 100, 2)) + '%', assessment)

        _df.plot(secondary_y=['history'],  
                 style=['-', '--', '--', '--', 'y-'],
                 title=title,
                 ax=ax,
                 legend=False)
    _ax[0].legend(loc='best')


def init(index_base=None):
    '''
    初始化数据缓存
    '''
    if index_base == None:

        index_base = ['000016.XSHG', '000300.XSHG', '399905.XSHE']  # 上证50，沪深300，中证500
    dict_index_base = dict()

    '''加载pe/pb'''
    for index in index_base:
        index_info = get_security_info(index) # 获取指数相关信息
        start_date = index_info.start_date  # 上市日期
        dict_index_base[index] = (GetPePb(index, start_date))  # 加载或重新计算pe/pb
    return dict_index_base


dic = init(['000001.XSHG'])
for index, data in dic.items():
    show_quantile(index, 'pe', 5, data)
```

### 函数`get_pe_pb`

这个函数用来获取指数在指定日期区间的pe/pb数据。

```
def get_pe_pb(index_code, start_date, end_date=datetime.datetime.now().date()):
    '''获取PE/PB'''
    def iter_pe_pb():
        '''一个获取PE/PB的生成器'''
        trade_date = get_trade_days(start_date=start_date, end_date=end_date)   

        for date in trade_date:
            stocks = get_index_stocks(index_code, date)
            q = query(valuation.pe_ratio,
                      valuation.pb_ratio
                     ).filter(valuation.pe_ratio != None,
                              valuation.pb_ratio != None,
                              valuation.code.in_(stocks))
            df = get_fundamentals(q, date)
            quantile = df.quantile([0.25, 0.75])
            df_pe = df.pe_ratio[(df.pe_ratio > quantile.pe_ratio.values[0]) &\
                                (df.pe_ratio < quantile.pe_ratio.values[1])]
            df_pb = df.pb_ratio[(df.pb_ratio > quantile.pb_ratio.values[0]) &\
                                (df.pb_ratio < quantile.pb_ratio.values[1])]
            yield date, df_pe.median(), df_pb.median()

    dict_result = [{'date': value[0], 'pe': value[1], 'pb':value[2]} for value in iter_pe_pb()]
    df_result = pd.DataFrame(dict_result)
    df_result.set_index('date', inplace=True)
    return df_result
```

这段代码的功能是获取指定指数在特定日期范围的市盈率（PE）和市净率（PB）数据，这段代码里面使用到了两个对我来说是新的知识点，先将它们解释如下：

1. pandas中的`quantile()`

这个函数是用来求取分位数的，分位数是依照概率将样本数据分隔开的那个点，它的输入的一个百分比的概率，输出是和样本数据相同量级的值。举个例子，有10位同学某学期期末取得的英语成绩分别为{60, 70, 87, 56, 35, 64, 28, 84, 89, 65}，我们想找到一个数值A，使得有20%的同学得分小于A，其余80%的同学得分大于A，那么A便是针对20%的分位数。

参考：

- [Python解释数学系列——分位数Quantile](https://www.cnblogs.com/brightyuxl/p/9815780.html)
- [如何通俗地理解分位数？](https://www.zhihu.com/question/67763556/answer/394626078)

2. 生成器和`yield`

看到这段代码的时候吓了一跳，怎么搞的还能在函数里面定义函数？这是第一次见。

`yield`的作用就是把一个函数变成一个generator，带有`yield`的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，在调用这个函数时会返回一个iterable对象，再次调用时会继续往下遍历。简单来说调用生成器函数实际的结果是会返回一个列表。

那么在这段代码里面生成器函数`iter_pe_pb()`的结果是一个保存了对应指数在一段日期内每天的日期、市盈率均值和市净率均值。

参考：

- [Python yield 使用浅析](https://www.runoob.com/w3cnote/python-yield-used-analysis.html)

函数`get_pe_pb()`详细解释如下：

- 首先，定义一个生成器函数`iter_pe_pb()`用来获得一段日期内指数每天的市盈率均值和市净率均值，这里面包括：
  - 调用`get_trade_days()`获取指定日期的所有交易日。
  - 循环遍历所有交易日，对于每个交易日，分别有如下操作：
    - 获取指数对应的所有成分股。
    - 获取所有成分股的市盈率和市净率数据。
    - 按照25%，75%过滤市盈率和市净率数据。
    - 返回（日期，市盈率均值，市净率均值）组成的元组。
- 其次，将由如上生成器获得的所有元组组合成列表，列表中的元素是集合，集合中的元素又是字典。
- 最后，用这个列表生成DataFrame类型的二维数据。


### 函数`loc_pe_pb()`和`save_pe_pb`

```
def loc_pe_pb(index_code):
    '''获取保存在本地的PE/PB数据'''
    file_name = get_security_info(index_code).display_name +'_pe_pb.csv'
    if os.path.exists(file_name):
        df_loc_pe_pb = pd.read_csv(file_name, index_col='date', parse_dates=True)

        return df_loc_pe_pb
    else:
        return pd.DataFrame()


def save_pe_pb(index_code, df_new, df_old=pd.DataFrame()):
    '''将数据保存或更新到本地，避免重复生成计算'''
    file_name = get_security_info(index_code).display_name +'_pe_pb.csv'
    if len(df_old) <= 0:
        df_new.to_csv(file_name)

    else:
        df = df_old.append(df_new)
        df.to_csv(file_name)
```

如上这两个函数用来从本地获取数据和存储数据到本地：

- `loc_pe_pb()`：获取本地的数据
  - 先用`指数中文名称` + `_pe_pb.csv`来拼接出要搜寻的文件名称。
  - 调用`os.path`搜索本地文件。
  - 如果搜索到了，使用`read_csv()`读取文件中的内容，并返回。
  - 如果没有找到，那么返回一个空的DataFrame。
- `save_pe_pb()`：存储数据到本地
  - 同样的，先拼接出要存储的文件名称。
  - 判断这个文件当中是否已有数据，如果没有那么直接使用`to_csv()`写入该文件。
  - 如果已有数据，那么则调用`append()`将已有文件内容和新的数据合并到一起，再调用`to_csv()`写入所有内容到老的文件中。


### 函数`GetPePb()`

```
def GetPePb(index_code, start_date):
    df_old = loc_pe_pb(index_code)  # 判断本地是否有历史数据
    if len(df_old) <= 0:
        start_date = start_date  # 给定一个默认的起始时间
    else:

        start_date = df_old.index[-1]
    df_new = get_pe_pb(index_code,start_date=start_date)
    save_pe_pb(index_code, df_new=df_new, df_old=df_old)
    return loc_pe_pb(index_code)
```

这个函数是对前面的`get_pe_pb()`，`loc_pe_pb()`，`save_pe_pb()`的综合应用，它完成的功能是完成对指定指数的pe/pb的查询，有如下过程：

- 先装在本地用来存储指数pe/pb的数据文件，并将其中保存数据的最后一个日期做为新的查询日期
- 调用`get_pe_pb()`查询最新的一段数据
- 将查询的新数据保存到本地，然后再装载本地的所有数据

### 函数`init()`

需要注意的是init()函数在研究模块里面有两个，我对比了一下，两者的差别只在最后一句`return`语句，根据上下文推断后面一个是正确的，返回保存的估值pe/pb数据，所以我在引用的时候保留了最后的那个init()函数，删除了前面的那个。

```
def init(index_base=None):
    '''
    初始化数据缓存
    '''
    if index_base == None:
        index_base = ['000016.XSHG', '000300.XSHG', '399905.XSHE']  # 上证50，沪深300，中证500
    dict_index_base = dict()

    '''加载pe/pb'''
    for index in index_base:
        index_info = get_security_info(index) # 获取指数相关信息
        start_date = index_info.start_date  # 上市日期
        dict_index_base[index] = (GetPePb(index, start_date))  # 加载或重新计算pe/pb
    return dict_index_base
```

### 函数`show_quantile()`

```
def show_quantile(index_code, p, n, data):
    '''
    展示估值图
    '''
    _df = pd.DataFrame()
    df = data.copy()
    df.index.name = None

    # 一、计算当前百分位高度
    _df[p] = df[p]
    _df = _df.iloc[-n * 244:]
    p_high = [_df[p].quantile(i / 10.0) for i in [3, 5, 7]]
    for p_h, i in zip(p_high, [3, 5, 7]):
        _df[str(i / 10 * 100)+'%'] = p_h

    # 二、计算历史百分位高度
    def _func(c):
        low_p = c[c < c[-1]]
        value = low_p.shape[0] / c.shape[0]
        return value
    _df['history'] = df[p].rolling(n * 244).apply(lambda x: _func(x), raw=True)[-n*244:]

    # 三、计算评估语句
    low_p = _df[_df[p] < _df[p].iloc[-1]]
    quantile_now = low_p.shape[0] / _df.shape[0]  # 当前百分位值
    last_p = _df[p][-1]
    assessment = ''
    if 0 <= quantile_now < 0.1:
        assessment = '超低估'
    elif 0.1 < quantile_now < 0.3:
        assessment = '低估'
    elif 0.3 < quantile_now < 0.4:
        assessment = '适中偏低'
    elif 0.4 < quantile_now < 0.6:
        assessment = '适中'
    elif 0.6 < quantile_now < 0.7:
        assessment = '适中偏高'   
    elif 0.7 < quantile_now < 0.9:
        assessment = '高估'   
    elif 0.9 < quantile_now <= 1:
        assessment = '超高估'   

    title = '{}，当前{}{}，近{}年历史百分位{}，{}'.format(get_security_info(index_code).display_name,
                                              p, round(last_p, 2), n,
                                              str(round(quantile_now * 100, 2)) + '%', assessment)

    _df.plot(secondary_y=['history'], figsize=(18, 10), style=['-', '--', '--', '--', 'y-'], title=title)
```

这个函数是用来给指数估值用的，估值的思路是看当前的市盈率与整个历史区间的市盈率进行对比，看分位数处在什么位置，最后使用图形将它们展示出来。步骤包括：

- 获取指数的pe/pb，然后创建DataFrame并取出近5年的pe数据，并计算出30%，50%和70%的分位数。
- 

## 二、`index_valuation.py`代码解释



## 二、上周计划任务



## 三、本周新学内容

### 1.历史百分位

自己目前在坚持ETF定投，为此还专门在聚宽上按照自己想到的算法来获取当前处于低位的ETF，代码见[价值研究笔记之获取处于历史地位TOP10的ETF基金](https://www.joinquant.com/view/community/detail/b7f2d084d39662b0b21295fe4db25211)，其中的大致思路是计算当前基金累计净值占过去几年最高值的百分比。

我原本以为这个指标就是“历史百分位”，心想怎么这么巧合。但仔细了解之后，发现并不是这样。“历史百分位”指的是按照整个历史日期区间所处的时间长短，比如20%的分位数是56，那么说明指定的日期区间内有20%的时间收盘价是小于56的；如果60%的分位数是89，那么指定的日期区间内有60%的时间收盘价是小于89的。这里的56和89就是相对于20%和60%的分位数。


## 四、下周学习任务

- 微信接口？
