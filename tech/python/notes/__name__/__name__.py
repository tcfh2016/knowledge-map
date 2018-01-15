if __name__ == '__main__':
    print('This program is being run by itself. %s' % __name__)
else:
    print('I am being imported from another module. %s' % __name__)

# 当作为单独程序执行时，__name__设置为__main__。
#> python __name__.py
#This program is being run by itself. __main__

# 当作为模块被import时，__name__设置为自身的模块名称。
#>>> import __name__
#I am being imported from another module. __name__
