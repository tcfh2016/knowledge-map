用C或C++实现void reverse(char * str)函数，即反转一个null结尾的字符串。

## 1 新的字符串转存

创建一个新的字符串，从后往前读取源字符串并拷贝至新的字符串中。

```
void reverse(char *str)
{
  int str_len = strlen(str);
	char *target_str = new char[str_len + 1];

	for (int i = str_len - 1, j = 0; i >= 0; --i, ++j)
	{
		target_str[j] = str[i];
	}
	target_str[str_len] = '\0';

	memcpy(str, target_str, str_len + 1);
}
```

## 2 直接转存

直接操作源字符串，首尾逐个对调。如果不允许使用库函数，那么可以通过收尾指针的方式完成。

```
void reverse(char *str)
{
  int str_len = strlen(str);


	int head_index = 0;
	int tail_index = str_len - 1;

	for (; head_index < tail_index; ++head_index, --tail_index)
	{
		str[str_len] = str[head_index];
		str[head_index] = str[tail_index];
		str[tail_index] = str[str_len];
	}
	str[str_len] = '\0';
}
```
