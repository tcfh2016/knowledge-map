## [安装boost库](https://www.boost.org/doc/libs/1_55_0/more/getting_started/windows.html)

原来以为直接将下载的boost库解压并添加系统path就可以了，在看过[ Install Boost C++ Library on Windows](https://www.youtube.com/watch?v=5afpq2TkOHc)这个视频后才知道需要先编译，于是回到[官方文档](https://www.boost.org/doc/libs/1_55_0/more/getting_started/windows.html#prepare-to-use-a-boost-library-binary)上去查看编译步骤。

第一步：执行`bootstrap`准备boost编译前期工作

结果提示"'cl' is not recognized as an internal or external command"，"cl"是MSVC工具（微软编译工具）。

![](./bootstrap_fail.png)

幸好在[这篇文章](https://joshuaburkholder.com/wordpress/2013/09/17/how-to-compile-boost-using-gpp-stdcpp11-from-mingw/)里面看到了`bootstrap mingw`的命令，尝试后成功。

第二步：执行`.\b2`去编译boost库

C:\Program Files\boost\boost_1_55_0


隔了几天前面的步骤忘了，但是boost例子一直编译不成功。查找到[Installing boost libraries for GCC (MinGW) on Windows](https://gist.github.com/sim642/29caef3cc8afaa273ce6)，准备按照步骤重试，下载了1.75.0的版本但是编译的时候失败了，提示：

```
sysinfo.cpp: In function 'unsigned int {anonymous}::std_thread_hardware_concurrency()':
sysinfo.cpp:93:21: error: 'std::thread' has not been declared
         return std::thread::hardware_concurrency();
```

在[这里](https://github.com/boostorg/type_erasure/issues/16)看到了原因，似乎是因为本地的mingw版本太老：

![](compile-error-thread.png)

在[安装了新的mingw]()之后再按照[Installing boost libraries for GCC (MinGW) on Windows](https://gist.github.com/sim642/29caef3cc8afaa273ce6)重试，第一步执行`.\bootstrap.bat mingw`编译成功：

![](./bootstrap-build-done.png)

第二步，boost build准备。执行`.\b2 --prefix="C:\Program Files\boost-build"`时候会因为"Access is denied."失败，这个时候可以在启动powershell的时候右键选择“run as administrator”可以解决，可以参考[Access is denied for "bootstrap" command](https://social.technet.microsoft.com/Forums/en-US/efb69edd-012d-4205-97f6-7a22653699ad/access-is-denied-for-quotbootstrapquot-command?forum=configmgrgeneral)。

第三步，boost build。将"C:\Program Files\boost-build\bin"添加到系统环境变量Path，然后进入"C:\Program Files\boost_1_75_0"，执行`b2 --build-dir="C:\Program Files\boost_1_75_0\build" --prefix="C:\Program Files\boost" toolset=gcc install` *这两个路径都是新建的目录，注意也要以管理员权限执行*

![](./boost-build.png)

第四步，配置inlcude和linker文件夹。在编译完成之后，会生成include和lib两个文件夹，分别可用于编译时指定。将`C:\Program Files\boost\include\boost-1_75`添加到Include目录。

![](./compile-boost-done.png)


在cpp目录下面执行`g++ .\boost_optional_ex.cpp -o boost -I "C:\Program Files\boost\include\boost-1_75"`可以正常编译。不过配置ATOM还没有成功。
