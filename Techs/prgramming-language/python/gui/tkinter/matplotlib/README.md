## 在`tkinter`上显示`matplotlib`图形

首先需要理解一点基本概念，`tkinter`和`matplotlib`是两个完全不相关的Python函数库。如果要将`matplotlib`所画的图形嵌入到`tkinter`上必须要有一些准备工作。

这些准备工作通常是由一种称为“后端（backend）”的组件来完成的，比如`matplotlib.backend`提供了不同的后端组件，而`backend_tkagg`便是用来在`tkinter`中嵌入图形使用的。

首先，导入画图必须的`Figure`对象；其次，从后端组件中导入用来承载图像的画布对象`FigureCanvasTkAgg`：

```
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
```

参考：

- [Using Tkinter and Matplotlib](https://ishantheperson.github.io/posts/tkinter-matplotlib/)
- [How to embed Matplotlib charts in Tkinter GUI?](https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/)