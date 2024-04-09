## 使用`post`方式获取数据



餐考：

- [11. requests.post()函数访问网页(小白入门)](https://zhuanlan.zhihu.com/p/639765581)

## 登录验证

使用`requests`去登录网站，首先要获取POST请求提交的URL以及填写用户名和密码对应的属性。

```
import requests

# Fill in your details here to be posted to the login form.
payload = {
    'inUserName': 'username',
    'inUserPass': 'password'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('LOGIN_URL', data=payload)
    # print the HTML returned or something more intelligent to see if it's a successful login page.
    print(p.text)

    # An authorised request.
    r = s.get('A protected web page URL')
    print(r.text)
        # etc...
```

参考

- [How to "log in" to a website using Python's Requests module?](https://stackoverflow.com/questions/11892729/how-to-log-in-to-a-website-using-pythons-requests-module)