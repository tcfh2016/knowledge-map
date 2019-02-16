## 坐标轴显示支持中文？

使用如下命令打印出matplotlib能够支持的系统字体：

```
fonts = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

for i in fonts:
    print(i)
```

再设定图形使用的字体：

```
plt.rcParams['font.family']=['STFangsong']
```

## plot线性图添加格式字符串来显示离散值

```
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,"ob") # o表示“圆标记”，b表示“蓝色”。
plt.show()
```

## 同一窗口绘制多条线条或者多张图形

[](label="cosine")
