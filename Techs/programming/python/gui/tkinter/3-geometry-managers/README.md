## 几何管理器

TKinter可以用`pack()`、`.place()`和`.grid()`来进行布局管理，每个window或者Frame只能够使用一种几何管理器，但不同的Frame可以使用不同的方式。

## `pack()`

`pack()`的布置算法很简单，对于要布置的对象算出一个刚好容纳该对象矩形区域（专业名词：`parcel`），然后默认居中显示。

- `fill`，指定填充的方向，水平为`tk.X`，垂直为`tk.Y`，或者`tk.BOTH`。
- `side`，`tk.TOP`,`tk.BOTTOM`,`tk.LEFT`,`tk.RIGHT`。不指定都是居中显示。
- `expand`，设置为Ture，在调整窗口大小的时候会自动扩展。
- `padx=5, pady=5`，给控件周围设置间距，`ipadx=5, ipady=5`给空间内部设置间距

控件的顺序和调用`pack()`的顺序有关。

## `place()`

使用`place(x, y)`能够更精确的指定控件的位置，这里的x和y都是以像素为单位，坐标轴以左上角为零点。

相比于`pack()`使用相对位置来布局，`place()`使用的是绝对位置，所以如果窗口尺寸变动的时候这些组件的位置也不会做对应的改变，这是不足之一；另外一点是如果组件很多的时候使用`plance()`来进行精确布局会变得复杂。

## `grid()`

`grid(row=i, column=j)`的布局是将整个window或Frame划分为行列形式的多个单元，然后通过行列的索引来布局。

各个单元之间的间隔可以进行填充，分“内部填充”和“外部填充”：

- internal padding：`ipadx=5, ipady=5`
- external padding: `padx=5, pady=5`

要让window能够在改变大小的时候进行自适应，需要通过`columnconfigure(index, weight, minsize)`和`rowconfigure()`来进行配置：

- index，行列的索引
- weight，默认为0，1为同步增长，2为双倍增长
- minsize，行高或者列宽的最小值

布局的空间如何展示在单元格里（默认居中），可以通过`sticky`参数来将控件往其他方向拉伸，取值为“n/N”, "e/E"，“s/S”和“w/W”，并且可以组合使用。

```
window.columnconfigure(i, weight=1, minsize=75)
window.rowconfigure(i, weight=1, minsize=50)

frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=i, column=j, padx=5, pady=5, sticky="n")
```


----

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
