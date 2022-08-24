
# 包Package
# 包也是一个模块
# 普通模块是一个.py文件,包是一个文件夹
# 包必须要一个__init__.py 这个文件,这个文件中可以包含包中的主要内容

from util import test1,test2
print(test1.b)
print(test2.a)


# __pycache__是模块的缓存文件,提高程序运行的性能

