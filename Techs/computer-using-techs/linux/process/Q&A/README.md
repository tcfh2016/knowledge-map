
## crontab配置了多个任务，但只执行第一个

有一次碰到一个问题，在服务器上配置了3个分别在23:59, 11:59和12:59执行的任务，但是发现只正常执行了第一个，后面两个都没有执行。查看`/var/log/cron`有如下信息，也就是可以看到后面两个任务没有执行是因为权限不够。

```
Aug  4 23:59:02 server-name CROND[41658]: (username) CMD (export DISPLAY=:1 && sh /home/username/auto-scripts/run1.sh)
Aug  5 11:59:01 server-name crond[35211]: (username) PAM ERROR (Authentication service cannot retrieve authentication info)
Aug  5 11:59:01 server-name crond[35211]: (username) FAILED to authorize user with PAM (Authentication service cannot retrieve authentication info)
Aug  5 12:59:01 server-name crond[43819]: (username) PAM ERROR (Authentication service cannot retrieve authentication info)
Aug  5 12:59:01 server-name crond[43819]: (username) FAILED to authorize user with PAM (Authentication service cannot retrieve authentication info)
```

前面刚碰到了“are not allowed to access to (crontab) because of pam configuration”，添加权限后又碰到“Authentication service cannot retrieve authentication info”。

在[CRON Jobs Fail To Run w/PAM Error](http://www.whitemiceconsulting.com/crondpamerror)提到是在`/etc/shadow`没有用户的记录，而又是和`/etc/passwd`对应的。然后我看了下`/etc/passwd`


## 使用crontab的使用提示“are not allowed to access to (crontab) because of pam configuration”

原因在于没有权限。需要编辑`/etc/security/access.conf`配置特定权限，比如添加`+: coins : cron crond :0`。


参考：

- [How to fix a crontab access issue with a pam configuration error message?](https://serverfault.com/questions/620157/how-to-fix-a-crontab-access-issue-with-a-pam-configuration-error-message)
