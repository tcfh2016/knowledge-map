## 旋转

旋转通常可以分为左旋和右旋，右旋为顺时针，左旋为逆时针，算法都类似。以下以左旋进行距离，针对包含n个元素的数组arr[]左旋d个元素的效果如下：

```
1 2 3 4 5 6 7 // 旋转前
3 4 5 6 7 1 2 // 旋转后
```


### 方法一：多次移动

这是最直接的办法，就是效率低。对于简单的测试用例可以通过，但是对于大量的数据则会超时。

```
while (d-- > 0) {
  auto tmp = arr[0];
  for (auto j = 1; j < n; ++j) {
    arr[j - 1] = arr[j];
  }
  arr[n - 1] = tmp;
}
```

这种方法有一个改进，也就是将“每一轮移动将所有元素往左走一步”改进为“每一轮移动将特定的元素一次性走d步”，这样的移动将会更加高效。不过这里“特定的元素”需要将所有元素进行分组的处理，这一点理解出来不是很直观，先不展开。


### 方法二：少次移动

可以很明显的发现，如上的移动操作实在太浪费了，旋转元素d个必须进行d轮了数组移动。一个小优化是计算好偏移量，只进行一轮的数组移动。

```
for (auto i = 0; i < n; ++i) {
  arr[i] = arr[(i + d) % n];
}
```

上面这个算法看起来正确，实际上是错误的，因为数组的开头元素已经被覆盖，后面通过模运算索引到的元素已经被改写。所以，可以将前面d个元素提前保存下来：

```
int new_arr[d] = {};
for (auto i = 0; i < d; ++i) {
  new_arr[i] = arr[i];
}

for (auto i = 0; i < n; ++i) {
  if (i + d > n - 1) {
    arr[i] = new_arr[(i + d) % n];
  }
  else {
    arr[i] = arr[i + d];
  }  
}
```


### 方法三：块交换/block swap

这种方法完全不同于前面讨论的直观移动，它通过递归来完成。


### 方法四：反转算法

假设AB是数组的两部分，A = arr[0..d-1]，B = arr[d..n-1]，算法的过程为：

- 反转A得到Ar，那么AB变为ArB
- 反转B得到Br，那么ArB变为ArBr
- 整体反转，那么ArBr变为BA

```
void rotate(int arr[], int start, int end) {
    for ( ;start < end; ++start, --end) {
        std::swap(arr[start], arr[end]);
    }
}

void leftRotate(int arr[], int n, int d) {
    rotate(arr, 0, d - 1);
    rotate(arr, d, n - 1);
    rotate(arr, 0, n - 1);
}
```
