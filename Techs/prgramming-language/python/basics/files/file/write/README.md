## 读取

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
