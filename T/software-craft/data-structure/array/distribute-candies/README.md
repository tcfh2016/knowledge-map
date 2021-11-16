## 分糖果

给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。

示例 1:

输入: candies = [1,1,2,2,3,3]
输出: 3
解析: 一共有三种种类的糖果，每一种都有两个。
     最优分配方案：妹妹获得[1,2,3],弟弟也获得[1,2,3]。这样使妹妹获得糖果的种类数最多。

## 解法

这道题目实际上就是找到n/2个元素中不同元素的最大个数，最简单的方法就是遍历一次，看不同种类糖果的个数有多少，超过n/2那么就取n/2，否则就去最大不同的种类即可。

```
int distributeCandies(vector<int>& candyType) {
  unordered_set<int> s;
  for (auto e : candyType) {
      if (s.count(e) == 0) {
          s.insert(e);
      }
  }

  return s.size() > candyType.size()/2 ? candyType.size()/2 : s.size();
}
```
