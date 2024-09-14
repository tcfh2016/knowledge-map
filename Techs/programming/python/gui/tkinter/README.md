
Python有不少的GUI框架，但只有`Tkinter`是内置在Python标准库当中的，它使用所运行的操作系统来渲染可视化组件，具有简单、跨平台的特性。

当然，`Tkinter`看起来有点过时，不够绚丽。所以，在选用具体的框架的时候，可以根据项目的特性选择对应的框架。


# 问题列表

## 1. 为什么使用 messagebox 的时候会弹出另外一个窗口？

Tkinter 必须拥有一个主窗口，尽管你不创建它也会自动创建。此时的处理有两种，一是直接创建
主窗口，并在上面布置你要显示的信息；另一种做法是隐藏它：

```
window = tkinter.Tk()
window.withdraw()
tkinter.messagebox.showinfo(title='',message='')#提示信息对话窗
```

## APP开发方法论

第一步：设计

- 明确APP需要哪些控件
- 控件的布局


## 参考

- [Tkinter messagebox without window?](https://stackoverflow.com/questions/17280637/tkinter-messagebox-without-window)
- [TkInter message box](https://pythonspot.com/tk-message-box/)
- [Python GUI Programming With Tkinter](https://realpython.com/python-gui-tkinter/)