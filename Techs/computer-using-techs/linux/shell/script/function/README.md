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

函数的参数类似于“命令行参数”，*所以并不需要显示的定义形式参数*，可以直接通过$1表示第一个参数，$2表示第二个参数，而$0代表了函数名称。

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


## 返回值

在shell中的函数返回值时，不能像其他编程语言里面那样直接`return ret`，而是要`echo ret`。

```
get_buildid() {
  ...
  echo ${buildid}
}

build_id=$( get_buildid $1 )
```

参考：

- [Returning value from called function in a shell script](https://stackoverflow.com/questions/8742783/returning-value-from-called-function-in-a-shell-script)