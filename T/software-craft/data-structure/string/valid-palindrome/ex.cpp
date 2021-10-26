#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        if (s.size() <= 1) {
            return true;
        }

        int begin = 0;
        int end = s.size() - 1;

        while (begin < end) {
            if ((!isDigit(s[begin])) and (!isLetter(s[begin]))) {
                ++begin;
                continue;
            }

            if ((!isDigit(s[end])) and (!isLetter(s[end]))) {
                --end;
                continue;
            }

            if (isDigit(s[begin]) && (s[begin] != s[end])) {
                std::cout <<"return false in digit judgement" <<begin <<" "<<end <<endl;
                return false;
            }
            if ((s[begin] - 'a' != s[end] - 'a') && (s[begin] - 'A' != s[end] - 'a')) {
                std::cout <<"return false in letter judgement" <<begin <<" "<<end <<endl;
                return false;
            }
            ++begin;
            --end;
        }
        return true;
    }

    bool isDigit(char c) {
        return (c >= '0' && c <= '9');
    }
    bool isLetter(char c) {
        return (c >= 'A' && c <= 'Z') or (c >= 'a' && c <= 'z');
    }
};

int main() {
  string str("A man, a plan, a canal: Panama");
  Solution s;
  s.isPalindrome(str);

  return 0;
}
