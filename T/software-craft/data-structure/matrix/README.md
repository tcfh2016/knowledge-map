## 矩阵

## 旋转

比如逆时针旋转90度，对于立方矩阵的旋转比较简单，使用双层循环可以搞定。算法虽然简单，但是在实现的时候需要比较细致的处理索引，主要是处在四个方向的元素的索引：

```
// Consider all squares one by one
for (int x = 0; x < N / 2; x++) {
    // Consider elements in group
    // of 4 in current square
    for (int y = x; y < N - x - 1; y++) {
        // Store current cell in
        // temp variable
        int temp = mat[x][y];

        // Move values from right to top
        mat[x][y] = mat[y][N - 1 - x];

        // Move values from bottom to right
        mat[y][N - 1 - x]
            = mat[N - 1 - x][N - 1 - y];

        // Move values from left to bottom
        mat[N - 1 - x][N - 1 - y]
            = mat[N - 1 - y][x];

        // Assign temp to left
        mat[N - 1 - y][x] = temp;
    }
}
```

另外一种方式是先反转每行，再运用矩阵的转置，不是很明白这种方式。

```
void rotateMatrix(int mat[][N])
{
  //REVERSE every row
  for(int i=0;i<N;i++)
    reverse(mat[i],mat[i]+N);

  // Performing Transpose
  for(int i=0;i<N;i++)
  { for(int j=i;j<N;j++)
      swap(mat[i][j],mat[j][i]);
  }
}
```
