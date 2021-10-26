## 合并两个有序数组

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

## 解法

这个题目看到的第一印象需要进行逆向遍历，并优先将最大的放到数组后方。否则，无法很好的完成元素的插入工作。

```
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int tail1 = m - 1;
        int tail2 = n - 1;
        int tail3 = m + n - 1;

        while (tail1 >=0 and tail2 >= 0) {
            if (nums1[tail1] > nums2[tail2]) {
                nums1[tail3] = nums1[tail1--];
            }
            else {
                nums1[tail3] = nums2[tail2--];
            }
            --tail3;
        }

        if (tail1 < 0) {
            while (tail2 >= 0) {
                nums1[tail3--] = nums2[tail2--];
            }
        }
    }
};
```
