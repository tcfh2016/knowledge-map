# numpy简介

`NumPy`是一个免费的、如同Matlab一样功能强大的数值计算开发平台，用C语言实现，提供了高性能的数组对象。`NumPy`这个词由“Numerical”和“Python”两个单词结合。

提供的功能：

- 强大的N维数组对象`ndarray`
- 广播功能函数
- 线性代数、傅立叶变换、随机数生成、图形操作等功能
- 整合C/C++/Fortran代码的工具


## 存储

使用`np.savetxt('out.txt', data)`来将数组写入文件，默认以科学表示法形式保存，可以通过`np.loadtxt('out.txt')`直接读取文件。


## np.right_shift

