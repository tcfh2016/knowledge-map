#  plotly

`plotly`是一个交互式的Python绘图库，支持统计、财务、地理、科学和三维领域内40多种图形。

```
C:\Users\lianbche\AppData\Local\Programs\Python\Python312\python.exe -m pip --proxy ip:port install plotly==5.24.1
```

优点：

- 更美观的图形：背景、坐标轴标签自然分散
- 更灵活：指定`color`自动给不同的值附上颜色，并不需要指定具体的颜色


## VSCODE

在VSCODE里面测试下面代码，会自动在浏览器里面打开图形：

```
import plotly.express as px

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])

fig.write_html('first_figure.html', auto_open=True)
```

如果需要将图形显示在Jupyter notebook里面，需要先安装`ipywidgets`，`nbformat`。


# 绘图

## 大小

可以通过`width`和`height`，默认宽700像素，高450像素：

```
fig.update_layout(autosize=<VALUE>)

```

## 图例

```
fig.update_layout(legend=dict(
    orientation="h",
    entrywidth=70,
    yanchor="bottom",
    xanchor="right",
    y=1.02,
    x=1
))
```

- `xref`/`yref`，宽度和高度是以绘图区（`paper`）还是整个幕布（`container`）参考
- `x`/`y`，设置相对`xref`/`yref`的位置，取值在0~1，默认值0.5
- `xanchor`，设置标题相对于`x`的距离，取值："auto" | "left" | "center" | "right"



参考：

- [Legends in Python](https://plot.ly/python/legend/)
- [](https://plotly.com/python/reference/layout/)


## `plotly.express`

参考：

- [plotly.express: high-level interface for data visualization](https://plotly.com/python-api-reference/plotly.express.html)


## `go.Scatter`

```
fig = go.Figure()
fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines',
                    name='lines'))
fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='lines+markers',
                    name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                    mode='markers', name='markers'))

fig.show()
```

## subplots

对于`make_subplots()`的使用：

- `shared_xaxes=True`，共享x轴



```
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=3, cols=1)

fig.append_trace(go.Scatter(
    x=[3, 4, 5],
    y=[1000, 1100, 1200],
), row=1, col=1)

fig.append_trace(go.Scatter(
    x=[2, 3, 4],
    y=[100, 110, 120],
), row=2, col=1)

fig.update_layout(height=600, width=600, title_text="Stacked Subplots", legend)
fig.show()
```

参考：

- [](https://plot.ly/python/subplots/)

## 参考：

- [Getting Started with Plotly in Python](https://plot.ly/python/getting-started/)