
## 归一化与对数化

这一对概念是在第10周周记里面学习@Gyro的[价值低波（中）-- 市盈率研究](https://www.joinquant.com/view/community/detail/328831058b45f5f1080914aaea6e0d09)碰到的概念，在第11周里面进行了较详细的了解。

**归一化**

归一化（英文`Normalization`），意思是将一些事物变得更加正常化或者常规化。但这是一个很宽泛的概念，它在不同的领域有不同的更加细致的含义，常见的应用领域包括科学、数学和统计、计算机科学与技术。我们这里使用到的，或者更具体些，上周学习的@Gyro在[价值低波（中）-- 市盈率研究](https://www.joinquant.com/view/community/detail/328831058b45f5f1080914aaea6e0d09)提到的“归一化”使用的是统计学中的归一化。

归一化是将数据集映射到指定的范围，通常是[0,1]和[-1,1]，用于除去不同维度数据的量纲。最常见的是“Min-Max 归一化”，公式为：(X - Xmin)/(Xmax - Xmin)。@Gyro里面应该就是类似这个思路，之所以说“类似”是因为里面归一化的时候仅仅是取了数据集中第一个记录来作为归一化的分母，但消除量纲的目的还是可以达到的。

参考：

- [Normalization](https://en.wikipedia.org/wiki/Normalization)
- [ML 入门：归一化、标准化和正则化](https://www.davex.pw/2017/10/07/Normalization-and-Regularization/)
- [归一化与标准化](https://ssjcoding.github.io/2019/03/27/normalization-and-standardization/)
- [数据特征的标准化和归一化你了解多少？](http://www.raincent.com/content-10-12066-1.html)

**对数化**

对数化（英文`Logarithm Transformation`），是数据转换众多方式中的一种，而数据转换的目的是为了将数据转换成一种更容易理解的形式以便于进一步的分析。总的来说，对数化的主要作用是它能够大幅缩小数据的绝对值，但是不会改变数据之间的相互关系，所以数据能够更加平稳。这样我们肉眼看看着比较方便，更重要的做得专业点是可以对这些平稳的数据进行回归的，回归就是找到数据的函数，也就是规律了。

如果这样理解，我们在上周周记里面提到的肉眼去看对数化之后的走势发现没有规律还不够严谨，更严谨的做法是尝试对那些对数化之后的数据尝试进行回归看是否找得到回归函数，但这目前超过了我的学习范围，先放放。

- [Data transformation (statistics)](https://en.wikipedia.org/wiki/Data_transformation_(statistics))
- [数据取对数的意义](https://www.cnblogs.com/zztt/p/3409675.html)
