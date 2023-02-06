## 字符串匹配

参考How to check if a string contains a substring in Bash](https://stackoverflow.com/questions/229551/how-to-check-if-a-string-contains-a-substring-in-bash)：

```
string='My long string'
if [[ $string == *"My long"* ]]; then
  echo "It's there!"
fi
```

*注：在使用`[ s1 = s2 ]`的时候如果只有单括号，那么s1和s2必须是常量。如果其中之一为变量，那么需要使用`[[ ${s1} = ${s2} ]]`。或者使用`[ "${s1}" = s2 ]`*

- string1 = string2: True if string1 equals string2.
- string1 != string2: True if string1 does not equal string2.


## 字符串相加

在shell里面两个字符串相加只需要简单的写在一起即可。

```
a='Hello'
b='World'
c="${a} ${b}"
```

参考：

- [How to concatenate string variables in Bash](https://stackoverflow.com/questions/4181703/how-to-concatenate-string-variables-in-bash)