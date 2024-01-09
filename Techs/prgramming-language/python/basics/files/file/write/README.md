## 写文件

```
lines = (
  'Line1: xxx',
  'Line2: xxx'
  )
with open('written.txt', mode='w') as out_file:
  out_file.write('hello')

  out_file.writelines(lines)
  out_file.flush() # 正式写入

with open('written.txt', mode='a') as out_file:
  out_file.write('hello')

with open(input_txt, 'r') as f1, open(output_txt, 'w') as f2, open(mandatory_caselist, 'w') as f3:

for line in f1.readlines():
  pass

```

参考：

- [How do I check if directory exists in Python?](https://stackoverflow.com/questions/8933237/how-do-i-check-if-directory-exists-in-python)
- [Create a directory in Python](https://www.geeksforgeeks.org/create-a-directory-in-python/)


## 新文件多了空格

在Windows下面调用`csv.writer()`写入文件的时候会写入`\r\r\n`，所以可能会多一个空行，这个时候需要设置`newline=''`：

```
with open('/pythonwork/thefile_subset11.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
```

参考：

- [CSV file written with Python has blank lines between each row](https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row)