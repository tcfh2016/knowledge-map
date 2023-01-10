## 类图


## 类与类的关系

扩展 <|--
组合 *--
聚合 o--

--直线。
..虚线（垂直方向）。
. 虚线（水平方向）。
<|三角形。
*实心菱形。
o空心菱形。

```
@startuml
Class01 <|-- Class02
Class03 *-- Class04
Class05 o-- Class06
Class07 .. Class08
Class09 -- Class10
@enduml
```


## 关系标签

:置于末尾添加关系标签。
""置于关系符两端表示基数关系。
<同时使用:和 <或者>来表示对象关系。

```
@startuml
Class01 "1" *-- "many" Class02 : contains
Class03 o-- Class04 : aggregation
Class05 --> "1" Class06
@enduml
```


## 添加方法

:置于类名后添加成员。
{}类似类的定义，将成员包括起来。

```
@startuml
Object <|-- ArrayList
Object : equals()
ArrayList : Object[] elementData
ArrayList : size()
@enduml
```

## 定义可见性

-private
#protected
~package private
+public

```
@startuml
skinparam classAttributeIconSize 0
class Dummy {
 -field1
 #field2
 ~method1()
 +method2()
}
@enduml
```


## 抽象和静态属性

{static}定义静态成员。
{abstract}定义抽象方法。

```
@startuml
class Dummy {
  {static} String id
  {abstract} void methods()
}
@enduml
```


## 注释和stereotypes

class << >> Stereotypes.note 
left/right/top/bottom of在类的左右上下添加注释。

```
@startuml
class Object << general >>
Object <|--- ArrayList

note top of Object : In java, every class\nextends this one.

note "This is a floating note" as N1
note "This note is connected\nto several objects." as N2
Object .. N2
N2 .. ArrayList

class Foo
note left: On last defined class

@enduml
```