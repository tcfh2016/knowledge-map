## 如何实现快速查找和替换

使用`grep -rnw . -e 'MAX_NUM_PRACH_PREAMBLE_PROCESSABLE'`完成递归查找。

```
find /path/to/files -type f -exec sed -i 's/oldstring/new string/g' {} \;
grep -rl matchstring somedir/ | xargs sed -i 's/string1/string2/g'
```

`grep -rn '\.psPeerCtrlAddress'`匹配包含'.psPeerCtrlAddress'的文件。


- [](https://stackoverflow.com/questions/15402770/how-to-grep-and-replace)