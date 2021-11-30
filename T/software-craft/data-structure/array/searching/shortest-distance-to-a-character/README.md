## 字符的最短距离

给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

示例 1:

输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

## 解法

这个看起来最直接的方法就是逐个遍历，然后每次遍历的时候去计算距离：

```
int findShortestPos(string& s, int start, char c) {
      for (int i = start, j = start; i < s.length() || j >= 0; ++i, --j) {
          if (i < s.length() and s[i] == c) {
                  return i - start;
          }

          if (j >= 0 and s[j] == c) {
              return start - j;
          }
      }
      return 0;
  }

  vector<int> shortestToChar(string s, char c) {
      vector<int> answer;
      for (size_t i = 0; i < s.length(); ++i) {
          answer.push_back(findShortestPos(s, i, c));
      }
      return answer;
  }
```

另外一种方法，是两次遍历，然后比较两次遍历的距离即可。
