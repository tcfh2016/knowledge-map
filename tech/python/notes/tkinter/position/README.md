# 控件位置

## 使用 pack()

在一个窗口上创建一个按钮，其默认按照上、下、左、右的方式排列：

```
window = tkinter.Tk()
window.title('CI 状态')
window.geometry('200x200')

button = tkinter.Button(window, text='知道了', width=15, height=2, command=hit_button)
button.pack()
```

可以在调用 pack()的时候传入不同的参数（`top`, `bottom`, `left`, `right`）来指定其摆放
位置。

## 使用 grid

grid 是以表格的形式了布置位置，row为行，colum为列，padx就是单元格左右间距，pady就是单元
格上下间距。

```
 tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)
```

## 使用 pace

指示部件的坐标位置，坐标的锚点有不同的位置。

```
tk.Label(window, text=1).place(x=20, y=10, anchor='nw')
```

# 参考

- [tkinter Python3](https://morvanzhou.github.io/tutorials/python-basic/tkinter/)
