## Removing Duplicates

首先要知道哪些行重复了，使用`duplicated()`，这个函数会返回一个Series，也就是对每行是否为重复行的Boolean数组。

删除重复行直接调用`df.drop_duplicates(inplace = True)`即可。
