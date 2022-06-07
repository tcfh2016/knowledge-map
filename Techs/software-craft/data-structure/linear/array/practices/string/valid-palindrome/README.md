## 验证回文串

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

## 解法

1）最直观的解法就是利用前后指针，思路直接，但是代码调试花了不少时间。尽量写得短小，效率越高。当然最好利用库函数。

```
bool isPalindrome(string s) {
        if (s.size() <= 1) {
            return true;
        }

        int begin = 0;
        int end = s.size() - 1;

        while (begin < end) {
            if (not needCheck(s[begin])) {
                ++begin;
                continue;
            }

            if (not needCheck(s[end])) {
                --end;
                continue;
            }

            if (isDigit(s[begin]) && (s[begin] != s[end])) {
                return false;
            }
            if (isBigLetter(s[begin]) && (s[begin] - 'A' != s[end] - 'a') && (s[begin] - 'A' != s[end] - 'A')) {
                return false;
            }
            if (isSmallLetter(s[begin]) && (s[begin] - 'a' != s[end] - 'a') && (s[begin] - 'a' != s[end] - 'A')) {
                return false;
            }

            ++begin;
            --end;
        }
        return true;
    }
    bool needCheck(char c) {
        if (isDigit(c) or isBigLetter(c) or isSmallLetter(c)) {
            return true;
        }
        return false;
    }

    bool isDigit(char c) {
        return (c >= '0' && c <= '9');
    }
    bool isBigLetter(char c) {
        return (c >= 'A' && c <= 'Z');
    }
    bool isSmallLetter(char c) {
        return (c >= 'a' && c <= 'z');
    }
```
