## 删除排序数组中的重复项

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

## 解法

1）暴力法，需要使用额外的空间来记录。

2）不使用额外的空间，真要实现起来需要预先熟悉。

```
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
      if (nums.size() == 0) {
        return 0;
      }

      size_t slow = fast = 0;
      while (fast < nums.size()) {
        if (nums[slow] == nums[fast]) {
          ++fast;
        }
        else {
          ++slow;
          nums[slow] = nums[fast];
          ++fast;
        }
      }
      return slow + 1;
    }
};
```
