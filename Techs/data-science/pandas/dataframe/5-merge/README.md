## pd.concat()

使用`pd.concat()`函数来完成多个DataFrame的连接操作，主要的参数为`axis`, `join`和`ignore_index`：

- `axis`决定在纵向（`axis=0`）还是横向（`axis=1`）连接, 默认为纵向连接。
- `join`决定连接时候的方式，`join='inner'`表示内部合并，`outer`表示外部合并，默认为外部合并。
- `ignore_index`确定是否需要重排合并之后的DataFrame。


这里对于`axis`的理解需要辨析一下，也就是要能够快速的反映出`axis=0/1`的含义。当`axis=0`指定的是“X轴”，相当于是“不同行以X轴进行纵向连接”，当`axis=1`指定的是`Y轴`，相当于是“不同列以Y轴进行横向连接”。

理解清楚两者之间的差别之后，就能够理解`join`参数通常是在`axis=0`既以X轴进行纵向连接的时候使用，横向连接因为轴是纵轴，通常是相等的，所以不需要。

### 纵向连接

```
pd.concat([df3, df4], axis=0, join='inner', ignore_index=True)
```

### 横向连接

同样，使用`pd.concat()`也可以进行横向连接，此时需要将`axis`参数设置为`1`。横向连接之后列的数量会增加，

```
pd.concat([df1, df2], axis=1)
```


## pd.merge()

怎样在行方向上进行合并：

使用`pd.merge(df1, df2, on=['column'])`。


## 怎样merge多个DataFrame数据

比如我有下面三个DataFrame数据，怎么把它们合并在一起：

```
# 2010年
total_operating_revenue  total_operating_cost  total_profit  np_parent_company_owners
0              444756672.0           216138608.0   217983440.0               163337936.0

# 2011年
   total_operating_revenue  total_operating_cost  total_profit  np_parent_company_owners
0              504532160.0           223844592.0   297411680.0               222218576.0

# 2012年
   total_operating_revenue  total_operating_cost  total_profit  np_parent_company_owners
0              586157056.0           286812384.0   341199296.0               256545872.0
```

上面这种方式的“合并”实际上是需要在列的方向上进行连接，可以使用`concat()`函数。由于每个DataFrame的行标签都是“0”，所以需要在连接之前或者连接之后进行更改。


## 怎样往已有DataFrame里面添加一行？

```
df.loc[len(df.index)] = ['Amy', 89, 93] 
```

- [](https://www.geeksforgeeks.org/how-to-add-one-row-in-an-existing-pandas-dataframe/)