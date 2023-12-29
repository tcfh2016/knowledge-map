## 字符串方法

当某列是字符串时，可以用`.str`对该列进行操作。


## 求每列最大值与最小值之差

使用`apply`将函数应用到每列：

```
df.apply(lambda x: x.max() - x.min())
```

## 求与前一行的差值

```
df['output']=df['input'] -df['input'].shift(1)
```

参考：

- [](https://stackoverflow.com/questions/57801048/subtract-previous-row-value-from-the-current-row-value-in-a-pandas-column)