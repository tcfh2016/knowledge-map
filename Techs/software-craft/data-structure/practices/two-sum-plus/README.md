## 两数之和

给定一个已按照 非递减顺序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

## 解法

1）这个不同于前面一道两数之和的地方在于给定的是有序数组，这样就更方便了，因为可以通过同时进行前后遍历在找到对应的结果。

```
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int begin = 0;
        int end = numbers.size() - 1;
        while (begin < end) {
            if (numbers[begin] + numbers[end] > target) {
                --end;
            }
            else if (numbers[begin] + numbers[end] < target) {
                ++begin;
            }
            else {
                return {begin+1, end+1};
            }
        }
        return {0, 0};
    }
};
```
