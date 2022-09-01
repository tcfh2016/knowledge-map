## READ JSON

大数据很多时候都以JSON格式存储，JSON格式也是纯文本的，但是它能够按照编程世界中“对象”的形式进行存储。

可以使用`read_json()`函数来读取JSON文件。JSON对象和Python中的字典拥有相同的格式，如果你已经将JSON对象保存在字典变量，比如`dict_data`里面，你可以直接使用`pd.DataFrame(dict_data)`来读取它。
