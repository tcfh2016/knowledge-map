## 线性回归

- 监督学习：每个例子都有一个“正确答案”
- 线性回归：预测具体数值的输出
- 训练集：包含有输入和输出的数据集合

## 监督学习

通过向“学习算法”提供“训练集”，然后输出一个“函数”，这个函数能够完成原始训练集中的数据转换。

## 模型假设

怎么样去得到这个“函数”？首先尝试最简单的线性函数是一个不错的开始。而这种尝试就被称为“线性回归”。最简单的就是“单变量线性回归”：

$h_{\theta}(x)=\theta_{0}+\theta_{1} x$

## 模型求解

怎么求解出上面模型中的a和b，以便能够更好地拟合训练集中的数据 ?

在线性回归中需要解决的是一个最小化的问题，也就是求解 $ \frac{1}{2 m} \sum_{i=1}^{m}\left(h_{\theta}\left(x^{(i)}\right)-y^{(i)}\right)^{2}$ 的最小值。 这个函数也称为“代价函数（cost function）”，也被称为“平方误差函数”。这个最小值成为“优化目标”。

要求取代价函数的最小值，从模拟的角度便是给 ${\theta_{0}}, {\theta_{1}}$ 分别指定一个数值范围，然后不断的尝试，直到找到最佳的值使得代价函数可以得到最小值，这个时候就算求解了假设函数。

## 梯度下降算法（Gradient Descent）

基本步骤：

- 开始时随机选择一个参数的组合 $ ({\theta_{0}}, {\theta_{1}},...,{\theta_{n}}) $，计算代价函数
- 然后寻找下一个能让代价函数值下降最多的参数组合
- 持续这么做直到抵达一个局部最小值（local minimum）

理解上述过程的一个例子是站在群山中的某个高点，持续往视线范围内的最低点走过去，直到下山。

该算法有个特点，那就是选择不同的初始参数组合，可能会找到不同的局部最小值。由于并没有尝试完所有的参数组合，所以不能确定得到的局部最小值是否便是全局最小值（global minimum）。

梯度下降算法的公式：

$ {\theta_{1}} := {\theta_{1}} - {\alpha} \frac{d}{{d}\theta_{1}} J(\theta_{1})$

其中的${\alpha}$表示学习率，也就是每次移动幅度的大小。

- 如果${\alpha}$太小，可能会很慢，因为它会一点点挪动，它会需要很多步才能到达全局最低点。
- 如果${\alpha}$太大，梯度下降法可能会一次次越过最低点，直到离最低点越来越远，最终会导致无法收敛，甚至发散。

求解之后，梯度下降算法为：

$ {\theta_{0}} := {\theta_{0}} - {\alpha} \frac{1}{{m}} \sum_{i=1}^{m} \left(h_{\theta}\left(x^{(i)}\right)-y^{(i)}\right) $

$ {\theta_{1}} := {\theta_{1}} - {\alpha} \frac{1}{{m}} \sum_{i=1}^{m} \left(h_{\theta}\left(x^{(i)}\right)-y^{(i)}\right)·x^{(i)} $

以上这种梯度算法也称为“批量梯度下降算法”，因为它每次的训练都使用了所以样本的数据。