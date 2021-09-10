## 使用ATOM编写C++程序

由于ATOM并不携带任何编译起，所以最开始的时候需要保证编译器在工作的计算机上是可用的。比如我想在Windows操作系统上编写C++，那么可以选择先安装`mingw64`并配置好系统path。

之后安装`linter-gcc`，该插件依赖的`linter`，`linter-ui-default`会自动提示进行安装。整个过程完成之后编写的c++程序会进行语法检查并及时提示错误（记得安装后重启ATOM使之生效）。

最后安装`gpp-compiler`，就可以直接右键选择“compile and run”编译和运行程序了。
