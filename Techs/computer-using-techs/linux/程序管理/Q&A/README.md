## 使用crontab的使用提示“are not allowed to access to (crontab) because of pam configuration”

原因在于没有权限。需要编辑`/etc/security/access.conf`配置特定权限，比如添加`+: coins : cron crond :0`。


参考：

- [How to fix a crontab access issue with a pam configuration error message?](https://serverfault.com/questions/620157/how-to-fix-a-crontab-access-issue-with-a-pam-configuration-error-message)
