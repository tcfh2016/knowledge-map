## glob

`glob`库可以方便的得到某个目录下面按照特定模式匹配的文件。

```
import glob
import os

glob.glob('*.*') # 得到当前目录下所有文件
glob.glob(os.path.join(path, '*.csv')) # 得到path目录下所有文件
```


参考：

- [glob — Unix style pathname pattern expansion](https://docs.python.org/3/library/glob.html)
