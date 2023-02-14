2015年1月12日16:17:45
svn add  ./C_Test/me.txt     // 添加单个文件
svn add  ./C_Test                 // 添加整个目录

svn add  * ./C_Test               // 添加整个目录，略去已经处于控制当中的文件

今天执行了上面这个命令，把一些不用添加的文件执行了添加，如何删除？

$ svn add mistake.txt whoops
A mistake.txt
A whoops
A whoops/oopsie.c

$ svn revert mistake.txt whoops
Reverted mistake.txt
Reverted whoops

$ svn status
? mistake.txt
? whoops

这里再补充一点，执行svn revert的时候如果需要对子目录进行生效需要加上参数"--depth=infinity"。
2015年1月12日17:14:00

 



2015年4月17日09:33:27
今天想到去深究之前的一个问题，不过在svn上面的记录已经是许久之前了。所以想通过一种方法查看到当时谁修改了，修改了哪些文件，差别是什么。

查找到的第一个方法为：
在命令行下面执行 svn log -r no，在GUI界面下面没有看到。


2016年10月25日19:44:16

svn checkout http://svn.example.com/svn/repo/trunk

// 更新到当前。
svn update
// 撤销修改。
svn revert filename
svn revert -R pathname

svn update -r 406829