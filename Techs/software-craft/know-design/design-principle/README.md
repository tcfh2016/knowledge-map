## 面向对象设计原则

1）封装变化

如果每次新的需求都会使某方面的代码发生变化，那么就可以确定这部分代码需要和其他稳定的代码区分，可以单独抽离。换句话说就是，把会变化的部分取出并封装起来，以便以后可以轻易地改动或扩充此部分，而不影响不需要变化的其他部分。

2）针对接口编程，而不是针对实现编程

针对实现编程的一个例子是子类实现父类/超类里面定义的所有接口，子类必须知道所有的细节。这将导致子类经常为了新的需求而需要修改，这是一种绑定于实现的耦合关系。

当我们将子类里面这些行为独立成一组单独的类，子类里面使用这组新类提供的接口，那么子类不需要再关心这些具体的实现，用接口就行了。这就是针对“接口编程”。

```
// 针对实现编程
Dog d = new Dog();
d.bark()

// 针对接口编程
Animal animal = new Dog(); // 可以动态指定，比如 animal = getAnimal()
animal.makeSound();
```

3）多用组合，少用继承

继承的好处在于可以最大化的复用代码，但却因为这种继承实现的紧耦合关系扩展性不好，即如果需要修改方法那么需要修改子类的实现，或者修改了父类的方法会影响所有的子类。而组合可以将一些变化较大的部分独立出来，减少了对于原有继承体系的影响。

4）为了交互对象之间的松耦合设计而努力

松耦合的设计之所以能让我们建立有弹性的OO系统，能够应对变化，是因为对象之间的互相依赖降到了最低。

5）类应该对扩展开放，对修改关闭。

开放-关闭原则的目标是允许类容易扩展，在不修改现有代码的情况下，就可搭配新的行为。这样的设计具有弹性可以应对改变，可以接受新的功能来应对改变的需求。

*注：开放-关闭原则通常会引入新的抽象层增加代码复杂度，所以每个地方都采用开放-关闭原则是一种浪费，也没有必要。你需要依照自身经验对设计中最有可能改变的地方应用该原则。*

6）依赖倒置原则

要依赖抽象，不要依赖具体类。

7）“最少知识”原则

减少对象之间的交互，只留下几个“蜜友”。这个原则是希望在设计中不要让太多的类耦合在一起，免得修改系统的一部分会影响到其他部分。如果太多类相互依赖，那么这个系统就会变成一个复杂的、难以维护的系统。

8）好莱坞原则

别调用（打电话给）我们，我们会调用（打电话给）你。