## 文本搜索 / grep

搜索文件内容。

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


## 行处理/sed

```
sed -i '/demo/d' file_name # 删除file_name文件中包含"demo"字段的所有行。
sed -i 's/^string_a/string_b/g' file_name # 替换string_a为string_b。
sed '/^$/d'      file_name # 删除空行。
sed "/^\s*$/d"   file_name # 这句代表可以删除文本中的空白行（包括space、tab、enter）
sed '/^\s.*$/d'  file_name # 这句代表可以删除文本中的空白行（包括space、tab、enter），以及空格键开头的行
sed '/^\t*$/d'   file_name # 这句代表文本中的tab和直接enter

```

*正则表示法中，星号代表重复之前一个字符的0个或0个以上，小数点‘.‘代表任意字符，‘\s‘代表space或tab，‘\t‘代表tab。*

参数：

- -i[SUFFIX], --in-place[=SUFFIX]: 直接修改原始文件。


## 列处理/awk

将文本行划分为列进行处理。

```
cat cycle.txt | awk 'BEGIN {FS="="} $1 {print $2}' > ca-data # 对每行按照"="进行分列，并输出第2列。
```


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


## 统计/wc

统计文件的行数。

```
wc -l file_name  # 统计file_name的行数。
ls -a | wc -l    # 灵活用法：查看目录a中的文件个数。
```
参数：

- -c, --bytes: print the byte counts
- -m, --chars: print the character counts
- -l, --lines: print the newline counts
- -w, --words: print the word counts             
