# react

`react`是一个让开发网站变得更简单的三方库。它可用于电脑和手机段的开发。

- `react.js`公共库
- `react-dom.js`专用与电脑端网站的js库

其他常用的库：

- `JSX`，JavaScript XML，是一种 在 JavaScript 中写 HTML-like 代码的语法扩展
- `Babel`，一个编译器，用来将一些新特性（比如JSX）转换为javascript，让浏览器可以展现出来
- `DayJS`更好的处理时间

使用`react`帮助更容易开发网站的几个方面：

- 使用`function`可以定义可重用的组件，通过它可以自定义html标签，并像传统html标签那样使用。这样将网站切分为更小的组件来组织会更容易。
- 在`function`里面可以通过`props`以字典形式来传递所有参数。
- `react`可以自动更新页面。


# shortcut

- `<input />`是`<input></input>`的简写，JSX有着比html更严格的语法规定，在html里面可以直接写`<input>`，但JSX必须要有结束元素标记`/<intput>`。
- `ChatInput`是一个定义好的函数，`{ChatInput()}`和`<ChatInput></ChatInput>`是等同的，前者是javascript的语法，后者是react里面的组件语法，它类似使用自定义的html标签。
- `<div>`可以用来将多个元素分组。使用`react`可以直接用`<></>`（fragment）来进行分段。
    - `div`会增加DOM层级，性能更差一点。同时语义上更清晰，fragment表示逻辑上的分组，不适视觉结构上的容器。
    - `div`是一种block element，它会单独占用一整行，也就是不会和其他元素并列在同一行。它经常会在布局的时候使用。
- `const message = props.message;`等同于`const {message} = props;`。
- `//`用来注释代码。
- `...`是spread opeartor，把数组里面的元素拷贝到新的数组里面。
- 使用`const [text, setText] = React.useState("")`来让`text`这个变量具有在变化的时候重新刷新页面的能力，注意其中的`setText`并不是变量，而是函数。


## 函数参数

```
function Chat(props) {
    const message = props.message;
    const sender = props.sender;
    ...
}

function Chat(props) {
    const { message, sender } = props;
    ...
}

function Chat({ message, sender }) {
    ...
}
```