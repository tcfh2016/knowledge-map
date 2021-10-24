## 两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

## 解体思路

- 暴力法，效率较低。
- 排序，根据头尾逐步缩小范围进行尝试。但这样会变动下标。
- 使用map来存储，讲效率提升至O(N)。


```
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (auto i = 0; i < nums.size(); ++i) {
            for (auto j = i + 1; j < nums.size(); ++j) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};
```

```
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> accessed_elem;
        for (auto i = 0; i < nums.size(); ++i) {
            auto r = accessed_elem.find(target - nums[i]);
            if (r == accessed_elem.end()) {
                accessed_elem.insert(std::pair(nums[i], i));
            } else {
                return {i, r->second};
            }
        }
        return {};
    }
};
```
