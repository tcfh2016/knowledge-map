## `.bind()`

使用`.bind()`来将事件和事件处理器绑定起来，既可以将事件处理器绑在窗口上，也可以绑在任何一种控件上：

```
window.bind("<event_name>", event_handler)
button.bind("<Button-1>", handle_click)
```

参考：


- [Python GUI Programming With Tkinter](https://realpython.com/python-gui-tkinter/)
- [Tkinter 8.5 reference: a GUI for Python](https://web.archive.org/web/20190512164300/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/event-types.html)

## `command`

每个`Button`都有一个`command`属性用来绑定处理函数，当按下`Button`的时候对应的处理函数就会被调用，比如下面的处理就是将函数`decrease()`绑定到按钮`btn_decrease`上：

```
btn_decrease = tk.Button(master=window, text="-", command=decrease)
```