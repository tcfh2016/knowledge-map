# [matplotlib.pyplot](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.html)

## [matplotlib.pyplot.ylim](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.ylim.html)

设置y坐标轴的极值。在2.x版本和3.x版本在参数名称上不同之处，比如2.x版本：

```
ylim( (ymin, ymax) )  # set the ylim to ymin, ymax
ylim( ymin, ymax )    # set the ylim to ymin, ymax
```

3.x版本为：

```
ylim((bottom, top))   # set the ylim to bottom, top
ylim(bottom, top)     # set the ylim to bottom, top
```

参考:

- [matplotlib.pyplot.ylim - 2.1.0](https://matplotlib.org/2.1.0/api/_as_gen/matplotlib.pyplot.ylim.html)

## [matplotlib.pyplot.gca](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.gca.html)

通过参数获取对应图形的坐标轴，或者创建一个坐标轴。可传递给projection的值可以通过使用
`matplotlib.projections.get_projection_names()`获取到

```
ax = fig.gca(projection='3d') # 获取3d
ax = fig.gca(projection='polar') # 获取当前极坐标轴
```

参考：

- [What does the command ax = fig.gca (projection='3d') do in NumPy?](https://www.quora.com/What-does-the-command-ax-fig-gca-projection-3d-do-in-NumPy)
