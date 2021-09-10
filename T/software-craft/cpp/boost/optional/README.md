## [boost::optional](https://www.boost.org/doc/libs/1_77_0/libs/optional/doc/html/index.html)

`optional`是一个类模板，主要使用在可选的场景，“可选”表示在一些情况下对应的变量具有正常情况下完全不一样的语义。比如定义了要获取一个最大值的函数（返回值为int），但某些情况下可能不满足求最大值的条件，此时调用者没有办法处理这种情况。这个时候需要返回的是“一种不成功的状态”，而非某个int值，因为此时你返回的任何一个int值都可能是有效值。

比如，下面的例子来将字符串转换为int类型的值*其中的boost::none就是未初始化的optional对象*：

```
boost::optional<int> convert(const std::string& text)
{
  std::stringstream s(text);
  int i;
  if ((s >> i) && s.get() == std::char_traits<char>::eof())
    return i;
  else
    return boost::none;
}
```

除了上面返回`boost::none`之外，还能够直接使用未初始化的值，比如`boost::optional<int> result`。


### 使用

奇怪下面第一句不能用`if (convert(text))`替换？ 测试了一下是可以的，之所以这样写是为了方便在条件分支里面获取到oi的值。

```
if (boost::optional<int> oi = convert(text))
{
  int i = *oi;
}
else
{
  // no valid value
}
```

如果用类型A实例化了`optional`类，此时要获取类型A的值需要通过如上的`*oi`，但通过`*`/`->`去抽取值的时候必须保证其中已经包含了有效值，否则行为是未定义的。

### 取值

有下面几种使用方法：

```
// 最简单的使用方法，通过星号来萃取值，前提是确保能获得有效值。
int i = *convert("100");

// 使用.value()接口 + 异常处理（无效时抛出异常）
try {
  int j = convert(text).value();
}
catch (const boost::bad_optional_access&) {
  ...
}

// 添加返回默认值
int k = convert(text).value_or(0);

// 添加默认回调
int fallback_to_default()
{
  cerr << "could not convert; using -1 instead" << endl;
  return -1;
}

int l = convert(text).value_or_eval(fallback_to_default);
```
