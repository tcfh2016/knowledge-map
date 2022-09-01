## Cleaning Wrong Data

“错误的数据”并非“空值”或者“错误的格式”，而是在逻辑范围上不满足对应列的定义范围。那么处理这种错误数据常用方法就是修改它的值。

处理空值的时候有`fillna()`这种批量化的方法，但是处理“错误数据”你只能定位到具体的值然后修改，如`df.loc[7, 'Duration'] = 45`。如果错误数据很多，那么需要编写循环进行多次替换：

```
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
```

当然，也可以直接移除对应行：

```
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
```
