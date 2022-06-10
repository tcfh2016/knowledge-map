利用字符重复出现的次数，编写一个方法，实现基本的字符串压缩功能。比如，字符串“aabcccccaaa” 会变为"a2b1c5a3"。若“压缩”后的字符串没有变短，则返回原先的字符串。

只需要直接统计相邻的重复值即可。

```
std::string compressString(std::string &str)
{
	if (str.empty())
	{
		return str;
	}

	std::string ret;
	std::string::iterator start_index = str.begin();
	int count = 0;

	ret.push_back(*str.begin());
	for (std::string::iterator it = str.begin(); it != str.end(); ++it)
	{
		if (*it == *start_index)
		{
			count++;
		}
		else
		{
			ret.push_back('0' + count);

			ret.push_back(*it);
			start_index = it;
			count = 1;
		}
	}
	ret.push_back('0' + count);

	if (str.length() == ret.length())
	{
		return str;
	}
	else
	{
		return ret;
	}
}
```
