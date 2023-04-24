## 查看文件大小，以“MB”单位显示

执行`ll`默认的单位为字节，但使用`ls -l --block-size=M`可以按照兆字节展示，换算单位为：1MB = 1024 * 1024 B。

或者执行`ls -lh`以便于阅读的方式展示出来。


参考：

- [How do I make `ls` show file sizes in megabytes?](https://unix.stackexchange.com/questions/64148/how-do-i-make-ls-show-file-sizes-in-megabytes)


## 按修改顺序显示

使用`ls -lr --sort=time`可以按照时间倒数排序。`-r`是倒叙显示，`-l`是长列表显示。

```
--sort=WORD
sort by WORD instead of name: none (-U), size (-S), time (-t), version (-v), extension (-X)
```