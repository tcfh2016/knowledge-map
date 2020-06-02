2018年10月29日10:51:12
gdb单步调试，发现无法打印当前变量的值，其他代码均能正常查看：
No symbol "cellParams" in current context

google之下发现可能是编译器启用了优化选项：
https://stackoverflow.com/questions/3758614/gdb-no-symbol-i-in-current-context
在eclipse的配置上找了编译选项，发现并没有打开，因此查看其它的回答，另外的一种回答是GDB和编译器不匹配。

当前的GDB版本：
[lianbche@hzlinb17 fddmac]$ gdb lteDo/gtest_sm3/exec/gtest/debug/TestMPsRoundRobinScheduleModeB
GNU gdb (GDB) Red Hat Enterprise Linux (7.2-60.el6_4.1)

根据上面的提示尝试安装更高的版本，第一次尝试了最新的8.2但是在make的时候由于c++11的依赖错误，重新尝试7.5的。安装步骤有如下几步：
tar -zxvf gdb-7.5.tar.gz
切换到 gdb-7.5目录，执行./configure
make -- 成功
sudo make install -- 失败，提示 “Sorry, user lianbche is not allowed to execute '/usr/bin/make install' as root on hzlinb17.china.nsn-net.net.”

尝试如下的方式，用“sudo cp gdb/gdb /usr/local/bin/gdb”直接拷贝，提示
https://askubuntu.com/questions/529781/upgrade-from-gdb-7-7-to-7-8

[lianbche@hzlinb17 gdb-7.5]$ sudo cp gdb/gdb /usr/local/bin/gdb
[sudo] password for lianbche:
Sorry, user lianbche is not allowed to execute '/bin/cp gdb/gdb /usr/local/bin/gdb' as root on hzlinb17.china.nsn-net.net.
[lianbche@hzlinb17 gdb-7.5]$

那么我是不是可以直接使用？单独使用可以，但是GDB里面会提示错误。
Reading symbols from /home/lianbche/fddmac/lteDo/gtest_sm3/exec/gtest/debug/TestMPsRoundRobinScheduleModeB...done.
(gdb) run
Starting program: /home/lianbche/fddmac/lteDo/gtest_sm3/exec/gtest/debug/TestMPsRoundRobinScheduleModeB
warning: no loadable sections found in added symbol-file system-supplied DSO at 0xf7fd7000
warning: Could not load shared library symbols for linux-gate.so.1.
Do you need "set solib-search-path" or "set sysroot"?
warning: File "/build/ltesdkroot/data/Platforms/SDK/PS_LFS_SDK_5_28/PS_LFS_SDK_5_28/bld-tools/i686-pc-linux-gnu/i686-pc-linux-gnu/sys-root/usr/lib/libthread_db-1.0.so" auto-loading has been declined by your `auto-load safe-path' set to "$debugdir:$datadir/auto-load".
warning: Unable to find libthread_db matching inferior's thread library, thread debugging will not be available.
cp-name-parser.y:220: internal-error: make_operator: Assertion `i' failed.
A problem internal to GDB has been detected,
further debugging may prove unreliable.

之后在eclipse上点击console模块，发现里面也使用了gdb，路径是/mac/common/tools/gdb-12/bin/gdb，这个版本更高，使用了一下发现总算可以使用print命令了！


2018年10月25日15:34:43
用GDB调试UT有如下错误：
warning: no loadable sections found in added symbol-file system-supplied DSO at 0xf7fd7000
warning: Could not load shared library symbols for linux-gate.so.1.
Do you need "set solib-search-path" or "set sysroot"?
/home/lianbche/fddmac/lteDo/gtest_sm3/exec/gtest/debug/TestMPsRoundRobinScheduleModeB: error while loading shared libraries: libGtestStubs.so: cannot open shared object file: No such file or directory

Program exited with code 0177.

尝试一：失败
https://stackoverflow.com/questions/24896034/solib-absolute-prefix-vs-solib-search-path-in-gdb
set solib-absolute-prefix /tmp/host 针对绝对路径展开搜索
set solib-search-path /tmp/host/usr/lib 如果库存在于多处，用该命令分别制定
set solib-search-path /tmp/host/usr/lib:/tmp/host/usr/local/lib

尝试二：成功
https://stackoverflow.com/questions/44896217/how-to-save-set-solib-search-path

首先，找到该LIB对应的路径
[lianbche@hzlinb17 fddmac]$ find . -name 'libGtestStubs.so'
./lteDo/gtest_sm3/lib/gtest/release/libGtestStubs.so
./lteDo/gtest_sm3/lib/gtest/debug/libGtestStubs.so
./lteDo/gtest_sm3/C_Test/gtest/TestModules/libGtestStubs/gtest/release/libGtestStubs.so
./lteDo/gtest_sm3/C_Test/gtest/TestModules/libGtestStubs/gtest/debug/libGtestStubs.so

