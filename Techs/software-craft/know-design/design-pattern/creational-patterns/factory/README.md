## 工厂模式

工厂模式针对的是初始化的耦合问题。初学者往往会误认为工厂模式直接让初始化的工作消失不见，这只是一个误解。工厂模式的真正含义是将初始化的工作进行一定程度的封装，让这部分可能在将来会变化的工作独立出来，从而限制往后扩展可能影响的范围。应用工厂模式后，以前必须要修改主体代码，现在只需要修改抽离出来的这部分代码即可。

当然，工厂模式有多种变化类型，比如简单工厂模式、抽象工厂模式和工厂方法模式这三种类型。


## [简单工厂](./simple_factory/README.md)

简单工厂的思想很简单，它创建一个单独的对象来负责创建不同的实例，这些实例同属于相同的继承体系。对用户而言它是一个主要的服务组件（它就是工厂），用户不涉及到创建实例的工作。


## [工厂方法](./factory_method/README.md)

简单工厂把全部的事情在一个地方都处理完了，然而工厂方法却是创建了一个框架，让子类决定要如何实现。简单来说，工厂方法模式是对简单工厂的进一步的抽象，使其能够多维化简单工厂，更具有扩展性。


## [抽象工厂](./abstract_factory/README.md)

相对于工厂方法创建单个产品而言，抽象工厂是创建一个产品家族，也就是创建多个产品。需要注意的是工厂方法一次创建单个产品，而抽象工厂是一次创建多个产品。因此，在实现上工厂方法每次创建一个新产品都是继承框架，而抽象工厂也是继承框架，但是每次继承则意味着创建了多个产品。