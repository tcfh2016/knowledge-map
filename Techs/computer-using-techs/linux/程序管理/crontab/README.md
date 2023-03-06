## crontab

`cron`是linux系统里面的任务调度器，可以用来创建一些周期性执行的任务。在linux系统里面由`crond`这个服务来负责这些例程工作。这个服务即负责系统本身的例行性工作，也可以提供用户添加新的例行性工作（通过`crontab`命令）。

由于安全考虑，系统提供了`/etc/cron.allow`和`/etc/cron.deny`两个名单来提供对于用户的控制，只需要在其中添加用户名就可以允许或者拒绝对应用户使用crond服务。不同的用户使用了crontab之后该用户的执行任务都记录到`/var/spool/cron/username`里面，而crond服务执行的每项工作会记录到`/var/log/cron`里面。


## 开始之前

在设置任务之前我们需要先确保`crond`这个服务是否已经开启，这个时候可以通过`systemctl status crond`命令来查看服务的状态，当然还可以通过`systemctl enable crond`/`systemctl restart crond`来开启或者重启该项服务。

```
[lianb]$ systemctl status crond
● crond.service - Command Scheduler
   Loaded: loaded (/usr/lib/systemd/system/crond.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2021-08-06 08:10:28 CST; 2 weeks 0 days ago
 Main PID: 2207 (crond)
   CGroup: /system.slice/crond.service
           └─2207 /usr/sbin/crond -n
[lianb]$

```


## 设置任务

`crontab`的语法为`crontab [-u username] [-l|-e|-r]`，对应参数：

- `-u` ：用来帮其他用户建立/移除crontab任务，仅root可用
- `-e` ：编辑crontab的工作内容
- `-l` ：查阅crontab的工作内容
- `-r` ：移除所有的crontab内容，移除一项通过`-e`去编辑

`crontab -e`这个命令是针对用户设计的，它编辑的执行文件在`/usr/bin/crontab`，同时为每位用户创建对应的文件放在`/var/spool/cron`。而linux系统里面的系统性例行性工作对应的执行文件在`/etc/crontab`，系统默认每分钟去读取`/etc/crontab`和`/var/spool/cron`里面文件内容。

添加`#`进行注释。


## 查看日志

crontab的相关日志有两份：1）针对每位用户会创建一个日志，存在于`/var/spool/mail`或者`/var/mail`。2）然后在`/var/log/cron`有cron本身的执行日志。


当这个文件满了怎么办？

对于`/var`目录的一些文件无法删除，比如这个目录下面有账户对应的`/var/spool/mail/lianb`，没用办法使用`rm`去删除，但可以使用`> /var/spool/mail/lianb`将其清空。


参考：

- [第十五章、例行性工作排程(crontab)](http://linux.vbird.org/linux_basic/0430cron.php)
- [How to enable logging for cron on Linux](https://www.techrepublic.com/article/how-to-enable-logging-for-cron-on-linux/)


## 配置了任务但是没有执行

调试脚本的时候设定了：

```

```

查看cron的日志`/var/log/cron`发现对应的时间点第2项任务没有执行起来

```
# 这个run1.sh是能够正常运行的。
Mar  6 05:59:02 yang-jinyong-dev-rhel7 CROND[44718]: (lianbche) CMD (export DISPLAY=:7 && sh /home/lianbche/auto-scripts/CI_SCT/run1.sh)

# 但这个run2.sh没有运行起来。
Mar  6 06:59:01 yang-jinyong-dev-rhel7 crond[10247]: (lianbche) PAM ERROR (Authentication service cannot retrieve authentication info)
Mar  6 06:59:01 yang-jinyong-dev-rhel7 crond[10247]: (lianbche) FAILED to authorize user with PAM (Authentication service cannot retrieve authentication info)
```

参考：

- [CRON Jobs Fail To Run w/PAM Error](http://www.whitemiceconsulting.com/crondpamerror)