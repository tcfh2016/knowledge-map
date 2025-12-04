# CSS

`CSS`俗称层叠样式表，用来装饰网站的，而`CSS with React`就是在React里面正常的使用CSS。它写在`<style>`区：

```
<html>
<head>
    <title>BOT</title>
    <style>
        button {
            background-color:green;
        }
    </style>
</head>
<body>
...
</body>
</html>
```

上面的代码里：

- `button`是CSS Selector，决定哪些元素要化妆。如果要指定具体某个按钮，就需要为特定按钮定义`className`属性，然后用`.class_name`来作为CSS选择器
- 大括号里面就是具体怎么化妆：
    - `background-color`是CSS Property，代表具体化妆的部位
    - `green`是CSS Value，代表化什么


# CSS 属性

- 元素的内部空间为`padding`，`padding: 12px 20px;`代表垂直方向12像素，水平方向20像素的填充
- 元素的边缘空间为`margin`，可以分上下左右：`margin-left`
- 元素的边框为`boarder`
    - `border-radius`可以控制边框的角度
    - `border-width`可以控制边框的厚度
- 元素里面的文本大小`font-size`
- `cursor:pointer`可以让鼠标移动到元素的时候显示为手的形状

# 其他

- `class`是JavaScript里面的保留字，所以在React里面要用`className`来表示HTML里面的`class`，比如React里面的`<button className="send-button">`等同于HTML里面的`<button class="send-button">`。