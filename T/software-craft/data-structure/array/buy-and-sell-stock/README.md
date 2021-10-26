## 买卖股票的最佳时机

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。


## 解法

1）最简单直白的方式就是双重循环，首层选择为买入，第二层我卖出，逐步遍历取最大值。但这样会超出时间限制

```
int maxProfit(vector<int>& prices) {
    auto max_profit = 0;
    for (auto i = 0; i < prices.size(); ++i) {            
        for (auto j = i; j < prices.size(); ++j) {
            max_profit = max(max_profit, prices[j] - prices[i]);
        }
    }
    return max_profit;
}
```

2）那再进行思考，股票最高利润就是低买高卖，来个单次遍历。怎么思考呢？就是假如第i天是卖出的时候，那么在0...i-1天里面一定有个最小值，所以遍历的时候记录下最小值，且不断更新最大值。

```
int maxProfit(vector<int>& prices) {
        auto max_profit = 0;
        auto min_price = prices[0];
        for (auto i = 1; i < prices.size(); ++i) {            
            if (min_price > prices[i]) {
                min_price = prices[i];
            }
            max_profit = max(max_profit, prices[i] - min_price);
        }
        return max_profit;
    }
```
