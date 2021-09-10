
## 如何统计搜索时匹配的个数

使用`:%s/pattern//ng`的时候会显示统计结果。

参考：

- [](https://vi.stackexchange.com/questions/93/is-there-a-way-to-count-the-number-of-occurrences-of-a-word-in-a-file)

## 在窗口打开其他文件

## 列编辑模式

在多行同时插入字符，可用于快速注释。在[酷壳](http://coolshell.cn/articles/5426.html)上有所谓的块操作。

第一步：Ctrl + v ，进入块操作模式
第二步：j,k或者Ctrl + d，在列上移动
第三步：I + 要插入的字符
第四步：Esc两下来使插入的生效

同理在删除的时候也类似，在使用jk进行行选择，使用h,l进行列选择然后d删除即可。


基本操作
Lenrn VIM Progressively
http://yannesposito.com/Scratch/en/blog/Learn-Vim-Progressively/

移动
1）行内移动
2）行间移动
gg/ [[                # 移动到文件开头
G/ shift+g / ]]  # 移动到文件尾, ]] 在{}之间跳转
: 或者 num+G  # 跳到某行
ggVG               # 全选
w 单词的行首
e 单词的行尾
0 行首
$ 行尾
^ 行首非空格
g_行尾非空格
fs 到下一个s地方
ts 到下一个s前的一个字符

ctrl+d               # 向下滚动半屏
ctrl+u               # 向上滚动半屏
ctrl+f                # 向下一屏
ctrl+b               # 向上一屏
ctrl + o             # 向后移动
ctrl + i              # 向前移动
H 屏幕最上方
L 屏幕最下方
M 屏幕中间  
n + <space> 右移动   
n + <enter> 下移动    


搜索 http://harttle.com/2016/08/08/vim-search-in-file.html
/name            # 往下查找
?name            # 向上查找
n                     # 下一个
N                    # 上一个    
*                     # 匹配下一个当前位置的单词, g*为部分匹配，使用g#向前查找
#                    # 匹配上一个当前位置的单词
%  匹配括号
/name/c        # \c表示大小不敏感， 或者设置 set ignorecase

查找替换
如何完成把一行中的某个字符替换为另一个字符
:n1,n2 s/word1/word2/g 在n1和n2行之间搜寻word1并且把word2替代之
:1,$ s/word1/word2/g 在整篇文中搜索并替换
:1,$ s/word1/word2/gc 需要确认


:s/vivian/sky/ 替换当前行第一个 vivian 为 sky
:s/vivian/sky/g 替换当前行所有 vivian 为 sky
:n,$s/vivian/sky/ 替换第 n 行开始到最后一行中每一行的第一个 vivian 为 sky
:n,$s/vivian/sky/g 替换第 n 行开始到最后一行中每一行所有 vivian 为 sky
n 为数字，若 n 为 .，表示从当前行开始到最后一行


删除
行内删除
D                 #从当前位置删除到行尾
C                 #直接删除到行尾了
d$                #删除到行尾
dw               #从当前位置删除到下一个单词开头
cw               #删除一个单词，似乎和dw一样
db               #从当前位置删除到前一个单词开头
diw              #删除光标上的单词
dG               #删除到文件末
dgg             #删除到文件首
l1, l2 m l3    #将l1到l2的行移动到l3之后
l1, l2 co l3   #将l1到l2的行拷贝到l3之后

添加
0y$ 拷贝一行
ye 拷贝一个单词
yw   复制一个word
y2w 复制两个word
yy    复制整行
2yy  复制两行
y^   或者y0 复制至行首
y$   复制至行尾
ctrl+r 再"   # 命令行拷贝

缩进
V选中多行，键入 '>'向右缩进，键入'<'向左缩进
使用n==一次性对齐n行，但似乎只能够向右对齐，另外该对齐默认为4个空格，是和设置有关吗？


其他
:set hls            # 打开高亮
:set nohls       # 关闭高亮
ctrl + n/p       # 英文补全
输入开头字符串 + 上/下箭 # 搜索历史， 这类似shell上的“ctrl + r”搜索。
viw                 #选定当前单词。
:set list           #之前编辑的时候，忘记进行tab扩展，如何查看tab键。
:retab             # 将已存在的tab都转化为空格。
（170913 注： 昨天使用vim修改代码，发现效率超低，盯着屏幕还觉得眼睛干涩，之后总算修改完了却发现tab之前没有进行自动扩展，因此对于vim神乎其神之说已多了几分怀疑。今早修改tab扩展，没想到使用一个命令直接完成，让人赞叹。便又对它的印象好了几分。）


编辑操作

2015年10月31日10:54:07
1.多标签编辑
当前少数几个标签的切换操作已经熟悉，不熟悉的是标签多了如何快速切换。
tabnew filename  在新的标签当中打开一个新文件filename
tabn                       切换到下一个标签（右侧）
tabp                       切换到上一个标签（左侧）
tabclose                 关闭当前标签

2. 分屏编辑
ctrl+w+s                #上下分屏当前文件
ctrl+w+v                #左右分屏当前文件
:sp filename           #上下分隔，并打开一个新的文件
:vsp filename         #垂直分隔，并打开一个新的文件
ctrl+W +                #加高
ctrl+W -                 #减高
ctrl+W <                #加宽
ctrl+W >                #减宽

参考：
http://coolshell.cn/articles/1679.html

5. buffer操作
:ls, :buffer               #列出所有缓冲区
:bn                          #下一个缓冲区
:bp                          #上一个缓冲区
:b {number}           #跳转到指定缓冲区
bdelete {number} #删除指定的缓冲
sb 3                        #分屏打开buffer 3
vertical sb 3           #垂直分屏打开buffer 3

参考：
http://harttle.com/2015/11/17/vim-buffer.html  




3. vim下的文件搜索
注：vim自带的find命令与shell当中的是不同的，在vim中使用find需要从指定的path中搜索文件，因此使用之前必须要配置。这个功能可以用来替代一般IDE当中的文件打开，设置步骤：

set path= $pwd/**                   # 设定搜索目录，使用/**表示进行递归搜索。
find MPsPreScheduler.cpp      # 搜索的时候指定文件全名，这与shell当中 find . -name "*scheduler" 不一样。

参考：
http://vim.wikia.com/wiki/Project_browsing_using_find  
http://blog.csdn.net/neosmith/article/details/17308119

查找文件：find . -name "*scheduler"

4. vim下的内容搜索
查找内容：:grep -r --include="*.[ch]" PS_StopUeReq I_Interface/
:cw 取出搜索结果。



插件使用

VIM无插件编程
http://coolshell.cn/articles/11312.html

第一步：
vim directory_name
先进入vim，通过 :E 命令





如何用Vim搭建IDE?
http://harttle.com/2015/11/04/vim-ide.html
http://codingpy.com/article/vim-and-python-match-in-heaven/


1.ctags
下载源代码包，解压进入目录，依次执行如下命令：
./config  # 进行初始配置
make      # 编译
make install # 安装

安装的时候提示：
[lianbche@hzlinb17 ctags-5.8]$ make install
cp ctags /usr/local/bin/ctags  &&  chmod 755 /usr/local/bin/ctags
cp: cannot create regular file `/usr/local/bin/ctags': Permission denied
make: *** [/usr/local/bin/ctags] Error 1

很显然是没有权限。尝试将其安装在本地目录，如下命令：
mkdir /home/lianbche/local/ctags58                                   # 创建本地安装目录
./configure -prefix=/home/lianbche/local/ctags58             # 设定安装目录
make                                                                                        # 编译，之前如果已经编译好，这一步实际上可以省略
make install                                                                             # 安装
export PATH=/home/lianbche/local/ctags58/bin:$PATH   # 添加路径

排错经验：
曾经安装ctags时安装网上提示进行，在安装完成之后在工程目录下面使用ctags -R并没有递归的创建ctags文件，而是提示“ctags: no input files specified.”网上查找了原因大概有两种情况：
版本不对
安装了多个版本的ctags
用使用whereis ctags查看了一下是第二种情况：


的确也存在两个版本。第一个也即是第一次执行configure没有使用-prefix添加安装路径来的。那么这个时候如何删除之前的呢？原来configure是linux下面的一个脚本配置工具，我采用了这里的方式，使用配置脚本当中的make uninstall和make clean删除配置，然后再重新执行上面的命令：
ctags -R   # 生成tag文件
:set tags=/home/lianbche/fddmac/tags   # 设定tags位置
ctrl + ]         # 跳转到定义
ctrl + w + ]  # 跳转到定义，但是在split出的新窗口中打开
ctrl + t         # 跳转上一步

2.taglist
ctags生成之后需要安装vim插件，以便使用生成的这些tag，在这里可以找到taglist的下载文件，插件的安装分为两步：
解压安装包，分别将taglist.vim拷贝到vim的plugin目录，同时将taglist.txt拷贝到vim的doc目录。
在.vimrc当中配置taglist。
（注：第一次尝试安装到/usr/share/vim目录下，也就是系统目录，发现没有权限。之后网上搜索，发现在~/.vim目录下面可以进行安装。）

taglist安装完成之后可以在命令模式下输入如下命令来操作：
:Tlist  #打开左侧窗口，再次输入关闭。或者使用 :TlistToggle。


可以在.vimrc当中添加如下设置 http://www.cnblogs.com/caosiyang/archive/2011/12/23/2299190.html
let Tlist_Show_One_File=1    "只显示当前文件的tags
let Tlist_WinWidth=40        "设置taglist宽度
let Tlist_Exit_OnlyWindow=1  "tagList窗口是最后一个窗口，则退出Vim
let Tlist_Use_Right_Window=1 "在Vim窗口右侧显示taglist窗口

参考：
这里可以学习如何安装。
这里可以找到ctags的下载文件，网速比较慢。

（注：如果没有将ctags添加到PATH中，Tlist在vim中会无法识别，提示Tlist不是命令。）

3. NERDTree http://blog.csdn.net/love__coder/article/details/6659103
NERDTree的安装与taglist类似，解压之后将NERD.vim/NERD.tx的文件拷贝到~/.vim对应的plugin/doc下，或者直接在~/.vim下面解压。命令：
:NERDTree  # 打开左侧
ctrl+w+h    # 跳到左边窗口，ctrl + w + l跳到右边黄口，ctrl+2w 自动在窗口中切换
:q 关闭窗口

安装完成之后在命令模式下输入“:NERDTree"打开左侧。



- mksession! mysession.vim  保存修改之后的session。
