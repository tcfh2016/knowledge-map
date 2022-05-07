好久之前注册了聚宽的账号，但耍玩几天之后也没有再碰，知道最近一次因为要写作《洋河股份初分
析》再次回到聚宽上获取数据，觉得非常方便。

今天浏览社区帖子，发现有人提到当前论坛上不够活跃，帖子内容许多不利于初学者，使得很多人不
知道从何开始。因此，自己想到可以把自己从本周开始在聚宽上面的学习记录笔记下来。

## 代码笔记

### 时间变量

```
log.info('函数运行时间(before_market_open)：'+str(context.current_dt.time()))
# 输出：函数运行时间(before_market_open)：09:00:00
```

```
log.info('函数运行时间(before_market_open)：'+str(context.current_dt.date()))
# 输出：函数运行时间(before_market_open)：2019-08-01
```

```
log.info('函数运行时间(before_market_open)：'+str(context.current_dt))
# 输出：函数运行时间(before_market_open)：2019-08-01 09:00:00
```

### 仓位控制

https://www.joinquant.com/help/api/help?name=api#%E5%AF%B9%E8%B1%A1


```
context.portfolio.positions[security].closeable_amount > 0
```
