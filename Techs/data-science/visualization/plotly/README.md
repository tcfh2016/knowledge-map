#  plotly

`plotly`是一个交互式的Python绘图库，支持统计、财务、地理、科学和三维领域内40多种图形。

```
C:\Users\lianbche\AppData\Local\Programs\Python\Python312\python.exe -m pip --proxy ip:port install plotly==5.24.1
```

优点：

- 更美观的图形：背景、坐标轴标签自然分散
- 更灵活：指定`color`自动给不同的值附上颜色，并不需要指定具体的颜色

之所以觉得使用`plotly`比原始的`matplotlib`好是因为它做了一些封装，比如如果在画散点图的时候指定`color`必须要是具体的颜色值，但是`plotly`可以直接将不同的值映射为不同的颜色并显示图例。

参考：

- [Getting Started with Plotly in Python](https://plot.ly/python/getting-started/)


## VSCODE

在VSCODE里面测试下面代码，会自动在浏览器里面打开图形：

```
import plotly.express as px

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])

fig.write_html('first_figure.html', auto_open=True)
```

如果需要将图形显示在Jupyter notebook里面，需要先安装`ipywidgets`，`nbformat`。


# 绘图

## `plotly.express`

基本的效果：

```
import plotly.express as px

fig = px.scatter(x=df['a'], y=df['b'], color=df['c'])
#相同效果：fig = px.scatter(df, x='a', y='b', color='c') 

fig.show()
```

稍微进一步的划分，使用`facet_row`和`facet_col`来按照其他列画出多个子图：

```
px.scatter(cu_fc, x='seconds', y='unsentGtpPackets', color='ueIdCuE1Cp', 
                 facet_col='bearerGroupId', facet_row='bearerId')
```

参考：

- [plotly.express: high-level interface for data visualization](https://plotly.com/python-api-reference/plotly.express.html)
- [Plotly Python Open Source Graphing Library Basic Charts](https://plotly.com/python/basic-charts/)


## 折线图

```
fig = px.line(df, x="year", y="lifeExp", color='country')
fig.show()
```


## 柱状图


1）基本的柱状图

最基本的柱状图，传入对应的dataframe，然后指定两列作为x和y轴：

```
import plotly.express as px

fig = px.bar(df, x='year', y='pop')
fig.show()
```

与`df.plot.bar()`的区别：

- `df.plot.bar()`不会对指定的数据列进行聚合处理，比如x轴对应列里面有重复元素，`df.plot.bar()`不会去重，但`px.bar()`会去重，然后y轴的列会堆叠展示。


2）堆叠的柱状图

如果有多列的数据，也就是想在二维的柱状图体现出另外第三维的数据，那么可以通过更多的参数，比如这里多用了`color`参数：

```
fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
fig.show()
```

如果要将多列堆叠在一起，那么用参数`y`来指定多列（如果单列展示堆叠，可以通过`color`参数来指定）：

```
fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
fig.show()
```

3）多柱形图

使用`barmode = 'group'`来设定多柱状图。或者改由`px.histogram()`来绘制。

参考：

- [Bar Charts in Python](https://plotly.com/python/bar-charts/)
- [Plotly Express Wide-Form Support in Python](https://plotly.com/python/wide-form/)
- [Plotly Express Arguments in Python](https://plotly.com/python/px-arguments/)


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

参考：

- [Line Plot with go.Scatter](https://plotly.com/python/graph-objects/)


## treadline

参考：

- [Linear and Non-Linear Trendlines in Python](https://plotly.com/python/linear-fits/)
- [Adding Trendline on Plotly Scatterplot](https://stackoverflow.com/questions/65135524/adding-trendline-on-plotly-scatterplot)

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

fig.update_layout(height=600, width=600, title_text="Stacked Subplots")
fig.update_xaxes(title_text="slot", row=2, col=1)

fig.show()
```

参考：

- [Subplots in Python](https://plot.ly/python/subplots/)


# 设置

## 大小

可以通过`width`和`height`，默认宽700像素，高450像素：

```
fig.update_layout(autosize=<VALUE>)
fig = px.bar(df_bar, x='country', y='in', color='fruit', width=600, height=400)

```

- `width=600, height=400`：设置大小
- `labels={'pop':'population of Canada'`：修改标签，从默认的`pop`更改为`population of Canada`


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
- [Python Figure Reference: layout](https://plotly.com/python/reference/layout/)

