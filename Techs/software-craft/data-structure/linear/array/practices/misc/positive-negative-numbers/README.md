## 将非负整数和负整数交替排列

这里有两个要求：1）非负在偶数位上，负数在奇数位上；2）多余的偶数或者奇数都放到末尾。


## 解法

1）没有保持相对不变位置的要求

- 利用快速排序的方式将非负整数和负数分成两半，并记录各自的起始的位置
- 利用快慢索引，交换位置上的元素

2）有保持相对位置不变的要求

- 从左到右扫描数组
- 找到未处理元素里面第一个不满足条件的元素x，并找到该元素后面符号相反的第一个元素y（该元素y应该移动到x所在的位置上）
- 将[x, y]区间进行右移，可以在保证相对位置不变的情况下，调换x,y的位置


参考：

- [](https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/)