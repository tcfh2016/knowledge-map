## ZipFile 

```
import os
import zipfile

working_folder = 'C:\\path_to_some_folder\\'
files = os.listdir(working_folder)
files_py = files

ZipFile = zipfile.ZipFile("zip testing3.zip", "a" )

for a in files_py:
    ZipFile.write(os.path.basename(a), compress_type=zipfile.ZIP_DEFLATED)
ZipFile.close()
```

参考：

- [zip a list of files and attach in email - python](https://stackoverflow.com/questions/41564425/zip-a-list-of-files-and-attach-in-email-python?rq=3)


## 压缩整个文件夹

需要一个一个添加：

```
import os, zipfile

name = 'DirToZip'
zip_name = name + '.zip'

with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
    for folder_name, subfolders, filenames in os.walk(name):
        for filename in filenames:
            file_path = os.path.join(folder_name, filename)
            zip_ref.write(file_path)

zip_ref.close()
```

*如果不给定`zipfile.ZIP_DEFLATED`那么仅仅打包，不会进行压缩。*

参考：

- [How to create a zip archive of a directory?](https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory)


## 压缩时的目录结构


- [zip file and avoid directory structure](https://stackoverflow.com/questions/27991745/zip-file-and-avoid-directory-structure)
- [Create zip from directory using Python](https://stackoverflow.com/questions/58955341/create-zip-from-directory-using-python)