## 问题

### 443错误

最近几天突然碰到push的时候无法成功，有如下提示：

```
$ git push origin master
fatal: unable to access 'https://github.com/tcfh2016/knowledge-map.git/': OpenSSL SSL_connect: Connection was reset in connection to github.com:443
```

搜索了许久，把网络上介绍的如下方案都尝试过了：

- 网络问题, ping不同（我的可以）
- ssh或端口问题，提示权限不允许（添加了公钥，依然不工作）
- 证书问题，对比~/.ssh/known_hosts的`主机名 ip地址`是否与ping结果一致，不一致删除（依然不成功）

最后是在[这里](https://jasonkayzk.github.io/2019/10/10/%E5%85%B3%E4%BA%8E%E4%BD%BF%E7%94%A8Git%E6%97%B6push-pull%E8%B6%85%E6%97%B6-%E4%BB%A5%E5%8F%8AGithub%E8%AE%BF%E9%97%AE%E6%85%A2%E7%9A%84%E8%A7%A3%E5%86%B3%E5%8A%9E%E6%B3%95/)提供的加速国内github访问，手动调整了域名解析IP地址才成功。
