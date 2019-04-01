## 行处理/sed

```
sed -i '/demo/d' file_name # 删除file_name文件中包含"demo"字段的所有行。
sed -i 's/^.*string_a/string_b/g' file_name # 替换string_a为string_b。
sed '/^$/d'      file_name # 删除空行。
sed "/^\s*$/d"   file_name # 这句代表可以删除文本中的空白行（包括space、tab、enter）
sed '/^\s.*$/d'  file_name # 这句代表可以删除文本中的空白行（包括space、tab、enter），以及空格键开头的行
sed '/^\t*$/d'   file_name # 这句代表文本中的tab和直接enter

```

*正则表示法中，星号代表重复之前一个字符的0个或0个以上，小数点‘.‘代表任意字符，‘\s‘代表space或tab，‘\t‘代表tab。*

参数：

- -i[SUFFIX], --in-place[=SUFFIX]: 直接修改原始文件。
