## 二进制手表

二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。

例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

## 解法

这道题目一看就是遍历所有可能就行了，因为小时和分钟的范围都给定了，用两层遍历，再加一层个数的判断。

```
int countBit1(int num) {
        auto cnt = 0;
        while (num != 0) {
            if (num % 2 != 0) {
                ++cnt;
            }
            num /= 2;
        }
        return cnt;
    }
    vector<string> readBinaryWatch(int turnedOn) {
        vector<string> answer;
        for (auto i = 0; i < 12; ++i) {
            for (auto j = 0; j < 60; ++j) {
                if (countBit1(i) + countBit1(j) == turnedOn) {
                    string str = "";
                    str += (std::to_string(i) + ":");
                    if (j < 10) {
                        str += "0";
                    }
                    str += std::to_string(j);
                    answer.push_back(str);
                }
            }
        }
        return answer;
    }
```
