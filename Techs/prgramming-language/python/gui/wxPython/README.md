## 安装

Python对应GUI工具库主要有`Tkinter`, `wxPython`和`PyQt`。`wxPython`是1998年基于C++库`wxWidgets`开发而来，它相比其他两者最大的不同是它尽可能使用本地系统提供的图形组件，所以不管是在Windows, macOS, 还是 Linux，`wxPython`创建的GUI都和系统本身的窗体非常接近。

相比之前`Tkinter`和`PyQt`则是自己去画GUI组件，所以看起来和运行系统本身差别会大一点。

```
pip install -U wxPython

# 测试是否安装成功
import wx
print (wx.version())
```

## 组件/Widgets

- Main window
- Menu
- Toolbar
- Buttons
- Text Entry
- Labels

## 事件循环 / Event Loops

GUI需要响应用户的行为，因此它会有一个事件循环时时刻刻监听用户的行为。用户的行为被定义为“事件”，与之对应的还有“事件处理”。

一个wxPython程序至少包括两个对象：

1. 应用程序对象`wx.App()`，会调用`MainLoop()`来启动事件循环。
2. 窗体对象`wx.Frame()`，创建窗体本身。


注：使用Jupyter Notebook调试wxPython程序的时候可能出现`wx.App object must be created first!`，一种方法是在程序的`MainLoop`的后面添加`del app`。参考[这里的讨论](https://github.com/wxWidgets/Phoenix/issues/556)。

## 开发

为了能够加速wxPython的界面开发，可以使用GUI设计工具来设计界面，减少编写代码的工作量。常见的GUI工具有`WxGlade`, `WxFormBuilder`和`Boa-constructor`。


## 参考

- [wxPython Downloads](https://wxpython.org/pages/downloads/)
- [How to Build a Python GUI Application With wxPython](https://realpython.com/python-gui-with-wxpython/)