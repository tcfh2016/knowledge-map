# 数据操作

## 移位：`shift()`

```
df.shift(period=1, frequ=None, axis=0)
```

求与前一行的差值可使用`df['output']=df['input'] -df['input'].shift(1)`。


参考：

- [Subtract previous row value from the current row value in a Pandas column](https://stackoverflow.com/questions/57801048/subtract-previous-row-value-from-the-current-row-value-in-a-pandas-column)


## `apply()`

1）使用`apply`将函数应用到每列，求每列最大值与最小值之差

```
df.apply(lambda x: x.max() - x.min())
```


2）使用多列来得到新列

```
def my_func( year,a,b,c,d,e ):
    #This function can be longer and do more things
    return np.nan if year < 2020 else a + ( ( (b + c) / (b + c + d) ) * e )


df['X'] = df.apply( lambda x: my_func( x.name, x.A, x.B, x.C, x.D, x.E ), axis = 1 )
```

参考：

- [Pandas : How to apply a function with multiple column inputs and where condition](https://stackoverflow.com/questions/72144769/pandas-how-to-apply-a-function-with-multiple-column-inputs-and-where-condition)


# 数据分析


## pivot_table

`pivot_table`用来进行数据透视的功能，比如有下面这些数据：

```
     A    B      C  D  E
0  foo  one  small  1  2
1  foo  one  large  2  4
2  foo  one  large  2  5
3  foo  two  small  3  5
4  foo  two  small  3  6
```

使用`pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc="sum")`便是以`A`,`B`两列作为行，以`C`列作为列，值以`D`列的`sum`进行数据透视，可以得到：

```
C        large  small
A   B                
foo one    4.0    1.0
    two    NaN    6.0
```

参考：

- [pivot_table](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html)