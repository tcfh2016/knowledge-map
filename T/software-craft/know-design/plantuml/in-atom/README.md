## 升级问题

### 升级本机Java之后出现 "plantuml.jar is not a file"

升级了Java之后在使用plantuml-preview插件生成图形时碰到如下提示：

```
plantuml-preview: C:\Program Files (x86)\Java\jre1.8.0_301\lib\plantuml.jar is not a file.
```

去该路径查看了一下，原来升级之后该目录已经无效，被`C:\Program Files (x86)\Java\jre1.8.0_331\lib`替换，而原目录里面的plantuml.jar也不见了，所以需要重新下载放到升级后的jre1.8.0_331的目录里。

plantuml.jar可以从http://plantuml.com/download下载，有多个版本。将下载的文件放到升级后的新目录之后，再回到ATOM的Plantuml Preview插件里把PlantUML Jar的路径更新为`C:\Program Files (x86)\Java\jre1.8.0_331\lib\plantuml.jar`，就可以了。

当然plantuml.jar也有版本，所以我最近一次更新之后发现里面图形的样式也更新了。



## 安装PlantUml

### 1. npm与apm

APM全称为 Atom Package Manager，为Atom的包管理器。它推荐使用命令`apm config`而非编辑~/.atom/.apmrc文件的形式来配置Atom。

APM是包装了NPM来完成基于Atom的配置，Atom的包安装源自GitHub，而非npmjs.com。

参考：

- [apm - Atom Package Manager](https://github.com/atom/apm)
- [npm 模块安装机制简介](http://www.ruanyifeng.com/blog/2016/01/npm-install.html)



### 2.PlantUml could not generate file

通过命令行安装好PlantUml插件之后测试puml文件提示：

```
PlantUml could not generate file.
Please make sure PlantUml can write to location of original file.
```

搜索之下发现相关问题寥寥，在将github库上所有问题列表阅读完之后也没有找到进一步思路，尤其对于其中提到的手动测试的方法觉得关键但不知道怎么操作。之后直接以关键词"plantuml"搜索发现有本地直接生成的方法。

于是：

1. 下载graphviz，安装并设置环境变量GRAPHVIZ_DOT，指向dot.exe。

https://graphviz.gitlab.io/_pages/Download/Download_windows.html

2. 下载plantuml.jar，这个文件我之前以为需要放到java的lib目录，让它可以直接执行，但测试
之后依然需要指定目录，因此可以放在其他目录，比如 C:\N-20L6PF1F2MV8-Data\lianbche\Downloads\plantuml-jar-mit-1.2019.3 目录，在其中执行`java -jar plantuml.jar -testdot` 可以测试dot成功：

```
C:\Users\lianbche
λ  java -jar plantuml.jar -testdot
The environment variable GRAPHVIZ_DOT has been set to C:\Program Files (x86)\Graphviz2.38\bin\dot.exe
Dot executable is C:\Program Files (x86)\Graphviz2.38\bin\dot.exe
Dot version: dot - graphviz version 2.38.0 (20140413.2041)
Installation seems OK. File generation OK
```

使用如下命令生成测试文件：

```
java -jar plantuml.jar MPsCompMain.plantuml
```

plantuml.jar可以从http://plantuml.com/download下载，有多个版本。

参考：

- [(记录)plantuml安装配置](http://skyao.github.io/2014/12/05/plantuml-installation/)
- [PlantUML安装和使用](http://blog.javachen.com/2016/02/29/plantuml-install-and-usage.html)



## 安装plantuml-viewer

一直安装不成功，失败日志显示是网络问题。

```
/www.atom.io/api/packages/plantuml-viewer/versions/0.7.2/tarball" "--runtime=electron" "--target=2.0.16" "--dist-url=https://atom.io/download/electron" "--arch=x64" "--global-style"
33 verbose node v8.9.3
34 verbose npm  v6.2.0
35 error code Z_BUF_ERROR
36 error errno -5
37 error zlib: unexpected end of file
38 verbose exit [ -5, true ]
```

按照如下命令设置代理：

```
λ apm config set strict-ssl false
λ apm config set https-proxy https://10.144.1.10:8080
λ apm config set http-proxy http://10.144.1.10:8080
```

但一直安装不成功。之后按照教程尝试手动安装，有以下步骤：

- 下载插件包到 C:\Users\User_Name\.atom\packages 目录；
- 添加 npm执行文件目录到系统PATH：C:\Users\User_Nmae\AppData\Local\atom\app-1.34.0\resources\app\apm\bin
- 切入插件目录执行`npm install`或者在任一目录执行`apm install plantuml-viewer`

这个过程中依然会有连网的过程，结果如下：

```
C:\Users\lianbche\.atom\packages\plantuml-viewer  (plantuml-viewer@0.7.2)
λ npm install
npm ERR! code ETIMEDOUT
npm ERR! errno ETIMEDOUTdealTree
npm ERR! network request to https://registry.npmjs.org/node-plantuml failed, reason: connect ETIMEDOUT 104.16.18.35:443
npm ERR! network This is a problem related to network connectivity.
npm ERR! network In most cases you are behind a proxy or have bad network settings.
npm ERR! network
npm ERR! network If you are behind a proxy, please make sure that the npm ERR! network 'proxy' config is set properly.  See: 'npm help config'

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\lianbche\AppData\Roaming\npm-cache\_logs\2019-03-11T07_11_55_788Z-debug.log
```

之后尝试设置apm/npm的代理，但依然不成功，因此只能认定该库不再可用。之后下载另一款插件plantuml，将apm代理删除，进入目录之后执行`apm install`提示成功。

```
C:\Users\lianbche\.atom\packages\plantuml  (plantuml@0.1.2)
λ apm install
Installing modules done
```

参考：

- [手动安装Atom的插件Package](https://blog.51cto.com/francis198/1865695)


## 配置plantuml-preview

尝试第三款插件，依然手动安装，即下载安装包，拷贝其到atom的package目录，然后切入插件目录并执行`apm install`。然而，测试的时候弹出提示框：

```
plantuml-preview: plantuml.jar is not a file.
Verify 'PlantUML Jar' in settings.
```

因为有了这几天的研究，今天下载了plantuml.jar文件，因此大概知道需要配置一下，于是将对应
目录填写到如下setting里面的PlantUML Jar的地址栏里，再测试成功。

![](plantuml-preview-setpath.PNG)

210816：最近一段时间没有使用plantuml，今天突然要画类图的时候再次碰到同样的提示，跑到`C:\Program Files (x86)\Java\jre1.8.0_201\lib\`看了一下，发现没有plantuml.jar这个文件。于是跑到[plantuml](http://plantuml.com/download)上去下载了这个文件，在拷贝到之前的`C:\Program Files (x86)\Java\jre1.8.0_201\lib\plantuml.jar`目录时才发现原来是因为java升级的关系，之前的"jre1.8.0_201"已经更换为“jre1.8.0_301”，所以路径和文件都变更了。
