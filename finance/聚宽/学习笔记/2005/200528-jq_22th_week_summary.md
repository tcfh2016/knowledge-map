# 聚宽学习周记二二：详解@云帆的“高频因子探索——动量交易”

本周将ETF投资参考日报发布到模拟交易，这样以后就能收到每个交易日之后的ETF还有指数的运行状态了，尽管模拟交易有一定的延时，今天凌晨3点才能拿到前天收盘时候的内容，但这对于ETF定投来说是没有问题的，它本身并不需要频繁的交易，所以是适用的。

上周制定的计划里面，我又要开始学习聚宽社区2019年的精选文章了。由于我在打算着怎么将当前的学习和之前的学习积累起来，所以选择了一篇与交易直接有关的文章，即@云帆的[高频因子探索——动量交易](https://www.joinquant.com/view/community/detail/22472)。脑中所抱有的期望是在接触一些交易上的算法后可以将这段时间对于指数的理解结合起来，这样就可以尝试编写策略了。

## 一、代码解释

### 代码片段1：获取交易日列表

```
def get_tradeday_list(start, end, frequency=None, count=None):
    '''
    获取日期列表
    input:
    start:str or datetime,起始时间，与count二选一
    end:str or datetime，终止时间
    frequency:
        str: day,month,quarter,halfyear,默认为day
        int:间隔天数
    count:int,与start二选一，默认使用start
    '''
    if isinstance(frequency, int):
        all_trade_days = get_trade_days(start, end)
        trade_days = all_trade_days[::frequency]
        days = [datetime.datetime.strftime(i, '%Y-%m-%d') for i in trade_days]
        return days

    if count != None:
        df = get_price('000001.XSHG', end_date=end, count=count)
    else:
        df = get_price('000001.XSHG', start_date=start, end_date=end)
    if frequency == None or frequency == 'day':
        days = df.index
    else:
        df['year-month'] = [str(i)[0:7] for i in df.index]
        if frequency == 'month':
            days = df.drop_duplicates('year-month').index
        elif frequency == 'quarter':
            df['month'] = [str(i)[5:7] for i in df.index]
            df = df[(df['month'] == '01') | (df['month'] == '04') | (df['month'] == '07') | (df['month'] == '10')]
            days = df.drop_duplicates('year-month').index
        elif frequency == 'halfyear':
            df['month'] = [str(i)[5:7] for i in df.index]
            df = df[(df['month'] == '01') | (df['month'] == '06')]
            days = df.drop_duplicates('year-month').index
    trade_days = [datetime.datetime.strftime(i, '%Y-%m-%d') for i in days]
    return trade_days
```

这个函数的目的在于按照不同的频率获取日期列表，它同时支持按照数字的形式和按照单词的形式获取：一、按数字的形式，即按间隔x个交易日；二、按单词的形式，即按天、月、季度、半年。

注意这两种形式的异同，它们两者的相同之处都是基于交易日，而不是单纯的天数。但是，按数字的形式虽然看起来更灵活，但是没有办法按照自然月、季度、半年来获取制定日期，这也是两者需要同时存在的地方。

对于如上代码的理解需要三方面的知识：

**1）聚宽提供的服务函数`get_trade_days`的作用**

这个我在前面最开始的周记里面每次都讲解，这里不重复了。简单来说就是获取交易日列表，但它的粒度是以“单个交易日”为单位，不支持按周、月、季度等多样化的获取方式。

**2）Python时间服务函数库`datetime`的`strftime`方法的作用**

它是用来将一个时间对象转换成字符串的形式，调用方式很简单，只需要直接调用`time`, `date`或者`datetime`对象的方法即可：

```
date = dt.date(2008, 2, 8)
print(date) # 结果为：2008-02-08

fmt = '%Y%m%d'
print(date.strftime(fmt)) # 结果为：20080208
```

可以参考[strftime() and strptime() Behavior](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)。

**3）Python数据处理函数库`pandas`里二维数据表DataFrame的基础知识**

- 首先需要知道索引(index)的概念。索引其实就类似我们excel里面第一列的那些序号，只不过在DataFrame里面这些索引可以有多种形式。这里适用索引也是因为要获得那些交易日的数据。
- 其次要知道DataFrame的条件选择表达式。条件表达式是用来选择复合要求的那些行的数据，比如`df[(df['month'] == '01')`这句就是以“列名为'month'”的那一列作为选择标准，然后选择出这一列里面“值为‘01’”的所有行。
- 还有`drop_duplicates()`。用来删除重复的记录，这里主要是为了按自然月以上的频度挑选时间时使用，因为要先构建出辅组列，在基于其上进行过滤。

### 代码片段2：获取指定交易日前一个交易日最后一段时间的动量收益

```
def get_profit_minutes_period(stocks,date,n=5,next_n=120):
    '''
    计算date前一天最后一段时间的动量收益
    注意：获取的数据是输入时间前一天的数据
    input:

    stocks:输入股票列表
    date:时间，数据为前一天
    n:开盘收益计算时间长度
    next_n:开盘后收益计算长度

    '''
    price = get_price(stocks,end_date=date,frequency='1m',count=n+next_n,fields=['close'])['close']
    l = len(price.shape)

    if l > 1:
        profit_open = price.pct_change(n-1)
        profit_open = profit_open.iloc[n-1]
        profit_next = price.pct_change(next_n)
        profit_next = profit_next.iloc[-1]
        profit = pd.concat([profit_open,profit_next],axis=1)
        profit.columns = ['open_profit','next_profit']
    else:
        profit_open = price.pct_change(n)
        profit_open = profit_open.iloc[n]
        profit_open = pd.DataFrame([profit_open],index=[stocks])
        profit_next = price.pct_change(next_n - 1)
        profit_next = profit_next.iloc[-1]
        profit_next = pd.DataFrame([profit_next],index=[stocks])
        profit = pd.concat([profit_open,profit_next],axis=1)
        profit.columns = ['open_profit','next_profit']
    return profit
```

动量这个词其实在第十四周和第十五周分析@东南有大树的那篇[用指数战胜指数，ETF二八轮动对冲模型](https://www.joinquant.com/view/community/detail/19490)就了解过了。“动量”是物理学里面的专有名词，我们这里的动量借用来指股价维持趋势的可能性，通过计算股价的涨幅来判断。

之前我们学习到的动量的计算方法是通过`(a - b) / b`这种形式，但今天看了这段代码算是涨知识了，原来pandas里面直接有函数来完成动量的计算：`pct_change()`。这个函数是用来计算行与行之间的数值变动，以百分比表示，默认计算相对于前一行的变化情况。比如：

```
             A   B   C   D
2000-01-02  14   5  20  14
2000-01-09   4   2  20   3
2000-01-16   5  54   7   6
2000-01-23   4   3  21   2
2000-01-30   1   2   8   6
2000-02-06  55  32   5   4

                    A          B         C         D
2000-01-02        NaN        NaN       NaN       NaN
2000-01-09  -0.714286  -0.600000  0.000000 -0.785714
2000-01-16   0.250000  26.000000 -0.650000  1.000000
2000-01-23  -0.200000  -0.944444  2.000000 -0.666667
2000-01-30  -0.750000  -0.333333 -0.619048  2.000000
2000-02-06  54.000000  15.000000 -0.375000 -0.333333
```

代码里面传入的其他数值n/next_n，计算的是每一行数据相对于前面n/next_n行的涨幅。这个函数可以这么解释：

- 首先，获取前一个交易日最后 n + next_n 分钟的交易数据
- 其次，计算这段交易数据里面前第n分钟相对于第1分钟的涨幅
- 最后，计算这段交易数据里面最后1分钟相对于前next_n分钟的涨幅

代码里面的`l > 1`主要是用来判断当前是否获取的是单只股票还是多只股票，处理上小有差异：计算的单只股票不是DataFrame类型，需要先创建，然后才能够使用`concat`进行合并。

### 代码片段3：获取指定交易日前一个交易日开盘时的动量收益

```
def get_open_profit_minutes_period(stocks,date,n=5,next_n=120):
    '''
    计算date前一天开盘的动量收益
    注意：获取的数据是输入时间前一天的数据
    input:

    stocks:输入股票列表
    date:时间，数据为前一天
    n:开盘收益计算时间长度
    next_n:开盘后收益计算长度

    '''
    price = get_price(stocks,end_date=date,frequency='1m',count=240,fields=['close'])['close']
    l = len(price.shape)

    if l > 1:
        profit_open = price.pct_change(n)
        profit_open = profit_open.iloc[n]
        profit_next = price.pct_change(next_n)
        profit_next = profit_next.iloc[n+next_n+1]
        profit = pd.concat([profit_open,profit_next],axis=1)
        profit.columns = ['open_profit','next_profit']
    else:
        profit_open = price.pct_change(n)
        profit_open = profit_open.iloc[n]
        profit_next = price.pct_change(next_n)
        profit_next = profit_next.iloc[n+next_n+1]
        profit_open = pd.DataFrame([profit_open],index=[stocks])
        profit_next = pd.DataFrame([profit_next],index=[stocks])
        profit = pd.concat([profit_open,profit_next],axis=1)
        profit.columns = ['open_profit','next_profit']
    return profit
```

在我们详细地理解了前面那个函数之后，这个函数理解起来就简单多了，可以解释如下：

- 首先，获取前一个交易日整天的以分钟为单位的交易数据（240分钟=4小时）
- 其次，计算这段交易数据里面前第n分钟相对于第1分钟的涨幅
- 最后，计算这段交易数据里面最后1分钟相对于前next_n分钟的涨幅

所以正如函数的注释而言，函数`get_profit_minutes_period()`衡量的是前一个交易日收盘那段时间的动量，而函数`get_open_profit_minutes_period()`衡量的是前一个交易日开盘那段时间的动量。


### 代码片段4：按天为单位计算动量

```
def get_day_profit_backward(stocks,end_date,start_date=None,count=3):
    '''
    向前计算收益率，得到的收益率是输入时间end_date向前计算，不包括当天
    input：
    stocks:list or Series,股票代码

    start_date:开始时间
    end_date：结束时间
    count:与start_date二选一，向前取值个数
    pre_num:int,向后计算的天数
    output:
    profit:dataframe,index为日期，columns为股票代码，values为收益率
    '''
    if count == -1:
        price = get_price(stocks,start_date,end_date,fields=['close'])['close']
    else:
        price = get_price(stocks,end_date=end_date,count=count+1,fields=['close'])['close']
    profit = price.pct_change(count-1)
    profit = profit.iloc[-2]
    if isinstance(profit,pd.Series):
        profit = profit.to_frame()
    else:
        profit = pd.DataFrame([profit],index=[stocks])

    profit.columns = ['back_profit']
    return profit
```

前面的函数`get_profit_minutes_period()`和`get_open_profit_minutes_period()`都是计算指定交易日内分钟级别的动量数据，而函数`get_day_profit_backward()`计算的是某个交易日相对于前几个交易日的动量数据。但是方法都是一样的，都是使用`pct_change`来完成。


### 代码片段5：获取沪深300指数成分股的动量数据

```
def get_open_and_backward_profit(stocks,date_list,n=5,next_n=60,count=3):
    '''
    注意：时间对齐
    '''
    l = len(date_list)

    dic = {}
    for d in range(l - 1):
        date = date_list[d+1]
        open_profit = get_profit_minutes_period(stocks,date,n,next_n)
        date = date_list[d]
        backward_profit = get_day_profit_backward(stocks,date,count)
        profit = pd.merge(open_profit,backward_profit,left_index=True,right_index=True,how='inner')
        dic[date] = profit
    return dic


start_date = '2017-01-01'
end_date = '2019-09-05'
date_list = get_tradeday_list(start=start_date,end=end_date)

dic_res_5_60_3_hs300 = get_open_and_backward_profit(stocks,date_list,n=5,next_n=120,count=3)

with open('movement_5_120_3_afternoon.pkl','wb') as pk_file:
    pickle.dump(dic_res_5_60_3_hs300,pk_file)
with open('movement_5_120_3_afternoon.pkl','rb') as pk_file:
    dic_res = pickle.load(pk_file)    
```

以上这些代码是对前面讲解的获取指定交易日前一个交易日最后分钟级别的动量函数`get_profit_minutes_period`和获取指定交易日相对于前几个交易日的动量函数`get_day_profit_backward`的应用，获取的是沪深300指数所有成分股在指定多个日期的动量数据。这些数据是按照字典形式组织起来的，其中的“键”为日期，“值”为300只股票的动量数据，然后将其保存到文件中。


### 代码片段6：

```
def combine_data(dic_res,sel_percent):
    '''
    字典数据按时间轴合并
    '''

    keys = list(dic_res.keys())
    data_list = []
    for key in keys:
        data = dic_res[key]
        data_list.append(data)
    all_data = pd.concat(data_list)
    test_data = all_data.dropna()
    new_col = ['back_profit','open_profit','next_profit']
    all_data = all_data[new_col]
    all_data.index = np.arange(len(all_data))
    #删除开盘停牌股票
    sel_data = all_data[all_data['open_profit'] == 0].index
    all_data = all_data.drop(sel_data,axis=0)
    length = len(all_data)

    '''
    #获取训练数据和测试数据
    cut_point = int(train_percent * length)
    print(cut_point)
    train_data = all_data[:cut_point]
    test_data = all_data[cut_point:]
    '''
    #剪切中间部分
    start_point = int(sel_percent[0] * length)
    end_point = int(sel_percent[1] * length)
    sel_data = all_data[start_point:end_point]
    return sel_data

def cut_data(data,n):
    '''
    将数据分层，基于分位数,最后一列作为收益不进行分层
    input:
    data:dataframe or series, 输入数据
    n: 分层数
    '''
    f = 1 / n
    l = []
    for i in range(n):
        l.append(f*(i+1))
    q = data.quantile(l)
    qv = q.values
    shape = qv.shape
    col = data.columns
    for i in range(shape[1] - 1): #最后一层收益不分层
        for j in range(shape[0]):
            data[col[i]][data[col[i]] <= qv[j][i]] = j + 1
    return data.dropna()

#单维度分析
def calculate_IC(factor,profit,method='pearson'):
    '''
    input:
    factor: 因子值
    profit:收益值
    me t hod:默认计算pearson相关系数
    输出：
    i c值和对应的pvalue
    '''
    if method == 'pearson':
        ic,pvalue = st.spearmanr(factor,profit)
    else:
        ic,pvalue = st.pearsonr(factor,profit)

    return ic,pvalue
```
