# 可变参数

最近修改clang warning，发现会对可变参数的宏报`pro-bounds-array-to-pointer-decay`错误，
改告警提示的是指针指向了数组。

```
va_start(vaArgs, inputString);
AaSysLogVPrint(severity, inputString, vaArgs);
va_end(vaArgs);
```

va_start, va_arg, va_end声明在头文件stdarg.h中，里面也定义了va_list这种类型。

- va_start(va_list ap, last)：根据inputString来初始化vaArgs，即找到inputString
之后的第一个参数
- va_arg(va_list ap, type)：获取ap指向参数的指，这个参数是在上面初始化的，并让ap指向
下一个参数
- va_end(va_list ap)：结束时释放ap。

所以va_list就是一个指针，用来指向对应的参数。

参考：

- [可變參數的使用](https://twblogs.net/a/5b9817f72b717736c6218092)
- [How are variable arguments implemented in gcc?](https://stackoverflow.com/questions/12371450/how-are-variable-arguments-implemented-in-gcc)
- [Is GCC mishandling a pointer to a va_list passed to a function?](https://stackoverflow.com/questions/8047362/is-gcc-mishandling-a-pointer-to-a-va-list-passed-to-a-function)