其次，将如下搜索路径添加到 .bashrc里面的 LD_LIBRARY_PATH里，然而仍旧失败。
/home/lianbche/fddmac/lteDo/gtest_sm3/lib/gtest/release/
/home/lianbche/fddmac/lteDo/gtest_sm3/lib/gtest/debug/
/home/lianbche/fddmac/lteDo/gtest_sm3/C_Test/gtest/TestModules/libGtestStubs/gtest/release/
/home/lianbche/fddmac/lteDo/gtest_sm3/C_Test/gtest/TestModules/libGtestStubs/gtest/debug/

再次，尝试用export命令来设置，竟然可以。
https://www.gnu.org/software/gsl/manual/html_node/Shared-Libraries.html
$ LD_LIBRARY_PATH=/home/lianbche/fddmac/lteDo/gtest_sm3/lib/gtest/debug/
$ export LD_LIBRARY_PATH

重新试验，发现是因为在.bashrc添加路径时没有使用export 关键字：
export LD_LIBRARY_PATH=/home/lianbche/fddmac/lteDo/gtest_sm3/lib/gtest/debug 可以
LD_LIBRARY_PATH=/home/lianbche/fddmac/lteDo/gtest_sm3/lib/gtest/debug 不可以



GDB调试的时候提示 "No such file or directory"：通常是由于GDB没有找到源代码，因此需要设定源代码路径，如下命令将GDB默认的路径修改为另一个：

set substitute-path '/ephemeral/workspace/CB.FL18A.BUILD-TARGET/build' '/home/lianbche/fddmac'

print 打印的时候可能数据太多会出现：
(gdb) p ::macps::dl::catm::MUserStorage::getStorage()
value of type `macps::dl::catm::MUserStorage' requires 307440 bytes, which is more than max-value-size
(gdb)

将最大值设大：
https://sourceware.org/gdb/onlinedocs/gdb/Value-Sizes.html



2015年5月1日16:08:30
调试循环
for (i=0; i<9; i++)
    print();

watch i            // 监视i，之后一旦i的值变化那么就如break的效果，程序会停住
info break       // 查看当前监视的断点序号
ignore break_no changed_time  // 请求将在i变动多少次停住

使用笔记：如果i初始化为0，需要在i=1的时候停住，这个时候使用ignore 2 1 只能够停止到i=2，所以可以直接c，因为每一次i改变都会停下。

continue number


2015年4月28日10:30:15
ulimit -c 查看

ulimit -c unlimited

之后使用gdb -c core-file out-file


01 添加调试信息
2016年7月19日10:00:43
编译link.cpp: g++ -o link link.cpp
使用gdb调试：
=>启动gdb。 gdb => 设置断点。(gdb) b HashTable<int, int>::InsertBreakpoint 1 at 0x400a04(gdb) runStarting program: /home/lianbche/gitlab/coding-cpp/201607/link/linkwarning: no loadable sections found in added symbol-file system-supplied DSO at 0x7ffff7ffd000Breakpoint 1, 0x0000000000400a04 in HashTable<int, int>::Insert(int const&) ()Missing separate debuginfos, use: debuginfo-install glibc-2.12-1.166.el6_7.7.x86_64 libgcc-4.4.6-4.el6.x86_64 libstdc++-4.4.6-4.el6.x86_64

怀疑是编译时没有加入DEBUG信息，于是使用g++ -c -o link link.cpp再次编译并启动gdb调试，有如下提示：
(gdb) b HashTable<int, int>::InsertBreakpoint 1 at 0x208(gdb) runStarting program: /home/lianbche/gitlab/coding-cpp/201607/link/link/bin/bash: /home/lianbche/gitlab/coding-cpp/201607/link/link: Permission denied/bin/bash: line 0: exec: /home/lianbche/gitlab/coding-cpp/201607/link/link: cannot execute: Permission deniedDuring startup program exited with code 126.

没有权限，莫非是因为编译选项'-c'添加得不对？
- 查看GCC笔记，编译选项 '-c'是生成.o，不进行链接的意思。
- 正确的编译选项是'-g'。
171027 注：使用makefile的时候 -g 的选项一般加在生成.o的时候。

02 断点设置
break filename:linenum
break filename:functionname
break *address
break if (i==100)

03 观察点设置
watch <expr>   表达式的值变化时
rwatch <expr>  表达式被读时
awatch <expr>  表达式被读或被写时

watch i ==> breakpoint 编号
ignore 编号 2 ==》 忽略2次

04 捕获点设置
catch <event> 当event有变化时

1. 程序被停住，用info program来查看当前程序为什么被停住；
