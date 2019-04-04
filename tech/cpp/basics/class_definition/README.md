## error: member access into incomplete type

- [https://stackoverflow.com/questions/19962812/error-member-access-into-incomplete-type-forward-declaration-of](https://stackoverflow.com/questions/19962812/error-member-access-into-incomplete-type-forward-declaration-of)

## 类定义里面无法创建对象进行初始化

好久没写代码，秀逗了。

```
class Mocker
{
  Mocker(int i)  {}
  ~Mocker()  {}
  ...
}

class Container
{
  Mocker mocker(1);
}
```

正确写法：

```
class Mocker
{
  Mocker(int i)  {}
  ~Mocker()  {}
  ...
}

class Container
{
  Container():mocker(1){}

  Mocker mocker;
}
```
