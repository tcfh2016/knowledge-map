## jupyter

Jupyter Notebook，是在浏览器中操作的一种基于对话模式的程序执行环境，它是一款除了支持Python语言，还可以支持Julia和Ruby等多种语言的开源软件。

参考：

- [Jupyter Home](https://jupyter.org/)

## 魔法命令

魔法命令可以理解为一条可将Jupyter Notebook的功能进行扩展的捷径，只需在命令的前面加上“%”，执行即可。执行魔法命令会因为IPython的版本及操作系统等的不同而有所不同。

- `%time`命令确认代码的执行速度
- `%%time`可以对整个单元的处理时间进行测量
- `%timeit`测量行潜入的处理时间
- `%%timeit`测量单元的处理时间
- `%matplotlib inline`实现将inline参数传递给“%matplotlib”，并将绘制的图表显示在Jupyter Notebook的单元中
- `%whos`对所有变量一览表进行显示