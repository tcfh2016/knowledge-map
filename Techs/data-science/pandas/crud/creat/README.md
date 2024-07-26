## 创建DataFrame

最简单的，就是从一个空的DataFrame开始，可以指定列标签，也可以不指定：

```
# 创建一个空的DataFrame
empty_df = pd.DataFrame()

# 创建一个带列标签的空DataFrame
col_names = ['A', 'B', 'C', 'D']
empty_df_with_header = pd.DataFrame(columns=col_names)

# 从空的DataFrame开始添加新列
df = pd.DataFrame(index=['a', 'b', 'c', 'd'])

df['floats'] = (1.5, 2.5, 3.5, 4.5)
df['names1'] = ('Yves', 'Guido', 'Felix', 'Francesc')
df['names2'] = pd.DataFrame(['Yv', 'Gu', 'Fe', 'Fr'],
                            index=['d', 'a', 'b', 'c']) # 添加新的DataFrame对象。
print(df)
```

## 其他创建方法

创建DataFrame 可以有以下几种方法：

- 序列，包括元组、列表。一维的数据作为列，二维的数据行列和DataFrame对应。
- 字典。默认以key作为列标签

## 常见问题


