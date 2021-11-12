## 两整数之和

不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1

## 解法

需要使用到位的运算，两个关键的思考点：

- 亦或可以看成是不带进位的加法
- 进位可以看成是与运算之后进位

这道题目从递归的角度去解会更容易，从中可以很方便的思考到当有进位、没有进位时候的停止条件。比如当没有进位的时候那么我们得到的就是`a^b`的值，当有进位且其他位为0的时候我们得到的是`(a^b) << 1`的值，而其他的情况是继续两者结果的相加运算。

```
int getSum(int a, int b) {
    if (a == 0) {
        return b;
    }
    if (b == 0) {
        return a;
    }

    return getSum(a^b, (unsigned int)(a & b) << 1);   
}
```

而迭代的版本看起来就费解多了：

```
int getSum(int a, int b) {
    if (a == 0) {
        return b;
    }
    if (b == 0) {
        return a;
    }
    
    while (b != 0) {
        auto carry = (unsigned int) (a & b) << 1;
        a = a ^ b;
        b = carry;
    }
    return a;
}
```
