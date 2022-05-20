## 给消息分组

最常用的关键字是`alt/else`表示分支判断，另外还有：

```
opt
loop
par
break
critical
group
```

## 不同形状的参与者

除了使用关键字`participant`之外，还可以使用下面这些关键字来定义不同类型/样式的参与者：

```
actor
boundary
control
entity
database
collections
queue
```

如果我们需要给某个参与者上点颜色，那么就直接将颜色写在后面，比如`actor ME #99FF99`。


## 调整序列实体显示顺序

正常情况下，plantuml会按照解析脚本的顺序生成对应的 participant，比如如下脚本的解析结果
里 A, B, C和D等按照出现的顺序排列：

```
@startuml

A -> B
B -> C
A -> D

@enduml
```

![](display_diagram_in_order.png)

如果我们想要事先固定显示顺序，比如让D 显示在 A后面，那么我们可以在脚本开始的时候定义participant，这样就可以固定它的显示顺序了。

```
@startuml

participant A
participant D
participant B
participant C

A -> B
B -> C
A -> D

@enduml
```

![](display_diagram_in_specified_order.png)

当然，还可以使用`order`关键字来调整参与者的顺序。

参考：

- [Sequence Diagram](https://plantuml.com/sequence-diagram)
