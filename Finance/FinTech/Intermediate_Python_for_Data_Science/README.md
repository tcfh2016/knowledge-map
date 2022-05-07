## [Intermediate Python for Data Science](https://campus.datacamp.com/courses/intermediate-python-for-data-science/)

### 1.Matplotlib

- Basic Plots with Matplotlib

使用matplotlib画线，本地测试无法找到该模块，因此使用 `pip3 install matplotlib`先安装。

line plot适用于有着递增规律的序列，基本用法为：

```
import matplotlib.pyplot as plt
plt.plot(year, pop)
plt.show()
```

对于无序的序列来说，使用线性图就会显得杂乱无章， 此时可以使用离散图：

```
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') #将x轴坐标值变更为指数规模
plt.show()
```

离散图标的大小可以通过其中的`s`参数来设定。

- histogram（直方图，柱状图）

在画直方图的时候参数"bin"用来指定将数据划分为多少份，Python默认为10。

```
plt.hist(life_exp)
plt.show()
plt.clf() #清空，刷新
```

[How to choose bins in matplotlib histogram](https://stackoverflow.com/questions/33458566/how-to-choose-bins-in-matplotlib-histogram)

- Customization

|函数|功能|
|-|-|
|xlabel|添加x轴描述|
|ylabel|添加y轴描述|
|title|添加标题|
|xticks|替换坐标显示单位|

```
# 设置size, color, alpha
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

plt.text(1550, 71, 'India') #添加文本
plt.text(5700, 80, 'China')
plt.grid(True) #网格样式

plt.show()
```

好吧，学习到这里要收费了。
