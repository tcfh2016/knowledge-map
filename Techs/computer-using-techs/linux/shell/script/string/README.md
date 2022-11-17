## 字符串匹配

参考How to check if a string contains a substring in Bash](https://stackoverflow.com/questions/229551/how-to-check-if-a-string-contains-a-substring-in-bash)：

```
string='My long string'
if [[ $string == *"My long"* ]]; then
  echo "It's there!"
fi
```
