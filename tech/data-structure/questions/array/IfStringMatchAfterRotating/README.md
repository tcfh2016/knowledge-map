假定有一个方法 isSubstring，可检查一个单词是否为其他字符串的子串。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成，要求只能调用一次isSubstring。（比如，waterbottle是erbottlewat旋转后的字符串。）

## 1 字符对比

最明显的一种方式是找到两个字符串相同的起始字符，然后以此为起点进行逐个字符对比。

```
bool MatchSameOrder(std::string targetStr, std::string sourceStr, int start)
{
	for (size_t i = 0; i < targetStr.length(); ++i)
	{
		if (targetStr[i] != sourceStr[(start + i)%sourceStr.length()])
		{
			return false;
		}
	}
	return true;
}

bool IsStringMatchAfterRotating(std::string &str1, std::string &str2)
{
	if (str1.length() != str2.length())
	{
		return false;
	}

	int str1StartIndex = 0;
	for (size_t i = 0; i < str2.length(); ++i)
	{
		if ((str2[i] == str1[0]) && (MatchSameOrder(str1, str2, i)))
		{
			return true;			
		}
	}

	return false;
}
```

## 2 使用数学推导的算法

但上面这种方式根本没有使用题目中给出的`isSubstring()`，其实这里有一种更加理性化的方式。
考虑一个字符串可以被任意分割为两部分，比如 x, y，那么：

- 原始字符串为source = xy，那么旋转之后为 target = yx。
- 那么题目的意思就是如何判断 source 与 target 之间的关系。
- 当我们将 source 或者 target重复时
  - source + source = xyxy = x + target + y
  - target + target = yxyx = y + source + x

所以这个算法就可以演变为判断下面任意一种：

- source 是否是 target + target 的子串。
- target 是否是 source + source 的子串。

```
bool IsStringMatchAfterRotating(std::string &str1, std::string &str2)
{
	if ((str1.length() == str2.length()) && (str1.length() != 0))
	{
		std::string temp = str1 + str1;
		return (NULL != temp.c_str(), str2.c_str());
	}
	return false;
}
```
