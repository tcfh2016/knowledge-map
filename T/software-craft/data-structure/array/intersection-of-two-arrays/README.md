## 两个数组的交集

给定两个数组，编写一个函数来计算它们的交集。


示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]

## 解法

1）直观的两重遍历

```
vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    set<int> uniqNum;

    for (size_t i = 0; i < nums1.size(); ++i) {
        for (size_t j = 0; j < nums2.size(); ++j) {
            if (nums1[i] == nums2[j]) {
                uniqNum.insert(nums1[i]);
            }
        }
    }

    vector<int> answer;
    for (auto e : uniqNum) {
        answer.push_back(e);
    }
    return answer;
}
```

2）另一种更高效的是使用hashtable/map

```
vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> uniq;
    for (size_t i = 0; i < nums1.size(); ++i) {
        if (uniq.count(nums1[i]) == 0) {
            uniq[nums1[i]] = 1;
        }
    }

    vector<int> answer;
    for (size_t i = 0; i < nums2.size(); ++i) {
        if (uniq[nums2[i]] > 0) {
            answer.push_back(nums2[i]);
            uniq[nums2[i]] = 0;
        }
    }

    return answer;
}    
```
