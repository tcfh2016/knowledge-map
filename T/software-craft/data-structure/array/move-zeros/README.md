## 移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。


## 解法

1）最直观的解法就是遍历的时候发现是0就进行移动，但这种移动很难处理连续多个0的情况。

2）另一种就是先遍历一次，记录所有0和非0的索引，然后先将非0的写入前面，后面的全部写0。

```
void moveZeroes(vector<int>& nums) {
    vector<int> nonZeroIndex;        
    for (size_t i = 0; i < nums.size(); ++i) {
        if (nums[i] != 0) {
            nonZeroIndex.push_back(i);
        }
    }
    for (size_t i = 0; i < nonZeroIndex.size(); ++i) {
        nums[i] = nums[nonZeroIndex[i]];
    }
    for (size_t j = nonZeroIndex.size(); j < nums.size(); ++j) {
        nums[j] = 0;
    }
}
```

3) 但是题目的要求是不能拷贝额外的数组，所以需要更换思路，使用双指针来进行，一个指向值为0的元素，另一个指向值为非0的元素。

```
void moveZeroes(vector<int>& nums) {
    size_t zeroPos = 0;
    size_t read = 0;

    while (read < nums.size()) {
        if (nums[read] != 0) {
            nums[zeroPos] = nums[read];
            ++zeroPos;
        }
        ++read;
    }
    while (zeroPos < nums.size()) {
        nums[zeroPos++] = 0;
    }
```
