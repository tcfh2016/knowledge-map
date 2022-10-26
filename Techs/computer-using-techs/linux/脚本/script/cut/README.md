## 字符串切片

在[这里](https://blog.csdn.net/rockstics/article/details/116917653)有一篇有关字符串切片的文章：

```
str=abced
echo ${#str} #5

${var:offset} #取offset -> length-1的字符串
${var: -length} #-length -> length-1的字符串，冒号后必须有空格
echo ${#str:1} #bced
echo ${#str: -2} #ed

${var:offset:-length} #取从offset开始，到倒数length字符之间的字符串，去掉头尾
echo ${#str:0:-1} #abce
```

或参考[Shell脚本编程之字符串切片](https://www.cnblogs.com/haona_li/p/10334057.html)。