# -*- coding: utf-8 -*-
# 在之前的学习中已经学习过有关print的几种方式，如今看到更为强大的format函数，因此再为之
# 记。

# I。简单的打印：使用转换说明符
my_name   = "lianbche"
my_age    = 18
my_weight = 63.1

print "name=%s age=%d weight=%.2f" % (my_name, my_age, my_weight)
# 输出：
# > python print_ex.py
# name=lianbche age=18 weight=63.10

# 2. 打印时候的格式控制，包括：
#   - 连接两行的print输出。
#   - 通过 “““ 来定义跨行的字符串。
print "this is the frist line",
print "yes, we are at the same line"

print """
    author: lianbche
    license: un-known
"""
# 输出：
# this is the frist line yes, we are at the same line
#
#     author: lianbche
#     license: un-known


# 3. 格式字符串的使用，比较灵活，常见的有：
# 'my {pet} was {age} years old.'.format (pet='dog', age=2)
# 'my {pet} was {age:.2f} years old.'.format (pet='dog', age=2)
# 'my {pet} was {age:.{d}f} years old.'.format (pet='dog', age=2, d=3)
# 'my {0} was {1} years old.'.format ('dog', 2)
print 'my {pet} was {age} years old.'.format (pet='dog', age=2)
print 'my {pet} was {age:.2f} years old.'.format (pet='dog', age=2)
print 'my {pet} was {age:.{d}f} years old.'.format (pet='dog', age=2, d=3)
print 'my {0} was {1} years old.'.format ('dog', 2)

 print "%14s %14.3f %14.3f" % ('size', sta1[0], sta2[0]
