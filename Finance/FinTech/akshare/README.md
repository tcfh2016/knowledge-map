## 安装

```
# 安装
pip install akshare --upgrade

# 升级
pip install akshare --upgrade -i https://pypi.org/simple
```

参考：

- [AKShare 安装指导](https://akshare.akfamily.xyz/installation.html)

## 查看版本

```
import akshare as ak

ak.__version__
```

## 问题

1. 升级问题

在Windows下面执行`pip install akshare --upgrade -i https://pypi.org/simple`升级碰到下面错误：

```
Installing collected packages: mini-racer, akshare
ERROR: Could not install packages due to an OSError: [WinError 5] 拒绝访问。: 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\py_mini_racer\\mini_racer.dll'
Consider using the `--user` option or check the permissions.
```

问了ds，`pip install --user akshare --upgrade -i https://pypi.org/simple`解决问题。