## 文件读写

在C里面使用文件读写的时候，常见的有`read/write`和`fread/fwrite`，大致区别如下：

- `read/write`会直接进行系统调用，但是`fread/fwrite`会工作在一个缓冲存，以避免频繁的进行费时的系统调用。
- `read/write`是在Posix标准定义，而`fread/fwrite`定义在C语言标准，后者的实现是使用前者。

按照[这里](https://blog.csdn.net/ljlstart/article/details/49535005)的描述，`read/write`系统调用会执行用户态到内核态之间的切换，因此比较费时。而`fread/fwrite`则不会直接进行系统调用，而是会在用户态创建缓存。

比如使用`fread`的时候会从内核态读取相比参数更多的数据到用户态的缓存区中，下次用户读取更多的时候或许就不需要去内核态读取。而使用`fwrite`的时候也一样，会先将写入的数据放到用户态的缓存区中，等到写入的数据填满用户态的缓冲区再切入内核态去写。这里缓冲区的设置可以参见[12.20.3 Controlling Which Kind of Buffering](http://www.gnu.org/software/libc/manual/html_node/Controlling-Buffering.html)，有"full buffering", "line buffering"和"unbuffered input/output"三种模式。*注：`write`调用时写入内核态后，操作系统会负责将数据写入文件。*


> When a stream is ``unbuffered'', bytes are intended to appear from the source or at the destination as soon as possible; otherwise, bytes may be accumulated and transmitted as a block. When a stream is ``fully buffered'', bytes are intended to be transmitted as a block when a buffer is filled. When a stream is ``line buffered'', bytes are intended to be transmitted as a block when a newline byte is encountered. Furthermore, bytes are intended to be transmitted as a block when a buffer is filled, when input is requested on an unbuffered stream, or when input is requested on a line-buffered stream that requires the transmission of bytes. Support for these characteristics is implementation-defined, and may be affected via setbuf() and setvbuf().


参考：

- [Why the fwrite libc function is faster than the syscall write function?](https://stackoverflow.com/questions/1360021/why-the-fwrite-libc-function-is-faster-than-the-syscall-write-function/1360651)
- [2.5 Standard I/O Streams](https://pubs.opengroup.org/onlinepubs/000095399/functions/xsh_chap02_05.html)
- [12.20.3 Controlling Which Kind of Buffering](http://www.gnu.org/software/libc/manual/html_node/Controlling-Buffering.html)
