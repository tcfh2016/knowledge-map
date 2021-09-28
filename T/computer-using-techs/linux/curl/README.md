## [curl](https://curl.se/)

curl用来下载文件。

## Q&A

1）错误“curl: (23) Failed writing body (153 != 16321)”

今天调试了文件下载不下来的问题，用浏览器访问是可以下载的，但是从5天前开始下载的文件就不对（从6M减小到339K）。之后发现是因为文件地址访问方式从http访问变为了https，所以无法成功下载文件。

在添加了`-k`选项之后发现又提示“curl: (23) Failed writing body (153 != 16321)”的错误，搜索良久，终于在CSDN上发现可能和磁盘空间有关。突然想起之前碰到过home目录下面过多core文件导致空间不足的问题，删除core文件后问题解决。

参考：

- [Curl command for https ( SSL )](https://stackoverflow.com/questions/28927051/curl-command-for-https-ssl)
- [curl: (23) Failed writing body (0 != 7937) 异常原因](https://blog.csdn.net/lijian965644856/article/details/108339978)
