## sort_values()

对某列的series进行排序：

```
movies['title'].sort_values() # 默认以升序排列
movies['title'].sort_values(ascending=False) # 以降序排列
```

对整个dataframe以某列为标准进行排序：

```
movies.sort_values('title') # 升序排列，不会更改原有dataframe
movies.sort_values('title', ascending=False) # 降序排列，不会更改原有dataframe
movies.sort_values(['content_rating', 'duration']) # 以两列进行排序
```

## 仅仅针对前面N行排序

先部分排序，再拼接起来：

```
pd.concat([df[0:N].sort_values('A'), df[N:]])
```