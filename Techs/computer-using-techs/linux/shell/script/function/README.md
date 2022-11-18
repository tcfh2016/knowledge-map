## 函数

函数按如下格式定义，之后调用的时候直接使用`function_name`即可。

```
function_name () { 
   list of commands
}

function_name () 
{ 
   list of commands
}

# 调用函数
function_name
# 将调用结果赋值给变量var
var=$(function_name)
```

参考：

- [Unix / Linux - Shell Functions](https://www.tutorialspoint.com/unix/unix-shell-functions.htm)


## 参数

```
error_exit()
{
  echo "$1" 1>&2
  exit 1
}

# Using error_exit

if cd "$some_directory"; then
  rm ./*
else
  error_exit "Cannot change directory! Aborting."
fi
```

参考：

- [An Error Exit Function](https://linuxcommand.org/lc3_wss0140.php)