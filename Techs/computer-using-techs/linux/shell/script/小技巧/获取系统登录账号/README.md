
## 一次读取文件

```
  #!/bin/bash
  
  users=$(cut -d ':' -f1 /etc/passwd)
  for username in $users; do
    echo $username
  done
```

## 逐步读取文件

```
#!/bin/bash
while read line; do
    IFS=':' read -ra account_info <<< $line
    username=${account_info[0]}
    echo $username
done < /etc/passwd
```