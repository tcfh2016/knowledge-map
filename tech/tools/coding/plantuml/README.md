## 在ATOM里面安装plantuml插件

1.安装plantuml-viewer

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
λ apm config set https-proxy http://10.144.1.10:8080
```

npm ERR! code ETIMEDOUT
npm ERR! errno ETIMEDOUT
npm ERR! network request to https://www.atom.io/api/packages/plantuml-viewer/versions/0.7.2/tarball failed, reason: connect ETIMEDOUT 34.206.253.53:443
npm ERR! network This is a problem related to network connectivity.
npm ERR! network In most cases you are behind a proxy or have bad network settings.
npm ERR! network
npm ERR! network If you are behind a proxy, please make sure that the


Please make sure PlantUml can write to location of original file.
