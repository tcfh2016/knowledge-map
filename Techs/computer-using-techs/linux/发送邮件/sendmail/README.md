## sendmail

正常情况下可以使用Python生成.html，然后使用`/usr/sbin/sendmail -t < generated.html`来发送html，但如果这个时候我需要添加一个附件呢？

两个基本概念需要知道：

1. sendmail的角色

首先有个概念需要明确，这个概念在[How can I add an attachment with Sendmail (limited options)?](https://unix.stackexchange.com/questions/409523/how-can-i-add-an-attachment-with-sendmail-limited-options)里面提到：

> sendmail is not the program to use to create the email, you need something else like mail or mutt to format the email correctly (including encoding the attachment in it) before feeding it to sendmail for delivery. They serve difference purposes: sendmail is an MTA to Transmit emails where mail/mutt are MUAs, that is Mail User Agent to build or view emails. –
Patrick Mevzek

简单来说，使用`sendmail`来发送邮件，你需要首先将邮件组织好。

2. mail的结构

特别需要知道如果需要发送带有附件的邮件，那么这种邮件的格式需要是`multipart/mixed`。


## 添加简单的csv

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
