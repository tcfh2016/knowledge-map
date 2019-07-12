# [matplotlib.pyplot](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.html)

## [matplotlib.pyplot.gca](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.gca.html)

通过参数获取对应图形的坐标轴，或者创建一个坐标轴。可传递给projection的值可以通过使用
`matplotlib.projections.get_projection_names()`获取到

```
ax = fig.gca(projection='3d') # 获取3d
ax = fig.gca(projection='polar') # 获取当前极坐标轴
```

参考：

- [What does the command ax = fig.gca (projection='3d') do in NumPy?](https://www.quora.com/What-does-the-command-ax-fig-gca-projection-3d-do-in-NumPy)
