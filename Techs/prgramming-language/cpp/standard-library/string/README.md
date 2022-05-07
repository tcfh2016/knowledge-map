## 将string写入文件

理解C++中的字符串对象需要窥探string的实现，然后记住`string对象`和`string保存的字符串`本身是分离的，在`string对象`里面仅仅有字符串的长度以及指向保存字符串内存的指针。所以，再写文件或者输出string的时候需要记住这一点。

举个例子，如果我想要将一个string对象保存到文件里面，

```
#include <fstream>
...
std::ofstream out("output.txt");
out << input;
out.close();
```

参考：

- [How to write std::string to file?](https://stackoverflow.com/questions/15388041/how-to-write-stdstring-to-file)
