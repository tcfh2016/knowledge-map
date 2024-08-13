## 基本元素

最基本的Tkinter GUI元素是窗口（`window`），它是一个可以用来容纳其他GUI元素的容器，比如text box, label, button这些被称为空间（`widget`）的元素。

## 创建第一个GUI应用

第一个应用必须要简单，比如首先创建一个窗口，窗口是一个`Tk`对象：

```
import tkinter as tk

window = tk.Tk()
```

执行上面的代码并不会有窗口出现，你还必须添加一句`window.mainloop()`，这句代码的意思是启动“事件循环”，以便窗口可以监听事件。

## 添加一个控件

使用`tk.Label`类来添加文本标签，先创建实例，再将其装进窗口中：

```
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
```

当有空间安装到窗口之后，窗口的大小会自动适配到空间的大小。

