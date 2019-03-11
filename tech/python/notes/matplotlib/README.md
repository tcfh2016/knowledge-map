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
plt.grid(True) # 添加网格
plt.axis('tight') # 调整坐标宽度
plt.xlim(-1, 20)  # 设置x轴值显示范围
plt.ylim(-5, 5) # 设置y轴值显示范围
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,"ob") # o表示“圆标记”，b表示“蓝色”。
plt.show()
```

## 颜色和样式

```
plt.plot(y.cumsum(), 'ro') # 设置颜色为红色，样式为圆形。
```

颜色：

|Character|Color|
|-|-|
|b|Blue|
|g|Green|
|r|Red|
|c|Cyan|
|m|Magenta|
|y|Yellow|
|k|Black|
|w|White|

样式：
|Character|Symbol|
||-|-|
|-|Solid line style|
|--|Dashed line style|
|-.|Dash-dot line style|
|:|Dotted line style|
|.|Point marker|
|,|Pixel marker|
|o|Circle marker|
|v|Triangle_down marker|
|^|Triangle_up marker|
|<|Triangle_left marker|
|>|Triangle_right marker|
|1|Tri_down marker|
|2|Tri_up marker|
|3|Tri_left marker|
|4|Tri_right marker|
|s|Square marker|
|p|Pentagon marker|
|*|Star marker|
|h|Hexagon1 marker|
|H|Hexagon2 marker|
|+|Plus marker|
|x|X marker|
|D|Diamond marker|
|d|Thin diamond marker|
|||Vline marker|

## 使用plt.legend为不同的数据集添加标签

plt.legend接收不同的位置参数，0表示最佳显示位置（尽可能不阻挡数据的显示），参数列表如下：

|Loc|Description|
|-|-|
|Empty|Automatic|
|0|Best possible|
|1|Upper right|
|2|Upper left|
|3|Lower left|
|4|Lower right|
|5|Right|
|6|Center left|
|7|Center right|
|8|Lower center|
|9|Upper center|
|10|Center|

```
plt.plot(y[:, 0], lw=1.5, label='1st') # 设置第1列数据集的标签为1st。
plt.plot(y[:, 1], lw=1.5, label='2nd') # 设置第1列数据集的标签为2nd。
plt.legend(loc=0) # 使用legend, loc设置位置
```

## 使用两个y坐标轴来显示两个数量级数据集的展示

```
np.random.seed(2000)
y = np.random.standard_normal((20, 2))
print(y)

fig = plt.figure(figsize=(7, 4)) # 设置图形大小

ax1 = fig.subplots()
plt.plot(y[:, 0], 'b', lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro') # 设置颜色为红色，样式为圆形。
plt.legend(loc=8)

ax2 = ax1.twinx()
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
plt.plot(y[:, 1], 'ro') # 设置颜色为红色，样式为圆形。
plt.legend(loc=0) # 使用legend, loc设置位置
plt.ylabel('value 2nd') # 第二个y坐标

plt.grid(True) # 添加网格
plt.axis('tight') # 调整坐标宽度
plt.xlabel('index') # 设置x轴标签
plt.ylabel('value') # 设置x轴标签
plt.title('A Simple Plot') # 设置图形标题
plt.show()
```

## 同一窗口绘制多条线条或者多张图形

```
plt.subplot(1,  2,  1) # 同一窗口第1副图
plt.plot(periods_list, AC_payment_per_month_list, color="blue", linestyle="-", label="等额本金月还款")
plt.plot(periods_list, ACPI_payment_per_month_list, color="red", linestyle="-", label="等额本息月还款")
plt.legend(loc='upper center', frameon=False) # 设置label的位置
plt.xlabel('期数 [月]')
plt.ylabel('金额 [元]')
plt.title('月还款总额')

plt.subplot(1,  2,  2) # 同一窗口第2副图
plt.plot(periods_list, AC_interest_per_month_list, color="blue", linestyle=":", label="等额本金月利息")
plt.plot(periods_list, AC_capital_per_month_list, color="blue", linestyle="-", label="等额本金月本金")
plt.plot(periods_list, ACPI_interest_per_month_list, color="red", linestyle=":", label="等额本息月利息")
plt.plot(periods_list, ACPI_capital_per_month_list, color="red", linestyle="-", label="等额本息月本金")
plt.legend(loc='upper center', frameon=False)
plt.xlabel('期数 [月]')
plt.ylabel('金额 [元]')
plt.title('月还款本金 vs 利息')
```

[](label="cosine")
