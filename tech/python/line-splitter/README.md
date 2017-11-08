2017年11月7日15:46:02

## 需求背景

当前多个Cell的日志均打印在相同日志文件中，这对于分析每个独立Cell的日志带来了不小的干扰，
所以想着可以使用Python写作一个简单的脚本，通过命令行提取出各个Cell的日志。

## 简单设想

目前的设想有下面功能：

- 指定`分析的文件名`、`匹配的关键字`，然后依据匹配的关键字分别生成存放过滤行的文件。
- 同时支持多个`匹配的关键字`。
- `匹配的关键字`可以支持“与”/“或”，即任一匹配或者全匹配。

使用Python写起来果然比较简单，使用搜索引擎很方便的搞定。

```
from sys import argv

script_name, file_name, key_word1, key_word2 = argv

print ("Script Name:         %s" % script_name)
print ("File to be splitted: %s" % file_name)
print ("key_word1:            %s" % key_word1)
print ("key_word2:            %s" % key_word2)

def main():
    output_filename = file_name + "-" + key_word1 + "-" + key_word2
    output_fp = open(output_filename, 'w')

    with open(file_name) as input_content:
        for line in input_content:
            if key_word1 in line or key_word2 in line:
                print (line)
                output_fp.write(line)

    output_fp.close()

main()
```
