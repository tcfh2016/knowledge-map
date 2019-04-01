## 文本搜索 / grep

搜索文件内容。

### 反向匹配

```
cat smb.conf | grep -v "#" | grep -v ";" | grep -v "^$"
```

### 简单搜索

```
 git log | grep -i test -A 5 -B 1 # 输出包含"test"字段极其前5行和后1行内容。
```

参数：
- -A NUM, --after-context=NUM: 输出匹配行之前的NUM行。
- -B NUM, --before-context=NUM：输出匹配行之后的NUM行。
- -C NUM, -NUM, --context=NUM：输出匹配行前后的NUM行。              

### 使用正则表达式

```
cat SYSLOG | grep -E 'macps|RX PHY' > SYSLOG_183_MAC_ULPHY.LOG # 多项搜索
```

### "Binary file (standard input) matches" 问题

在对文件执行搜索的时候，比如执行`cat command.txt | grep -i 'Cell'`提示“Binary file (
standard input) matches”，其原因是grep识别其为data文件类型，解决方案为添加 `-a`参数。

- [参考](https://unix.stackexchange.com/questions/335716/grep-returns-binary-file-standard-input-matches-when-trying-to-find-a-string)
