# 模块包

Python代码的目录就称为包，这类导入称为包导入。包导入是把计算机上的目录变成另一个Python命名空间，而属性则对应于目录所包含的子目录和模块文件。

- 一个文件夹必须包含一个`__init__.py`，才能被定义为包，执行文件导入工作。
- 一个文件夹必须包含一个`__main__.py`，这个包才能够被执行：`py -m folder_name`。

## 包导入基础

如下的语句表明了机器上有个目录dir1，而dir1里有子目录dir2，dir2内包含一个名为mod.py的模块文件。同时该导入意味着dir1位于某个容器目录dir0中，这个`dir0`目录可以在Python模块搜索路径中找到（或者它本身就是顶层文件的主目录）。

```
import dir1.dir2.mod
from dir1.dir2.mod import x
```

在使用包导入时，必须遵守一条约束：包导入语句的路径中每个目录内必须有__init__.py文件，否则包导入会失败。如上的代码目录结构解释如下：

- dir1和dir2中必须都包含一个__init__.py文件。__init__.py文件扮演了包初始化、替目录产生命名空间以及实现`from *`行为的角色：
  - Python首次导入某个目录时会自动执行该目录下__init__.py文件中所有程序的代码。
  - 脚本内的目录路径，在导入后会变成真实的嵌套对象路径。
  - 在__init__.py里使用__all__列表来定义目录以`from*`语句形式导入时导出的变量名。
- dir0时容器，不需要__init__.py文件，如果有的话，它也会被忽略。
  - 如果直接执行某个程序，__init__.py不会被调用。
- dir0必须列在模块搜索路径上（该目录是主目录，或者列在PYTHONPATH中）。

*注：import语句中的目录路径只能是以点号间隔的变量。*

## 包相对导入

包自身内部的导入称为相对导入，它们的语法与Python版本有关。

|语法|Python 2.6|Python 2.7|Python 3.0|
|-|-|-|-|
|常规导入语句|隐式地搜索包目录（相对搜索），再绝对搜索。|绝对搜索。|需要显示指定相对导入语法，默认执行绝对导入（绝对搜索）。|
|带.号的from语句|执行相对搜索。||执行相对搜索|
|improt语句|先相对再绝对。|绝对搜索。|先相对再绝对。|


```
from . improt spacm # 在Python3.0, 2.6中，均执行相对搜索。
from .. improt spacm # 导入当前包上层目录的spacm。
```

尽管绝对导入允许我们略过包模块，它们仍然依赖于sys.path上的其他部分，因此并不会略过当前工作目录（CWD），比如：

```
C:\test\pkg\spam.py
C:\test\pkg\eggs.py
C:\test\pkg\__init__.py
```

在spam.py里面使用import eggs语句不会成功，因为当前spam.py和eggs.py都处于同一个包内，会执行绝对搜索（不会看到pkg目录下的eggs.py），但如果工作目录在pkg下面是可以的。

- 测试1：在`c:\test`目录进入python命令行，执行`import pkg.spam`会提示错误。
- 测试2：在`c:\test\pkg`目录进入python命令行，执行`import spam`会正常工作。

# 高级模块话题
