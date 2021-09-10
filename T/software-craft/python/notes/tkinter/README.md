
Tkinter 是使用 python 进行窗口视窗设计的模块。具有简单、跨平台的特性。

# 问题列表

## 1. 为什么使用 messagebox 的时候会弹出另外一个窗口？

Tkinter 必须拥有一个主窗口，尽管你不创建它也会自动创建。此时的处理有两种，一是直接创建
主窗口，并在上面布置你要显示的信息；另一种做法是隐藏它：

```
window = tkinter.Tk()
window.withdraw()
tkinter.messagebox.showinfo(title='',message='')#提示信息对话窗
```

# 参考

- [Tkinter messagebox without window?](https://stackoverflow.com/questions/17280637/tkinter-messagebox-without-window)
- [TkInter message box](https://pythonspot.com/tk-message-box/)
