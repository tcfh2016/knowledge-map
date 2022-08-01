## 什么是sendmail

`sendmail`是一种MTA，可以理解为邮件服务器程序，一些细节可以参考[这里](../README.md)。

在[How can I add an attachment with Sendmail (limited options)?](https://unix.stackexchange.com/questions/409523/how-can-i-add-an-attachment-with-sendmail-limited-options)里面提到：

> sendmail is not the program to use to create the email, you need something else like mail or mutt to format the email correctly (including encoding the attachment in it) before feeding it to sendmail for delivery. They serve difference purposes: sendmail is an MTA to Transmit emails where mail/mutt are MUAs, that is Mail User Agent to build or view emails. –
Patrick Mevzek

简单来说，使用`sendmail`来发送邮件，你需要首先将邮件组织好。那么邮件的组织通常对应着两种情况：

1）将邮件标题、邮件正文编写在同一个文件，使用`/usr/sbin/sendmail -t < generated.html`直接发送。
2）将邮件标题和邮件正文分开，在发送的时候再进行组装。这种情况常见于需要给邮件添加附件的情况。

## sendmail的简单用法

```
#!/usr/bin/ksh

export MAILTO="xxx"
export SUBJECT="Mail Subject"
export BODY="/tmp/email_body.html"
(
 echo "To: $MAILTO"
 echo "Subject: $SUBJECT"
 echo "MIME-Version: 1.0"
 echo "Content-Type: text/html"
 echo "Content-Disposition: inline"
 cat $BODY
) | /usr/sbin/sendmail $MAILTO
```

## 添加简单的csv

正常情况下可以使用Python生成.html，然后使用`/usr/sbin/sendmail -t < generated.html`来发送html，但如果这个时候我需要添加一个附件呢？

特别需要知道如果需要发送带有附件的邮件，那么这种邮件的格式(`Content-Type`)需要是`multipart/mixed`。

在调用`sendmail`之前需要首先先完成邮件的组装，比如下面通过shell命令先用已有的html作为邮件的body，同时还需要生成附件（*注：这种附件无法直接attach上来，必须调用其他的命令来完成attach过程*）。

```
#!/usr/bin/ksh

export MAILTO="xxx"
export SUBJECT="Mail Subject"
export BODY="/tmp/email_body.html"
export CSV="attachment.csv"
export DATA=$(cat 'Local.csv')
(
 echo "To: $MAILTO"
 echo "Subject: $SUBJECT"
 echo "MIME-Version: 1.0"
 echo 'Content-Type: multipart/mixed; boundary="-q1w2e3r4t5"'
 echo
 echo '---q1w2e3r4t5'
 echo "Content-Type: text/html"
 echo "Content-Disposition: inline"
 cat $BODY
 echo '---q1w2e3r4t5'
 echo "Content-Type: text/csv;charset=utf-8"
 echo "Content-Disposition: attachement;filename=${CSV}"
 echo "$DATA"
 echo '---q1w2e3r4t5--'
) | /usr/sbin/sendmail $MAILTO
```

也就是邮件里面名称为“attachment.csv”的附件是在上面的shell命令里面通过`echo $DATA`读取本地的Local.csv生成的，而不是直接attach了Local.csv，这一点一定要注意。

uuencode --base64 $ATTACH $(basename $ATTACH)

## 添加zip

在[sendmail with zip is corrupting first file in the zip](https://stackoverflow.com/questions/50272892/sendmail-with-zip-is-corrupting-first-file-in-the-zip)看到了如果要添加zip类型的附件，需要注意指定`Content-Type`为`application/zip`，并且还需要调用`base64`来完成attach的过程。*另外一个要点是在每个邮件的部分需要添加空行来分割，否则附件解压会出错。*

```
export MAILTO="xxx"
export SUBJECT="Mail Subject"
export BODY="/tmp/email_body.html"
export ATTACH="output.zip"
(
 echo "To: $MAILTO"
 echo "Subject: $SUBJECT"
 echo "MIME-Version: 1.0"
 echo 'Content-Type: multipart/mixed; boundary="-q1w2e3r4t5"'
 echo
 echo '---q1w2e3r4t5'
 echo "Content-Type: text/html"
 echo "Content-Disposition: inline"
 cat $BODY
 echo
 echo '---q1w2e3r4t5'
 echo 'Content-Type: application/zip;'
 echo 'Content-Transfer-Encoding: base64'
 echo "Content-Disposition: attachement; filename=${ATTACH}"
 echo ''
 base64 ${ATTACH}
 echo '---q1w2e3r4t5--'
) | /usr/sbin/sendmail -t
```


参考：

- [sendmail with attachments](https://www.unix.com/shell-programming-and-scripting/118534-sendmail-attachments.html)
- [Sendmail Attachment](https://unix.stackexchange.com/questions/223636/sendmail-attachment)

## 收件人列表被截断的问题

我在使用`sendmail`发送邮件的时候，使用`cc="a@BB.com;b@BB.com...`定义了一个比较长的收件人列表，结果邮件发送之后看到收件人的列表被截断了：

- 数了下收件人列表的字符，刚好254个，超过254个字符的其他收件人地址被截掉
- 不过，即便outlook里面没有显示被截断收件人的地址信息，他们仍然收到了邮件

google了许久，对于`254个字符`只找到了RFC里面在定义收件人地址标准时候的一些历史故事，正式的[rfc5321](https://www.rfc-editor.org/rfc/rfc5321#section-4.5.3)里面定义的是64+256=320，但在[3696](https://www.rfc-editor.org/errata_search.php?rfc=3696&eid=1690)又重新定义为254。

但是这个仅仅是单个收件人的长度，不过实际上发现尽管outlook里面显示收件人截取了，实际上被截取的那些收件人也能正常收到邮件，只是outlook上面收件人列表没有展示出来。所以，这个问题应该是outlook在整个收件人列表上应用了254个字符的限制。

在参考文章里面VBA里面，实际上也有这个问题，不过可以通过创建收件人数组的方式来解决。在sendmail上目前没有找到类似的方法。

参考：

- [VBA 调用 Lotus 发送邮件的收件人长度问题](https://zhiqiang.org/coding/lotus-vba-recepient-no-longer-than-256.html)
- [What is the maximum length of a valid email address?](https://stackoverflow.com/questions/386294/what-is-the-maximum-length-of-a-valid-email-address)
