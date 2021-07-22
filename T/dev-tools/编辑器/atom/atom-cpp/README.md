## 使用ATOM编写C++程序

由于ATOM并不携带任何编译起，所以最开始的时候需要保证编译器在工作的计算机上是可用的。比如我想在Windows操作系统上编写C++，那么可以选择先安装`mingw64`并配置好系统path。

之后安装`linter-gcc`，该插件依赖的`linter`，`linter-ui-default`会自动提示进行安装。整个过程完成之后编写的c++程序会进行语法检查并及时提示错误（记得安装后重启ATOM使之生效）。

最后安装`gpp-compiler`，就可以直接右键选择“compile and run”编译和运行程序了。

## [安装boost库](https://www.boost.org/doc/libs/1_55_0/more/getting_started/windows.html)

原来以为直接将下载的boost库解压并添加系统path就可以了，在看过[ Install Boost C++ Library on Windows](https://www.youtube.com/watch?v=5afpq2TkOHc)这个视频后才知道需要先编译，于是回到[官方文档](https://www.boost.org/doc/libs/1_55_0/more/getting_started/windows.html#prepare-to-use-a-boost-library-binary)上去查看编译步骤。

第一步：执行`bootstrap`准备boost编译前期工作

结果提示"'cl' is not recognized as an internal or external command"，"cl"是MSVC工具（微软编译工具）。

![](./bootstrap_fail.png)

幸好在[这篇文章](https://joshuaburkholder.com/wordpress/2013/09/17/how-to-compile-boost-using-gpp-stdcpp11-from-mingw/)里面看到了`bootstrap mingw`的命令，尝试后成功。

第二步：执行`.\b2`去编译boost库

C:\Program Files\boost\boost_1_55_0
