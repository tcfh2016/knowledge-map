给定两个字符串，请编写程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

## 1 先排序，再比较是否相同

```
bool checkIfStringSameAfterRestructure(std::string &str1, std::string &str2)
{
	std::sort(str1.begin(), str1.end());
	std::sort(str2.begin(), str2.end());

	return str1 == str2;
}
```

## 2 散列的方式

这种方法实际上也就是统计字符串中各个字符的出现次数，再比较结果。

```
void countString(std::string &str, std::map<std::string::value_type, int> &count_map)
{
	for (std::string::iterator it = str.begin(); it != str.end(); ++it)
	{
		std::map < std::string::value_type, int>::iterator pos = count_map.find(*it);
		if (pos == count_map.end())
		{
			count_map.insert(std::map <std::string::value_type, int>::value_type(*it, 1));
		}
		else
		{
			pos->second++;
		}
	}
}

bool checkIfStringSameAfterRestructure(std::string &str1, std::string &str2)
{
	std::map<std::string::value_type, int> str1_count_map;
	std::map<std::string::value_type, int> str2_count_map;

	countString(str1, str1_count_map);
	countString(str2, str2_count_map);

	return str1_count_map == str2_count_map;
}
```

这种方式还有一种更轻便的实现方式：

```
if (str1.length() != str2.length())
{
  return false;
}

static const int MAX_CHAR_NUMBER = 256;
int counter[MAX_CHAR_NUMBER] = { 0 };

for (std::string::size_type i = 0; i < str1.length(); ++i)
{
  counter[str1[i]] ++;
}

for (std::string::size_type i = 0; i < str2.length(); ++i)
{
  counter[str2[i]] --;
}

for (std::string::size_type i = 0; i < MAX_CHAR_NUMBER; ++i)
{
  if (counter[i] != 0)
    return false;
}
return true;
```
