# 使用

## 创建组件

使用`add_***`来创建不同的组件，返回对应的tag：

```
b0 = dpg.add_button(label="button 0")
b1 = dpg.add_button(tag=100, label="Button 1")
```

## 创建分组

```
with dpg.group():
    dpg.add_button(label="Button 3")
    dpg.add_button(label="Button 4")
    with dpg.group() as group1:
        pass
```

## 配置、状态

- get_item_configuration -> label, callback, width, height
    - get_item_label
- get_item_state -> visible, hovered, clicked, etc
    - is_item_hovered
- get_item_info -> item type, children, theme, etc
    - get_item_children

## 回调函数

可以使用`set_item_callback(sender, app_data, user_data)`来设置回调函数：

```
def button_callback(sender, app_data, user_data):
    ...

# 创建组件的时候设置回调和用户数据
dpg.add_button(label="Apply", callback=button_callback, user_data="Some Data")

# 其他时候设置回调和用户数据
btn = dpg.add_button(label="Apply 2", )
dpg.set_item_callback(btn, button_callback)
dpg.set_item_user_data(btn, "Some Extra User Data")
```

## 组件的值

可以通过`get_value()`和`set_value()`来获取和设置组件的值：

```
# 获取
def print_value(sender):
    print(dpg.get_value(sender))

input_txt1 = dpg.add_input_text()
dpg.set_item_callback(input_txt1, print_value)

# 设置
dpg.set_value("slider_int", 40)
```

## 使用`item handler`

对于一些文本框并不能直接绑定回调函数，这个时候可以用`item handler`来绑定回调：

```
with dpg.window(width=500, height=300):
    dpg.add_text("Click me with any mouse button", tag="text item")
    with dpg.item_handler_registry(tag="widget handler") as handler:
        dpg.add_item_clicked_handler(callback=change_text)
    dpg.bind_item_handler_registry("text item", "widget handler")
```

# Staging

stage用来创建一些需要结构化组织的组件。


参考：

- [Staging](https://dearpygui.readthedocs.io/en/latest/documentation/staging.html)


# Child

组件仅仅能够作为容器的子组件。一个容器将不同类型的子组件存储在不同的slot里面：

- Slot 0: mvFileExtension, mvFontRangeHint, mvNodeLink, mvAnnotation, mvDragLine, mvDragRect, mvDragPoint, mvLegend, mvTableColumn
- Slot 1: Most items
- Slot 2: Draw items
- Slot 3: mvDragPayload


参考：

- [Container Slots & Children](https://dearpygui.readthedocs.io/en/latest/documentation/container-slots.html?highlight=get_item_children)