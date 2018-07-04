# 单元测试

当一个功能日趋复杂的时候，就开始感觉到单元测试的重要了。两个方面：

- 对子功能进行测试，有利于发现和解决问题。
- 为之后的维护建设保护墙。
- 采用测试驱动的方式可以将代码写得更整洁。

# 简单示例

由于 python内建单元测试模块，因此测试用例的写作很简单，只需要创建测试文件并将测试模块导
入进来即可，可以使用的测试断言有好几种：

- assertEqual(a, b)
- assertNotEqual(a, b)
- assertTrue(x)
- assertFalse(x)

python 3.1版本新增如下几种断言：

- assertIs(a, b)
- assertIsNot(a, b)
- assertIsNone(x)
- assertIsNotNone(x)
- assertIn(a, b)
- assertNotIn(a, b)
- assertIsInstance(a, b)
- assertNotIsInstance(a, b)

primes.py

```
def is_prime(number):    
    if number <= 1:
        return False

    for element in range(2, number):
        if number % element == 0:
            return False

    return True
```

test_primes.py

```
import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
    unittest.main()
```

执行`python test_primes.py`进行测试，可添加`-v`参数在执行时打印更多信息。


# 跨目录测试

当前学会了单个文件的测试，但是通过什么方式将多个测试文件连接起来呢？

在读了[Python Unit Testing – Structuring Your Project](http://www.patricksoftwareblog.com/python-unit-testing-structuring-your-project/)之后，发现对于跨目录的单元测试可以进行如下组织：

- 在src, tst目录均创建__init__.py文件。
- 在src, tst的公共目录执行`python -m unittest discover -v`。
- import跨目录的模块进行测试的时候通过顶层目录结合"."逐级向下引用，比如'src.metadata_handler'。

原来在src和tst目录都放入 __init__.py之后，即便这两个文件是空的，python解析器便将它们识
别为 `containing packages`，即包目录，意味着它里面可以包含其他模块，在执行搜索的时候会
进一步搜索该目录下的所有文件。

# 参考链接

- [Improve Your Python: Understanding Unit Testing](https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/)
- [unittest introduction](http://pythontesting.net/framework/unittest/unittest-introduction/)
- [assert-methods](https://docs.python.org/3/library/unittest.html#assert-methods)
- [Python Unit Testing – Structuring Your Project](http://www.patricksoftwareblog.com/python-unit-testing-structuring-your-project/)
- [What is __init__.py for?](https://stackoverflow.com/questions/448271/what-is-init-py-for)
