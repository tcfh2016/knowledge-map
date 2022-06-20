## 切分/split

切分文件。

```
split -b 15m error.log         # 以15M的大小分隔，生成文件名xaa,xab
split -b 15 error.log mylog -d # 以15字节大小分隔，生成文件名mylog01, mylog02
cat xaa  xab > large.log       # 还原分隔的文件
```

参数：

- -b, --bytes=SIZE: put SIZE bytes per output file      
- -l, --lines=NUMBER: put NUMBER lines per output file
- -d, --numeric-suffixes: use numeric suffixes instead of alphabetic
