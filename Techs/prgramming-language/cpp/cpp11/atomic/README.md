## atomic

要理解atomic需要先理解[Strong Memory Models](https://preshing.com/20120930/weak-vs-strong-memory-models/)的如下定义，其实也就是atomic操作就是某个操作同时具有“获取/释放”的语义，也就是同一个时间只有一个CPU/线程/进程在操作它。

> A strong hardware memory model is one in which every machine instruction comes implicitly with acquire and release semantics. As a result, when one CPU core performs a sequence of writes, every other CPU core sees those values change in the same order that they were written.

基本数据类型的读写本身不具备原子性，而使用互斥量进行读写效率又不是很高，所以提供了std::atomic的模板来优化多线程场景的互斥操作。

参考：

- [What exactly is std::atomic?](https://stackoverflow.com/questions/31978324/what-exactly-is-stdatomic)
