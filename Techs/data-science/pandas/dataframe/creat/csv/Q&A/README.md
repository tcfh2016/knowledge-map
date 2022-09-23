## 什么是CSV

CSV全称为[Comma-separated values](https://en.wikipedia.org/wiki/Comma-separated_values)



## 读取csv 调用`to_numeric()`出现`ValueError: Unable to parse string " " at position 0`错误

读取lrb000898.csv, zcfzb000898.csv进行数据清洗、转换没有问题，但读取xjllb000898.csv的时候出现错误:

```
File "C:\Users\lianbche\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\tools\numeric.py", line 135, in to_numeric
  coerce_numeric=coerce_numeric)
File "pandas\_libs\lib.pyx", line 1925, in pandas._libs.lib.maybe_convert_numeric
ValueError: Unable to parse string " " at position 0
```

调试发现多转换了一列，查看原始文件发现在xjllb000898.csv每行末多了一个空行，因此问题出在转换空行时的错误。

参考：

- [pandas.to_numeric - find out which string it was unable to parse](https://stackoverflow.com/questions/40790031/pandas-to-numeric-find-out-which-string-it-was-unable-to-parse)
