## json

JSON全称为“Java Script Object Notation”，是web应用之间进行数据存储与传输的常见格式。

JSON的格式简单，是以“key-value”形式的对象来存储数据，这些对象使用`{}`包括起来。`value`的格式相比XML来说更少，只支持字符串、数字、布尔型和对象这集中类型。在JSON存储的时候稍复杂点的结果为：

- 嵌套对象，也就是一个`value`包含有多个对象。
- 对象数组，将多个对象存放在`[]`里面，通常作为某个`key`对应的`value`。

常用函数：

- json.load(json_file)
- json.loads(json_string)


参考：

- [How to Best Work with JSON in Python](https://towardsdatascience.com/how-to-best-work-with-json-in-python-2c8989ff0390)


## JSONPath

`JSONPath`是JSON对应的查询语言，类似于XML的`XPath`。一个`JSONPath`表达式（由`$`, `[]`或者`.`组成）可以定位到一个JSON结构中的某个元素或者元素集合。

- $.store.book[0].title
- $['store']['book'][0]['title']
- ['store']['book'][0]['title']

`$`表示根对象/数组，可以忽略。

参考：

- [JSON Tutorial Part-4 | How To Retrieve Data from JSON using JSON Path | JSON Path Expressions](https://www.youtube.com/watch?v=kP73mR9PX6w)


## 读取json文件

读取出来默认是`dict`类型：

```
import json

with open('sample.json', 'r') as openfile:
    # reading file contents and parse it as json format
    json_object = json.load(openfile)
```

*注1：文件为空的时候不能读取。*
*注2：`load()`是从JSON文件读取，`loads()`是从JSON字符串读取，`read_json()`直接将读取的内容转换为DataFrame。*

参考：

- [Python JSON](https://www.geeksforgeeks.org/python-json/)

## 从字符串读取

```
employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'

#convert string to  object
json_object = json.loads(employee_string)
```

参考：

- [](https://www.freecodecamp.org/news/python-json-how-to-convert-a-string-to-json/)

## 访问

读取为字典后就是按照字典的访问方式来访问，对于内嵌的结构需要多访问几层，比如：

```
j['level1_key'][level2_index]['level3_key']
j.get('level1_key').get(level2_index).get('level3_key')
```

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
    json.dump(employee_dict, outfile, indent=2)    
```


## json_normalize

