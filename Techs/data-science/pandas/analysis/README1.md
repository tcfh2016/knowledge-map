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

- [Subtract previous row value from the current row value in a Pandas column](https://stackoverflow.com/questions/57801048/subtract-previous-row-value-from-the-current-row-value-in-a-pandas-column)

## 使用多列来得到新列

```
def my_func( year,a,b,c,d,e ):
    #This function can be longer and do more things
    return np.nan if year < 2020 else a + ( ( (b + c) / (b + c + d) ) * e )


df['X'] = df.apply( lambda x: my_func( x.name, x.A, x.B, x.C, x.D, x.E ), axis = 1 )
```

参考：

- [Pandas : How to apply a function with multiple column inputs and where condition](https://stackoverflow.com/questions/72144769/pandas-how-to-apply-a-function-with-multiple-column-inputs-and-where-condition)