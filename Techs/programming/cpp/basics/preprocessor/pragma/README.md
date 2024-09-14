## `#pragma once`

和防止头文件重复包含的预处理指令作用一样，据说因为不会进行预处理工作而显得更快，但实际讨论结论不一。

参考：

- [#pragma once](https://zh.wikipedia.org/wiki/Pragma_once)
- [Is #pragma once a safe include guard?](https://stackoverflow.com/questions/787533/is-pragma-once-a-safe-include-guard)

## FAQ

1）使用时出现“warning: #pragma once in main file”告警

这个是因为尝试着编译包含有“#pragma once”的源代码文件，我当前是在ATOM使用了自动预编译的插件，所以会有这个提示。
