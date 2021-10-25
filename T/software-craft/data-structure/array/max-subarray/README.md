## 最大子序列和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

## 解法

1）常规解法，两层遍历，会超时

```
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max = nums[0];

        for (auto i = 0; i < nums.size(); ++i) {
            int sum = 0;
            for (auto j = i; j <nums.size(); ++j) {
                sum += nums[j];
                if (sum > max) {
                    max = sum;
                }
            }
        }
        return max;
    }
};
```

2）代码最简单的是动态规划的方法，但是这种方法需要思考状态转移方程

```
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = nums[0];
        int curr_max = nums[0];

        for (auto i = 1; i < nums.size(); ++i) {            
            curr_max = max(curr_max + nums[i], nums[i]);
            max_sum = max(max_sum, curr_max);
        }
        return max_sum;
    }
};
```
