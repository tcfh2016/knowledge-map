
# 关联

把实体（类）之间连接起来的线被称为关联：

- 所有的关联都具有名字，名字都是动词或者动词短语。
- 关联的两段用`0..*`表示多重性，小三角图标指向两个实体之间关联组成句子的谓语。

关联都被认为是双向的，除非其上带有一个箭头，箭头的出现把知识限制在箭头所指的方向。双向关
联允许两个实体互相知晓。

关联是两个类之间的一种关系，这种关系允许从这两个类创建的实例之间会存在链接。关联最常见的
实现方式为：一个类中的实例变量指向或者引用到另外一个类。

在关联中增加箭头可以限制关联的导航性。当带有一个箭头时，关联就只能够朝着箭头的方向前进。
这意味着箭头指向的类不知道它的关联者。

# 聚合

聚合是一种特殊形式的关联，意味着“整体/部分”关系。它被表示为聚集类上一个白色菱形，和白色
菱形相邻的类是整体，另外一个类是部分。

# 组合

组合是一种特殊形式的聚合，意味着“整体”负责它的“部分”的生存期。它被表示为一个黑色菱形。

# UML分类

UML2.0 相比 UML1.0新增了4副图，达到13副图。

### 一、结构建模

- class diagram: discribe the static structure of a system.

- object diagram: describe the static structure of a system at a particular time.
They can be used to test class diagrams for accuracy.

- package diagram: a subset of class diagrams, it organize elements of a system
into related groups to minimize dependencies between packages.

- deployment diagram: depict the physical resources in a system, including nodes, components, and connections.

- component diagram: describe the organization of physical software componenets,
including source code, run-time (binary) code, and executables.

- composite structure diagram: show the internal part of a class.

### 二、行为/交互建模

- user case diagram: model the functionality of a system using actors and use cases.

- activity diagram: illustrate the dynamic nature of a system by modeling the flow of control from activity to activity. An activity represents an operation on some class in the system that results in a change in the state of the system. Typically, activity diagrams are used to model workflow or business processes and internal operation.

- sequence diagrame: describe interactions among classes in terms of an exchanges of message over time.

- state diagram: describe the dynamic behavior of a system in response to external
stimuli.

- communication diagram: model the interactions between objects in sequence.

- interaction overview diagram: a combination of activity and sequence diagrams.

- timing diagram: a type of behavioral or interation UML diagram that focuses on
processes that take place during a specific period of time. They're a special
instance of a sequence diagram, except time is shown to increase from left to
right instead of top and down.
