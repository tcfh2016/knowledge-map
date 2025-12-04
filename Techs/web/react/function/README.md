# 函数

函数参数

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

# 箭头函数

这种函数是一种简化的写法。比如下面的代码当键入`Enter`的时候发送消息，完整的写法如下：

```
function pressEnter(event)
{
    if (event.key === 'Enter') sendMessage();
}

<input 
    placeholder="Send a message to Chatbot" 
    size="30"
    onChange={saveInputText}
    onKeyDown={pressEnter}
    value={inputText}
/>
```

而更简单的写法就是使用箭头函数：

```
<input
    placeholder="Send a message to Chatbot" 
    size="30"
    onChange={saveInputText}
    onKeyDown={(e) => { if (e.key === 'Enter') sendMessage(); }}
    value={inputText}
/>
```
