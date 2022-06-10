## 加1

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

## 解法

1）最直接的解法就是用新的内存来存放运算产生的结果，完全模拟加法运算的过程

```
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> sum;
        int flag = 1;

        for (int i = digits.size() - 1; i >= 0; --i) {
            auto t = digits[i] + flag;
            if (t == 10) {                
                sum.push_back(0);
                flag = 1;
            }
            else {
                sum.push_back(t);
                flag = 0;
            }
        }
        if (flag == 1) {
            sum.push_back(1);
        }

        vector<int> res;
        for (auto iter = sum.rbegin(); iter != sum.rend(); ++iter) {
            res.push_back(*iter);
        }

        return res;
    }
```

2）另外一种解法是直接在原来数组上进行修改

```
int carry = 1;
for (int i = digits.size() - 1; i >= 0; --i) {
    carry += digits[i];
    digits[i] = carry % 10;
    carry = carry / 10;
}
if (carry == 1) {
    digits.insert(digits.begin(), carry);
}
return digits;
```
