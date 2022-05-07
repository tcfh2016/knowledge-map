## 发送文本

`email.message`这个模块里面的核心类是[EmailMessage](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage)。那这个`EmailMessage`又是什么呢？其实这个对象提供了一些函数可以直接添加多种类型的内容，而不用像老的API那样组装邮件内容时需要先创建`MIMEText`, `MIMEImage`或者其他的对象。比如下面是一个发送邮件正文为纯文本的例子：

```
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['From'] = '你的163邮箱地址'
msg['To'] = '接收者邮箱地址'
msg['Subject'] = 'Hello world'
msg.set_content("There you are!")

mail_server = smtplib.SMTP_SSL('smtp.163.com',port=465)
mail_server.login('你的163邮箱账号', '你的SMTP授权码')
mail_server.send_message(msg)
```

测试成功之后我决定尝试着发送html网页，于是我先创建了一个最简单的html网页，名称为`display.html`，然后尝试将它的内容读出来再调用`set_content`填充到msg里面，最后发送出去。

```
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['From'] = '你的163邮箱地址'
msg['To'] = '接收者邮箱地址'
msg['Subject'] = 'Hello world'
msg.set_content("There you are!")

mail_server = smtplib.SMTP_SSL('smtp.163.com',port=465)
mail_server.login('你的163邮箱账号', '你的SMTP授权码')
with open("display.html") as f:
    msg.set_content(f.read())
mail_server.send_message(msg)
```

我看到的内容并不是展示出来的html内容，而全是代码。问题出在哪里？在网络上进行查找对比之后是因为在`set_context()`的时候没有设置内容格式因此默认当作纯文本格式了，只需要设置`msg.set_content(f.read(), 'html')`就可以。在官方文档[email: Examples](https://docs.python.org/3/library/email.examples.html)的一个例子里面，使用`msg.add_attachment(f.read(), subtype='html')`也是可以成功的。


## 发送图片

[EmailMessage](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage)是在新版本的Python（3.6）引入的，以便通过统一接口来操作各种MIME type。前面我们提到了发送文本的做法，那么发送图片如何处理呢？

在之前的版本里面发送图片需要手动创建`MIMEMultipart`做为邮件的主体对象，然后创建`MIMEText`和`MIMEImage`分别将文本对象和图片对象组合到主体对象中。如果直接使用`EmailMessage`就不需要这么麻烦了，直接调用`add_attachment()`进行添加即可。

```
msg = MIMEMultipart()
content = MIMEText(html, _subtype='html', _charset='utf8')
msg.attach(content)
for id, pic in picture.items():
    img = MIMEImage(open(pic, 'rb').read(), _subtype='octet-stream')
    img.add_header('Content-ID', id)
    msg.attach(img)

msg = EmailMessage()
msg.add_attachment(html, subtype='html')
for id, pic in picture.items():
    msg.add_attachment(open(pic, 'rb').read(), maintype='image', subtype='png',cid=id)
```

另外一个知识点，从廖雪峰的[SMTP发送邮件](https://www.liaoxuefeng.com/wiki/1016959663602400/1017790702398272#0)才搞明白`add_alternative()`实际上添加的是一个备选项，比如下面这段代码的意思是先用`set_content()`将邮件正文设置为“text里面的内容”，这种是纯文本；同时也用`add_alternative()`添加一种备选的html格式的正文，如果接收者的邮箱支持html那么默认按照html格式展示html_content，如果不支持那么以纯文本展示text包含的纯文本内容。也就是这添加的两种内容仅仅只会展示一种。

```
msg = EmailMessage()
msg.set_content(text)
msg.add_alternative(html_content, subtype='html')
```
