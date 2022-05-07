## 模拟行走机器人

机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：

-2：向左转 90 度
-1：向右转 90 度
1 <= x <= 9：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物。

第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])

如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。

返回从原点到机器人的最大欧式距离的平方。


示例 1：

输入: commands = [4,-1,3], obstacles = []
输出: 25
解释: 机器人将会到达 (3, 4)

## 解法

这道题目初看起来还以为和图有关系，但仔细对照例子确认后，其实就是求XY的距离，然后求取平方和。这里有两个犯错的地方：1，弄错题目的意思，是求过程中的最大值；2，在找寻障碍的时候别企图跳跃性的运用公式去判断，而是直接逐个“当前位置+1”去判断。

```
void goStraight(string& direction, int steps, int& x, int& y, set<int>& obstaclesX, set<int>& obstaclesY) {
bool isBlocked = false;

if (direction == "north") {
    while (steps-- and obstaclesY.count(y + 1) == 0) {
        y += 1;
    }
}
else if (direction == "south") {
    while (steps-- and obstaclesY.count(y - 1) == 0) {
        y -= 1;
    }         
}
else if (direction == "west") {
    while (steps-- and obstaclesX.count( x - 1) == 0) {
        x -= 1;
    }   
}
else if (direction == "east") {
    while (steps-- and obstaclesX.count( x + 1) == 0) {
        x += 1;
    }   
}
else {
    //invalid
}
}

void calcDirection(int command, string& direction) {
if (direction == "north") {
    if (command == -2) {
        direction = "west";
    }
    else {
        direction = "east";
    }
}
else if (direction == "south") {
    if (command == -2) {
        direction = "east";
    }
    else {
        direction = "west";
    }
}
else if (direction == "west") {
    if (command == -1) {
        direction = "north";
    }
    else {
        direction = "south";
    }
}
else if (direction == "east") {
    if (command == -2) {
        direction = "north";
    }
    else {
        direction = "south";
    }
}
else {
    // invalid
}
//cout <<direction <<endl;
}

int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {        
int x = 0;
int y = 0;
int answer = 0;
string direction = "north";
unordered_map<int, set<int>> obstaclesInXpath;
unordered_map<int, set<int>> obstaclesInYpath;

for (auto& v : obstacles) {
    obstaclesInYpath[v[0]].insert(v[1]);
    obstaclesInXpath[v[1]].insert(v[0]);
}

for (auto c : commands) {            
    if (c < 0) {
        calcDirection(c, direction);                
    }
    else {                
        goStraight(direction, c, x, y, obstaclesInXpath[y], obstaclesInYpath[x]);
        answer = max(answer, x*x + y*y);
    }
}

return answer;
}
```
