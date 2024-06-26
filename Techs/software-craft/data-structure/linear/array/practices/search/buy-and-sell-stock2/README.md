## 买卖股票的最佳时机

给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


## 解法

1）这个一时也想不出来简单直白的方法。暴力的解法只为了能够遭到一个最优解，但是现在看起来需要多个。稍微思考之后发现，在遍历到某个节点的时候能够确认出最大的利润的那笔交易，而多笔交易要达到最大其实只需要在剩下的天数里面继续寻找最大的交易，有这么一个递归的过程。

尝试之后发现不对。

看了提示之后才发现没那么复杂，只需要购买每一次上升趋势就行了。

```
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        auto max_profit = 0;
        for (auto i = 0; i < prices.size() - 1; ++i) {
            int t = prices[i + 1] - prices[i];
            if (t > 0) {
                max_profit += t;
            }
        }
        return max_profit;
    }
};
```
