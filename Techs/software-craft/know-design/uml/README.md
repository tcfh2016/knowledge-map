## UML分类

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
