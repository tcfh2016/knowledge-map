编写一个算法，若MxN矩阵中某个元素为0，则将其所在的行与列清零。

遍历每个元素，看是否为0，如果为0就清空对应的行和列，同时需要避免对已经清零的行或列进行检测。

```
void zeroMatrixRowAndColumn(int matrix[ROW_NUM][COLUMN_NUM], int rows = ROW_NUM, int cols = COLUMN_NUM)
{
	std::set<int> zeroedRow;
	std::set<int> zeroedCol;

	for (int i = 0; i < rows; ++i)
	{
		for (int j = 0; j < cols; ++j)
		{
			if ((matrix[i][j] == 0) && (zeroedRow.find(i) == zeroedRow.end()) && (zeroedCol.find(j) == zeroedCol.end()))
			{
				zeroedRow.insert(i);
				zeroedCol.insert(j);

				clearRowAndColumn(matrix, i, j);
			}
		}
	}
}
```
