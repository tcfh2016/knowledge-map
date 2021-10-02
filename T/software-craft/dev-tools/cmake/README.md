## [CMake](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)

CMake让开发者可以编写一种与平台无关的CMakeLists.txt来定制工程的编译流程，之后CMake工具会使用该文件来生成对应平台的Makefile文件。

参考：

- [CMake 入门实战](https://www.hahack.com/codes/cmake/)


## CMake的安装

不同平台有不同的安装方式，Windows下可以将编译好的二进制软件包下载下来，然后添加到系统变量里面。一些细节可以参考[Installing CMake](https://cmake.org/install/)。

## CMake的使用

CMake的使用手册在[CMake Tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)，不过读过了之后发现一头雾水，还是从[CMake Example](https://cmake.org/examples/)上去看更容易理解。

编写了一个最简单的CMakeLists.txt，root目录就一个main.cpp，另外有两个pizza, pizza_store单独存放了头文件，如下：

```
cmake_minimum_required(VERSION 3.21.3)

project(FactoryMethod)

add_subdirectory(pizza)
add_subdirectory(pizza_store)

add_executable(main main.cpp)
```

执行`make .`，提示编译器还没有配置：

```
CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!
```

在[]()里面没有发现要配置编译器，所以搜索“CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage”，之后在[How do you set CMAKE_C_COMPILER and CMAKE_CXX_COMPILER for building Assimp for iOS?](https://stackoverflow.com/questions/11588855/how-do-you-set-cmake-c-compiler-and-cmake-cxx-compiler-for-building-assimp-for-i)找到两种可选的解决方法：

1. 在执行命令的时候加上参数比如：`cmake -D CMAKE_C_COMPILER="/path/to/your/c/compiler/executable" -D CMAKE_CXX_COMPILER "/path/to/your/cpp/compiler/executable" /path/to/directory/containing/CMakeLists.txt`
2. 在CmakeLists.txt里面设置`set(CMAKE_CXX_COMPILER "C:\\msys64\\mingw64\\bin")`

这样设定之后对应的错误就消失了。不过一直提示第6行“project(FactoryMethod)”的`The system cannot find the file specified`错误，从官方手册上查看不到原因，所以在中文搜索中找到了[CMake 入门实战](https://www.hahack.com/codes/cmake/)，阅读之下发现自己的大致方向没有问题。

实在没有办法，只好创建一个最基本的hello world来进行测试，发现依旧提示"The system cannot find the file specified"的错误。由于无法得知更多的错误信息，所以去`cmake --help`里面阅读命令提示，发现当前默认的是"NMake Makefiles"，而选项里面还有“MSYS Makefiles”和“MinGW Makefiles”。于是我使用[windows+cmake+mingw 搭建c/c++开发环境](https://zhuanlan.zhihu.com/p/35137700)提到的命令逐个尝试过来发现`cmake . -G "MinGW Makefiles"`可以正常执行。

上一步已经成功生成了Makefile，接下来可以键入“make”来编译了，然而发现找不到make。但实际上，在mingw目录“C:\msys64\mingw64\bin”里面已经有了“mingw32-make.exe”，所以拷贝一份并命名为make.exe即可。


## Q&A

1）“cmake Error: could not load cache”错误

仿照示例编写了一个最简单的版本，并执行`cmake --build .`，提示“cmake Error: could not load cache”错误。后面发现是需要先执行`cmake .`进行配置再执行`cmake --build .`。

2）怎样设定默认的make工具

在Windows下安装的cmake默认选择的是nmake工具，所以如果使用了MinGW来完成编译，每次执行的之后必须添加`-G "MinGW Makefiles"`选项。是否可以默认设定
