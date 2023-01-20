## Cannot perform 'rand_' with a dtyped...

想根据两列的查询数据来查询满足条件的行时提示“`Cannot perform 'rand_' with a dtyped [float64] array and scalar of type [bool]`”

```
df = df[df['市盈率(TTM)'] < 5.0 & df['市净率'] < 0.5]
```

解决方案，在不同条件上加上括号。比如上面的修改为：

```
df = df[(df['市盈率(TTM)'] < 5.0) & (df['市净率'] < 0.5)]
```

参考：

- [TypeError: Cannot perform 'rand_' with a dtyped [float64] array and scalar of type [bool]](https://stackoverflow.com/questions/60654781/typeerror-cannot-perform-rand-with-a-dtyped-float64-array-and-scalar-of-ty)