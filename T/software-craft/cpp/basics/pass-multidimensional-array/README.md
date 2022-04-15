同事在编写UT的时候突然提到如何实现将同行不同列的二维数组传递给函数。最初的时候简单聊了三
种方式：

- 直接传入行和列；
- 将二维数组封装为单个数据结构进行传递；
- 使用模板。

后来想了想，后面两种方法过于大费周折，其实直接传入行和列来解决。

```
void print2DArray(int array[][3], int rows, int cols)
{
	for (int i = 0; i < rows; ++i)
	{
		for (int j = 0; j < cols; ++j)
		{
			std::cout << array[i * cols + j] << ' ';
		}
		std::cout << std::endl;
	}
}
```

这种方式行不通，因为二维数组作为参数的时候必须要指定列的大小。然而，我们可以通过比较tricky
的方式，即通过将二维数组按照一维数组寻址的方式来达到目的：

```
void print2DArray(int *array, int rows, int cols)
{
	for (int i = 0; i < rows; ++i)
	{
		for (int j = 0; j < cols; ++j)
		{
			std::cout << array[i*rows + j] << ' ';
		}
		std::cout << std::endl;
	}
}
```

对于模板这种方式，最直接的思路是通过为函数定义非类型参数来实现，然而，除了将二维数组作为
指针的形式进行传递之外，单独指定非类型参数没有办法做到。
