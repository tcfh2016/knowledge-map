在将Python对象写入磁盘的时候通常会使用`pickle` 用来支持序列化操作。


## pickle.dump(obj, file)

The file argument must have a write() method that accepts a single bytes argument. It can thus be an on-disk file opened for binary writing.

## pickle.load(file)

The argument file must have two methods, a read() method that takes an integer argument, and a readline() method that requires no arguments. Both methods should return bytes. Thus file can be an on-disk file opened for binary reading.


- [pickle — Python object serialization](https://docs.python.org/3/library/pickle.html)
- [pickle — Python object serialization](https://docs.python.org/2/library/pickle.html)

# 问题列表

### 1.TypeError: write() argument must be str, not bytes

执行如下代码遇到的问题：

```
a = [gauss(1.5, 2) for i in range(1000000)]

pkl_file = open('data.pkl', 'w')
pickle.dump(a, pkl_file)
pkl_file.close()
```

问题的原因在于Python 3.x里面使用 dump/load方法时需要指定进行"binary"读写方式，这在Python 2.x里面不需要。

- [Using pickle.dump - TypeError: must be str, not bytes](https://stackoverflow.com/questions/13906623/using-pickle-dump-typeerror-must-be-str-not-bytes)
