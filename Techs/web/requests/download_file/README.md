## 下载文件

之前以为在Linux下面使用`curl`下载文件快，在python里面使用`requests`慢。但是按照[Download large file in python with requests](https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests)里面的方法尝试，结果并非如此。

1）方法一：使用`curl`

使用`curl url -o filename --progress`命令来下载，可以看到进度，测量时间为：。


2）方法二：使用`requests`

代码如下。测量时间为：。

```
import requests
import shutil

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename
```
