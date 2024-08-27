# [python-beginner-projects](https://github.com/Mrinank-Bhowmick/python-beginner-projects)

算法类。

## BFS visualizer

使用`curses`模拟广度优先搜索算法，`curses`这个库提供了独立于终端的屏幕绘制和键盘处理功能。

在执行程序的时候提示“ModuleNotFoundError: No module named '_curses'”，以为是没有安装好`curses`，使用`pip install curses`重新安装又提示：

```
ERROR: Could not find a version that satisfies the requirement curses (from versions: none)
ERROR: No matching distribution found for curses
```

之后搜索之下发现是Linux和Windows下面版本的差异，执行`pip install windows-curses`安装成功并解决问题。

参考：

- [ImportError: No module named '_curses' when trying to import blessings](https://stackoverflow.com/questions/35850362/importerror-no-module-named-curses-when-trying-to-import-blessings)
- [用 Python 进行 Curses 编程](https://docs.python.org/zh-cn/3/howto/curses.html)

## Bigram_Autocomplete

实现了一个简单的自动补全算法：

- 语料库的清洗
    - 去除标点
    - 整理为单词列表
- 补全算法
    - 根据给定的单词去语料库里面匹配
    - 将每一个匹配单词后面一个单词位置记录下来，并计数
    - 最后搜索计数，选择最佳匹配项
