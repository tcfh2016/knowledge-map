编写一个方法，将字符串中的空格全部替换为“%20”。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。

示例：
  - 输入：“Mr John Smith”
  - 输出：“Mr%20John%20Smith”

## 1 借助新的字符串转存

这里使用string类来进行操作，目的是学习使用C++的库函数，效率不会高到哪里去。

```
std::string replaceBlankChars(std::string &str)
{
	std::string res;
	std::string targetReplaceString("%20");

	for (std::string::iterator it = str.begin(); it != str.end(); ++it)
	{
		if (*it == ' ')
		{
			res += targetReplaceString;			
		}
		else
		{
			res.push_back(*it);
		}
	}

	return res;
}
```

## 2 字符串上直接操作

这种方式需要给定限制条件，即整个字符串的长度足够容纳替换之后的字符串，那么可以先计算原字
符串中空格的多少，从而计算出替换之后的总长度，最后再从后往前替换。

```
void replaceBlankChars(char *str, int length, int capacity)
{
	int blankCount = 0;
	for (int i = 0; i < length; ++i)
	{
		if (str[i] == ' ')
		{
			++blankCount;
		}					
	}

	int replacedStringLength = length + 2 * blankCount;
	if (replacedStringLength > capacity)
	{
		return;
	}

	for (int i = replacedStringLength - 1, j = length - 1; (i >= 0) && (j >= 0); --j)
	{
		if (str[j] == ' ')
		{
			str[i--] = '0';
			str[i--] = '2';
			str[i--] = '%';
		}
		else
		{
			str[i--] = str[j];
		}
	}
	str[replacedStringLength] = '\0';
}
```
