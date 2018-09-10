实现一个算法，确定一个字符串的所有字符是否全部不同。假使不允许使用额外的数据结构，又该如何处理？

## 1 散列方式

这个问题很明显的解法是通过散列表的方式为每个字符创建一个标记位，只需要扫描一遍字符串，便可以得到结果。时间复杂度O(N)，即对数级别。

然而，字符有不同的编码格式，因此需要进一步限制问题，如下实现方式是假定ASCII码的编码方式。

```
bool isAllCharUnique(const char *str, int length)
{
  const int MAX_ARRAY_LENGTH = 256;
  if (length > 256)
  {
    return false;
  }

  static char letter_check_flags[MAX_ARRAY_LENGTH] = {'n'};

  for (int i = 0; i < length; ++i)
  {
    int index = static_cast<int>(str[i]);
    if (letter_check_flags[str[i]] == 'y')
    {
      return false;
    }

    letter_check_flags[str[i]] = 'y';
  }
  return true;
}
```

优化空间：

- 使用位图，减少标记位的存储空间。

## 2 暴力比较

使用双层循环将每一个字符以此与其他字符进行比较，时间复杂度为O（N^2），即平方级别。

```
bool isAllCharUnique(const char *str, int length)
{
  for (int i = 0; i < length; ++i)
  {
    for (int j = i + 1; j <length; ++j)
    {
      if (str[i] == str[j])
      {
        return false;
      }
    }
  }
  rturn true;
}
```

## 3 借助排序

先对数组进行排序，然后依次检查相邻的字符是否重复。如下使用STL进行实现。

```

```
