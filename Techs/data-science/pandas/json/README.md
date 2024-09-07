## json_normalize()

嵌套定义的JSON格式数据，可以通过`pandas.json_normalize()`将其转化为二维码结构，便于分析和处理。

- `record_path`，这个参数可以用来将指定列的数据转换为二维表。 

```
pd.json_normalize(json_data)
pd.json_normalize(d,record_path='table_ori')
```

参考：

- [How to Normalize semi-structured JSON data into a flat table?](https://www.askpython.com/python-modules/pandas/normalize-json-flat-table)