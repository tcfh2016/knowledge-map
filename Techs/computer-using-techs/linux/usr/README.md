## 用户管理

linux管理用户的时候是按照用户ID来管理的，每个用户都至少有两个ID：UID和GID，前者是用户ID，后者是群组ID。在查看文件拥有者属性的时候就会去找到`etc/passwd`文件找到对应UID的用户名，从而在显示的时候可以看到用户名和群组。

在`etc/passwd`文件里面可以查找到用户相关信息，不过这个文件里面除了新的用户还有不少供系统本身使用的账号，比如bin, daemon, adm等等。里面每行是由“账号名称:口令:UID:GID:信息说明:home目录:SHELL”构成。

```
bin:x:1:1:bin:/bin:/sbin/nologin
```

## 创建用户

用户创建使用`useradd`和`passwd`，理论上使用`uaser add new_user`的时候会默认创建home目录，但也不一定，它依赖于配置文件`/etc/login.defs`。添加后的用户默认被锁定，此时需要用`passwd new_user`设定密码，密码设定是否成功可以查看`/etc/shadow`文件：

```
# 创建前
vb:!!:19005:0:99999:7:::

# 创建后
vb:$5$2N7544pq$at9S4JLRZRep/0yWjtN5kp/yAqqauw5lWxlm4JmZAK5:19005:0:99999:7:::
```

## sudoers

在使用`sudo apt install git-all`安装git的时候，突然提示：

```
lbc is not in the sudoers file.  This incident will be reported.
```

这是因为并非所有人都能够执行`sudo`，而是仅有`/etc/sudoers`内的用户才能够执行这个命令。可以使用`visudo`来给特定账号配置全部或部分的root命令功能。

```
lbc ALL=(ALL) NOPASSWD:ALL
```