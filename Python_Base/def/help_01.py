# help()是python中的内置函数
# 通过help()函数可以查询python中的函数的用法
# 语法：help(函数对象)
# help(print) 获取print()函数的使用说明

# 文档字符串(doc str)
# 函数的第一行写一个字符串就是文档字符串

def fn(a, b, c):
    ...
    '这是一个文档字符串'
    ...

    return 10


help(fn)
