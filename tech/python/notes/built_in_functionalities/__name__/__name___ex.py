# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print('This program is being run by itself. %s' % __name__)
else:
    print('I am being imported from another module. %s' % __name__)

# 当作为单独程序执行时，__name__设置为__main__。
#> python __name__.py
#This program is being run by itself. __main__

# 当作为模块被import时，__name__设置为自身的模块名称。
#>>> import __name__
#I am being imported from another module. __name___ex

# 注：当在源代码文件里面添加注释的时候需要在最前方指定编码格式，否则则会提示：
#> python __name___ex.py
#  File "__name___ex.py", line 6
#SyntaxError: Non-ASCII character '\xe5' in file __name___ex.py on line 6, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
