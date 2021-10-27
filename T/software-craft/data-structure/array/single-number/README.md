## 只出现一次的数字

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4


## 解法

1）最直观的解法就是用map，保存并计数，但这需要两次遍历，并且使用了额外空间。不管怎样，先搞个简单版本出来：

```
int singleNumber(vector<int>& nums) {
    map<int, int> m;
    for (auto i = 0; i < nums.size(); ++i){
        if (m.count(nums[i]) == 0) {
            m[nums[i]] = 1;
        }
        else {
            ++m[nums[i]];
        }
    }
    for (auto& e : m) {
        if (e.second == 1) {
            return e.first;
        }
    }
    return 0;
}
```

2）最好的方法是使用亦或的运算

```
int singleNumber(vector<int>& nums) {
    int r = 0;    
    for (auto i = 0; i < nums.size(); ++i){
        r ^= nums[i];
    }
    return r;
}
```
