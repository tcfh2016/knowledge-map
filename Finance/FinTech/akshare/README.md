# 使用

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

# 问题

## `ak.stock_individual_info_em(symbol="000001")`

从2025-02-14开始脚本执行出错，提示“KeyError: '000001'”，查看服务器上akshare版本为“1.15.10”，本地版本为“1.14.86”也有同样的问题。可能是因为升级之后接口变了。

执行`pip install akshare --upgrade -i https://pypi.org/simple`升级到“1.16.9”之后修复了。

## `index_value_hist_funddb()`移除

后面在仓库里面发现韭圈儿的估值接口已经移除：

- [最新版本，index_value_hist_funddb()这个接口去掉了，希望能恢复](https://github.com/akfamily/akshare/issues/5484)
