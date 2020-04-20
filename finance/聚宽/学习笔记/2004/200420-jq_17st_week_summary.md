# 聚宽学习周记十六：详解@东南有大树的“指数估值自动报表系统”（下）



## 一、代码解释

```
```


## 三、上周计划任务


### 1. 进一步学习[指数估值自动报表系统——源代码](https://www.joinquant.com/view/community/detail/20497)里面自己不熟悉的知识点，并仿照原有代码改写自动报表系统。


### 2. 在理解函数`send_message()`的时候发现聚宽本身定义了这个函数用来发送微信消息，当前自己在进行ETF定投，都是使用聚源数据提供的指数估值来进行决策，受这篇文章的启发其实可以尝试手动计算当前指数的估值，这样每天就可以实时掌握指数的估值状态了。


## 三、本周新学内容

### 1.使用Python进行邮件发送

Python函数库`smtplib`专门用来支持邮件的发送，这个库是基于SMTP（Simple Mail Transfer Protocol，简单邮件传输协议）的封装，发送邮件的过程我们需要创建对应的[SMTP的对象](https://docs.python.org/3/library/smtplib.html#module-smtplib)，用来创建SMTP对象的类定义有如下两种：

```
class smtplib.SMTP(host='', port=0, local_hostname=None, [timeout, ]source_address=None)

# 与SMTP行为一样，但支持SSL访问
class smtplib.SMTP_SSL(host='', port=0, local_hostname=None, keyfile=None, certfile=None, [timeout, ]context=None, source_address=None)

```

在创建该对象的时候我们需要明确要使用SMTP服务，也就是我们要使用哪里的邮件服务器来发送邮件，比如我现在要使用我已经注册的163邮箱来发送邮件，那么我们这里要先找到163提供了哪些邮件服务，这可以通过在邮箱设置里面查看得到。比如我登录自己邮箱之后可以在【设置】选项里面找到[什么是POP3、SMTP和IMAP?](https://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac22dc0e9af8168582a)，里面包含了163提供的邮件服务：

![](./w17-mail163-service.PNG)

上面就提供了“SMTP服务器地址”，“SSL协议端口号”和“非SSL协议端口号”，我们这个时候想使用支持SSL协议的SMTP服务，那么就可以创建下面的SMTP对象：

```
import smtplib

mail_server = smtplib.SMTP_SSL('smtp.163.com',port=465)
```

在创建好这个对象之后，我们就可以使用SMTP的`sendmail`函数来进行邮件的发送，该函数声明为`SMTP.sendmail(from_addr, to_addrs, msg, mail_options=(), rcpt_options=())`。但在此之前我们要先准备好对应的参数信息：

- from_addr: 发送者邮件地址。我们使用163邮件服务，所以这里填写自己的邮箱账号。
- to_addrs：接收者邮件地址。可以支持多个。
- msg：要发送的消息。

邮件的消息`msg`这个时候是难点，我们无法直接发送字符串，而是需要[email.message](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage)

```
from email.message import EmailMessage

mail_server = smtplib.SMTP_SSL('smtp.163.com',port=465)
mail_server.sendmail('lianbch@163.com', 'lianbche@163.com', "hello")
```


[email.mime](https://docs.python.org/3/library/email.mime.html?highlight=mimetext#email.mime.text.MIMEText)

参考：

- [Python SMTP发送邮件](https://www.runoob.com/python/python-email.html)
- [email — An email and MIME handling package](https://docs.python.org/3/library/email.html)
- [email: Examples](https://docs.python.org/3/library/email.examples.html)

## 四、下周学习任务
