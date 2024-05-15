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