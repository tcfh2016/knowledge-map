## 七进制数

给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"

## 解法

觉得很简单的一道题目，差点不知道原理是啥，看了提示后才清晰。

```
string toBase7(uint num) {
    string answer;

    while (num > 0) {
        auto a = num % 7;
        answer += '0' + a;
        num = num / 7;
    }
    if (num != 0)
        answer += num + '0';

    return {answer.rbegin(), answer.rend()};
}

string convertToBase7(int num) {
    if (num == 0) {
        return "0";
    }

    string answer;
    if (num < 0) {
        return "-" + toBase7(-num);
    }

    return toBase7(num);
}
```
