## 打家劫舍

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

## 解法

1）典型的动态规划题目，每次都不是很熟悉，确实有点不好做，但看了提示之后又觉得比较简单了。

```
int rob(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        if (nums.size() == 1) {
            return nums[0];
        }
        int first = nums[0];
        int second = max(first, nums[1]);

        for (size_t i = 2; i < nums.size(); ++i) {
            auto t = second;
            second = max(first + nums[i], second);
            first = t;
        }
        return second;
    }
```
