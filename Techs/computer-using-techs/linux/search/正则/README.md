## 正则



## 在“441”，"442", "443"中过滤掉“441”

比如我有下面这些文件夹，但是我不想匹配“441”开头的，其实可以通过`find . -name "log_44[2-9]*"`来达到目的。因为`[]`可以用来匹配一系列字符（单个字符可以为制定的任何一个）。当然，在`[]`还可以利用反向字符`^`，所以`find . -name "log_44[^1]*"`也可以达到目的。

```
[bing]$ find . -name "log_44*"
./log_44151
./log_441
./log_44346
./log_44876
./log_44577
```


- [正则表达式](https://math.ecnu.edu.cn/~jypan/Teaching/Linux/Linux08/lect07p_rexp.pdf)
- [正则表达式入门](https://houxiaoxuan.top/2021/02/05/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F/)
