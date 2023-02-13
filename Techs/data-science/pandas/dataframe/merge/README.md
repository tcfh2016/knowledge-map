## 怎样在行方向上进行合并

```

```

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