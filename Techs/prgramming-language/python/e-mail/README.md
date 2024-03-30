## 添加bookmarks

在outlook里面测试，发现无法支持`id`属性建立的跳转关系，只能使用命名锚点`a`。

参考：

- [Create a bookmark for a section in an HTML paste email](https://help.salesforce.com/s/articleView?id=000338370&type=1)


## 查看smtp服务器最大邮件size

```
import smtplib    
smtp = smtplib.SMTP('server.name')    
smtp.ehlo()    
max_limit_in_bytes = int( smtp.esmtp_features['size'] )
```

参考：

- [Change/Set maximum message size for Python smtplib](https://stackoverflow.com/questions/45409799/change-set-maximum-message-size-for-python-smtplib)


## '5.3.4 Message size exceeds fixed limit'

邮件超大的问题有点奇怪，因为我的附件才7M，通过打印出当前服务器的最大size为10M，但依然有这个问题。

