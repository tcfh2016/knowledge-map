# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()

# 添加positional参数，解析之后的结果即为该值。
parser.add_argument("echo", help="echo the string you use here.")
parser.add_argument("square", help="display a square of a given number.", type=int)

# 添加optional参数，必须指定value，解析之后的结果为value的值。
parser.add_argument("--verbosity", help="increase output verbosity.")
# '-v'的指定的action为“store_true”，所以当指定-v的时候，args.verbose的值为True。
parser.add_argument("-v", "--verbose", help="increase output verbosity.", action="store_true")


args = parser.parse_args()

print (args.echo)
print (args.square**2)

if args.verbosity:
    print (args.verbosity)
if args.verbose:
    print (args.verbose)

# 1. -h --help 是argparse默认提供的optinal argument。
# 2. 通过在add_argument设定参数名称中包括"-"/"--"字符，该参数自动转换为optional类型。
# 3. 在使用optinal参数的时候，必须指定value。
# 4. positional/optional参数的顺序可以互换。
