# [python-beginner-projects](https://github.com/Mrinank-Bhowmick/python-beginner-projects)

游戏类。

## Battleship

最基本的战舰游戏，随机的布置一个战舰位置，然后用户去猜测位置对不对。相当于扫雷游戏的简化版，不过是用命令行来玩。

有两个版本，一个简单点，一个复杂点。`battleship_v2`的代码写得很正式，可以学习。

## BFS visualizer

在执行程序的时候提示“ModuleNotFoundError: No module named '_curses'”，以为是没有安装好`curses`，使用`pip install curses`重新安装又提示：

```
ERROR: Could not find a version that satisfies the requirement curses (from versions: none)
ERROR: No matching distribution found for curses
```

之后搜索之下发现是Linux和Windows下面版本的差异，执行`pip install windows-curses`安装成功并解决问题。

参考：

- [ImportError: No module named '_curses' when trying to import blessings](https://stackoverflow.com/questions/35850362/importerror-no-module-named-curses-when-trying-to-import-blessings)