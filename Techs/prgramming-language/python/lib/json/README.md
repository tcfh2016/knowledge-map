## json



## 将字典转换为json

在使用`json.dumps()`的时候如果不指定`indent=4`参数那么所有记录都在一行，指定之后则会另起一行并缩进，有利于阅读。

```
#方式一：
employee_dict = {'id': '09', 'name': 'Nitin', 'department': 'Finance'}
json_object = json.dumps(employee_dict, indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)   

#方式二：
with open("sample.json", "w") as outfile:     
    json.dump(dictionary, outfile)    
```



## 读取json文件

读取出来默认是`dict`类型：

```
with open('sample.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
```

文件为空的时候不能读取。

参考：

- [Python JSON](https://www.geeksforgeeks.org/python-json/)
