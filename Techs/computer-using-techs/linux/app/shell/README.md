Shell常见命令。



## 如何实现快速查找和替换

使用`grep -rnw . -e 'MAX_NUM_PRACH_PREAMBLE_PROCESSABLE'`完成递归查找。

```
find /path/to/files -type f -exec sed -i 's/oldstring/new string/g' {} \;
grep -rl matchstring somedir/ | xargs sed -i 's/string1/string2/g'
```

`grep -rn '\.psPeerCtrlAddress'`匹配包含'.psPeerCtrlAddress'的文件。


- [](https://stackoverflow.com/questions/15402770/how-to-grep-and-replace)

## source

`source`命令用来在当前shell里面（当前进程）执行该脚本，不同于使用`sh script.sh`会在新的子进程里面执行脚本的方式。

参考：

- [利用 source 來執行腳本：在父程序中執行](http://linux.vbird.org/linux_basic/0340bashshell-scripts.php#some_ex_run)
