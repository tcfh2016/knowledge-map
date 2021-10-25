## 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

## 解法


1）直观的解法

```
class Solution {
public:
    bool match(char left, char right) {
        if (left == '(') {
            if (right == ')') {
                return true;
            }
            return false;
        }

        if (left == '[') {
            if (right == ']') {
                return true;
            }
            return false;
        }

        if (left == '{') {
            if (right == '}') {
                return true;
            }
            return false;
        }

        return false;
    }
    bool isValid(string s) {
        if (s.size() == 0) {
            return false;
        }

        stack<char> c;
        for (auto e : s) {
            if (e == '(' or e == '[' or e == '{') {
                c.push(e);
            }
            else if (c.empty()){
                return false;
            }
            else {
                auto p = c.top();
                if (not match(p, e)) {
                    return false;
                }
                c.pop();                
            }
        }
        if (c.empty()) {
            return true;
        }
        return false;
    }
};
```

2）更有效率的解法

如上的解法可以优化的有两个地方:

- `match()`函数的实现有些复杂，可以优化
- 使用了`stack`，可以直接使用当前的字符串来标记

```
class Solution {
public:
    bool isValid(string s) {
        int top = -1;
        for(int i =0;i<s.length();++i){
            if(top<0 || !isMatch(s[top], s[i])){
                ++top;
                s[top] = s[i];
            }else{
                --top;
            }
        }
        return top == -1;
    }
    bool isMatch(char c1, char c2){
        if(c1 == '(' && c2 == ')') return true;
        if(c1 == '[' && c2 == ']') return true;
        if(c1 == '{' && c2 == '}') return true;
        return false;
    }
};
```
