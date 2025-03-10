## 丑数

编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:

输入: 6
输出: true
解释: 6 = 2 × 3


## 解法

1）直观的解法就是直接遍历去除，然后判断因子是否存在于{2，3，5}里，但这样还需要过滤是否因子为质数，因为都与质数的判断有关，那其实可以直接记录该数字的所有质数，然后判断是否只有2，3，5即可。这样还是不行，还是需要逐步整除。

```
bool isUgly(int n) {
    if (n == 0) {
        return false;
    }
    while (n % 2 == 0) {
        n /= 2;
    }
    while (n % 3 == 0) {
        n /= 3;
    }
    while (n % 5 == 0) {
        n /= 5;
    }

    return n == 1;
}
```
