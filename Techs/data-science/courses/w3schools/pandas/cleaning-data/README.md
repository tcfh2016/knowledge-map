## Cleaning Data

数据清理指的是处理掉数据集中的“坏数据”，它们包括：

- 数据单元是空值
- 数据单元中的格式错误
- 错误数据
- 重复数据

以下是举例。

1）空值

```
    Duration          Date  Pulse  Maxpulse  Calories
0         60  '2020/12/01'    110       130     409.1
1         NaN '2020/12/01'    110       130     409.1
```

2）格式错误

```
    Duration          Date  Pulse  Maxpulse  Calories
0         60    2020/12/01    110       130     409.1
1         NaN '2020/12/01'    110       130     409.1
```

3）错误数据

```
    Duration          Date  Pulse  Maxpulse  Calories
0        660  '2020/12/01'    110       130     409.1
1         50  '2020/12/01'    110       130     409.1
```

4）重复数据


```
    Duration          Date  Pulse  Maxpulse  Calories
0         50  '2020/12/01'    110       130     409.1
1         50  '2020/12/01'    110       130     409.1
```
