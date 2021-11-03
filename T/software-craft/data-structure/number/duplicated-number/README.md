## 存在重复元素 II

给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true


## 解法

1）最简单的解法就是两次遍历，但这种解法会超时

```
bool containsNearbyDuplicate(vector<int>& nums, int k) {
        for (size_t i = 0; i < nums.size(); ++i) {
            for (size_t j = i+1; j < nums.size(); ++j) {
                if (nums[i] == nums[j]) {
                    if (j - i <= k) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
```

2）另一种就是将索引和值对应存储到map里面，这样只需要遍历一遍就可以。但需要考虑多于两个的重复情况。

```
bool containsNearbyDuplicate(vector<int>& nums, int k) {
    map<int, int> answer;
    for (size_t i = 0; i < nums.size(); ++i) {
        if (answer.count(nums[i]) == 0 || (i - answer[nums[i]] > k)) {
            answer[nums[i]] = i;
            continue;
        }

        if (i - answer[nums[i]] <= k) {
            return true;
        }
    }

    return false;
}
```
