#include <iostream>
#include <stack>

class Solution {
public:
    bool match(char left, char right) {
        std::cout <<"compare " <<left << right <<std::endl;
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

    bool isValid(std::string s) {
        if (s.size() == 0) {
            return false;
        }

        std::stack<char> c;
        for (auto e : s) {
            if (e == '(' or e == '[' or e == '{') {
                c.push(e);
            }else {
                auto p = c.top();
                if (not match(p, e)) {
                    std::cout <<"not match" <<std::endl;
                    return false;
                }
                c.pop();
            }
        }
        return true;
    }
};

int main() {
  Solution s;
  std::cout <<s.isValid("()") <<std::endl;
}
