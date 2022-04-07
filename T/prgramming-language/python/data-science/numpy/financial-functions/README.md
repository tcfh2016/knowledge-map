# [Financial functions](https://docs.scipy.org/doc/numpy/reference/routines.financial.html)

## [fv]()

## [pv]()

## [npv]()

## [pmt]()

## [ppmt]()

## [irr](https://docs.scipy.org/doc/numpy/reference/generated/numpy.irr.html)

numpy.irr(values)

返回Internal Rate of Return (IRR, 内部收益率)，IRR是基于复利求取的当NPV为0时的收益率。
输入参数为单维或者多维的数组，每个数组代表每期的输入现金流：负数表示进行投资的现金流，正
数表示收回投资的现金流。

```
>>> round(irr([-100, 39, 59, 55, 20]), 5) # 5表示小数点后5位。
0.28095
>>> round(irr([-100, 0, 0, 74]), 5) # 5表示小数点后5位，第5位为0，省略。
-0.0955
```

## [mirr]()

## [nper]()

## [rate]()
