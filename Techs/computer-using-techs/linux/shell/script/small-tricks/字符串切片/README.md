## 字符串切片

在[这里](https://blog.csdn.net/rockstics/article/details/116917653)有一篇有关字符串切片的文章。以`str=abced`举例：

- 使用`${#var}`来返回字符串的长度，比如`echo ${#str}`输出为`5`。
- 使用`${var:offset}`来去取offset（不包括）到length-1之间的字符串。比如`echo ${#str:1}`输出为`bced`。
- 使用`${var:offset:number}`来取offset（不包括）开始的`number`个字符串。

另外比较复杂一点的方式：

- 使用`${var: -length}`取字符串最右侧length个字符，注*冒号后必须有空格*。比如`echo ${str: -2}`返回`ed`。
使用`${var:offset:-length}`取从offset开始，到倒数length字符之间的字符串，去掉头尾，比如`echo ${str:0:-1}`返回`abce`。


或参考[Shell脚本编程之字符串切片](https://www.cnblogs.com/haona_li/p/10334057.html)。


参考：

- [How do I split a string on a delimiter in Bash?](https://stackoverflow.com/questions/918886/how-do-i-split-a-string-on-a-delimiter-in-bash)