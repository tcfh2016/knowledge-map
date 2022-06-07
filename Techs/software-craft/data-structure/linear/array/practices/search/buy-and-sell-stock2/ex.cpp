#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_trade_day = 0;
        auto max_profit = singleMaxTrade(prices, 0, prices.size() - 1, max_trade_day);
        std::cout <<"out loop" <<max_trade_day;
        while (max_trade_day < prices.size() - 1) {
            max_profit += singleMaxTrade(prices, max_trade_day + 1, prices.size() - 1, max_trade_day);
            std::cout <<"in loop" <<max_trade_day;
        }
        return max_profit;
    }

    int singleMaxTrade(vector<int>& prices, int begin, int end, int& day) {
      if (begin >= end) {
        day = prices.size() - 1;
        return 0;
      }
        auto max_profit = 0;
        auto min_price = prices[begin];
        for (auto i = begin + 1; i < end; ++i) {
            if (min_price > prices[i]) {
                min_price = prices[i];
            }
            if (max_profit < prices[i] - min_price) {
                max_profit = prices[i] - min_price;
                day = i;
            }
        }
        return max_profit;
    }
};

int main() {
  Solution s;
  std::vector<int> v{7,1,5,3,6,4};
  std::cout <<s.maxProfit(v);

  return 0;
}
