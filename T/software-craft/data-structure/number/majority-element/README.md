## 多数元素

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。



示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

## 解法

1）最直接的解法就是用一个map来计数，最后找到最大的那个元素。

```
int majorityElement(vector<int>& nums) {
        map<int, int> cnt;
        for (auto e:nums) {
            if (cnt.count(e) > 0) {
                ++cnt[e];
            }
            else {
                cnt[e] = 1;
            }
        }

        for (auto e:cnt) {
            if (e.second > nums.size()/2) {
                return e.first;
            }
        }
        return -1;
    }
```

2）另外一种解法是先排序，然后选择中间的元素

3）还有一种最高效的是所谓的“投票算法”，也就是不断消除不同元素，剩下的就是要找到的元素。

```
int answer = 0;
int cnt = 0;
for (auto e : nums) {
    if (e == answer) {
        ++cnt;
    }
    else if (cnt > 0) {
        --cnt;
    }
    else {
        answer = e;
        cnt = 1;
    }
}
return answer;
```
