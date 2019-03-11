## 在ATOM里面安装plantuml插件

### npm与apm

APM全称为 Atom Package Manager，为Atom的包管理器。它推荐使用命令`apm config`而非编辑
~/.atom/.apmrc文件的形式来配置Atom。

APM是包装了NPM来完成基于Atom的配置，Atom的包安装源自GitHub，而非npmjs.com。

参考：

- [apm - Atom Package Manager](https://github.com/atom/apm)


### 安装plantuml-viewer

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

参考：

- [手动安装Atom的插件Package](https://blog.51cto.com/francis198/1865695)
