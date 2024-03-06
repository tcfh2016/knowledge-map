## configparser

在一些大型项目里面通常需要将一些配置进行集中式管理，Python中的`configparser`就是用来做这件事情的。


## 读取配置

```
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

value = config.get('section_name', 'option_name')
#value = config['section_name']['option_name']
```

*注1：不能通过`config=configparser.ConfigParser().read('config.ini')`读取，然后通过`config`去访问。*
*注2：获取到的值是字符串形式，如果想用列表*

## 更新配置

```
config.set('section_name', 'option_name', 'new_value')

with open('config.ini', 'w') as configfile:
  config.write(configfile)
```


参考：

- [Managing Configuration Files in Python: A Comprehensive Guide to Reading, Writing, and Updating config.ini Files](https://www.linkedin.com/pulse/managing-configuration-files-python-comprehensive-guide-niwate/)