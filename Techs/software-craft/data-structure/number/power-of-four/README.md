## 4 的幂

给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？


## 解法

1）最简单的办法就是循环除

```
bool isPowerOfFour(int n) {
    if (n == 0) {
        return false;
    }

    while (n % 4 == 0) {
        n = n / 4;
    }
    if (n == 1) {
        return true;
    }
    return false;
}
```

2）其他的办法就是数论中的内容了，略过。
