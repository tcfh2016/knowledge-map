## 气象站的需求

建立一个应用，利用`WeatherData`对象取得数据，并更新三个布告板：目前状况、气象统计和天气预报。

最简单的实现便是为三个布告板单独定义类并且创建各自的对象来完成数据的更新，我们称之为耦合版本:

![](coupling_design.png)

耦合版本针对具体实现进行编程，对于之后的新的需求不甚友好，比如我们需要增加或者删除布告板的时候必须改动`WeatherData`。为此我们可以对“WeatherData对外部的依赖解耦”，将其依赖的`ConditionDisplay`、`StatisticsDisplay`和`ForecastDisplay`抽离出来让`WeatherData`仅仅依赖其三者的抽象类型/接口，这样便不再受之后增删新的布告板的影响。

![](observer_design.png)

其实，如上的设计里面可以仅仅让`Subject`单向依赖于`Observer`，只不过这样`Observer`不管是在将自己添加进观察者列表还是从中移除都需要“第三方”来完成。
