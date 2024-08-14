## 几何管理器

TKinter可以用`pack()`、`.place()`和`.grid()`来进行布局管理，每个window或者Frame只能够使用一种几何管理器，但不同的Frame可以使用不同的方式。

## `pack()`

`pack()`的布置算法很简单，对于要布置的对象算出一个刚好容纳该对象矩形区域（专业名词：`parcel`），然后默认居中显示。

- `fill`，指定填充的方向，水平为`tk.X`，垂直为`tk.Y`，或者`tk.BOTH`。
- `side`，`tk.TOP`,`tk.BOTTOM`,`tk.LEFT`,`tk.RIGHT`。
- `expand`，设置为Ture，在调整窗口大小的时候会自动扩展。

## `pack()`
