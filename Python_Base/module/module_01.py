
# 模块化.将完整的程序分解为一个一个小模块
# 模块化优点:
#  1.方便开发
#  2.方便维护
#  3.模块可复用!

# 在一个模块中引入外部模块
# 1.import 模块名
# 2.import 模块名 as 别名
# 可以通过__name__属性获取到模块的名字
# __name__属性值为__main__的模块是主模块，一个程序中只会有一个主模块
# import module_test as m1

# print(m1)
# print(__name__)
# print(m1.__name__)

# print(m1.a + m1.b)
#
# m1.test()
# m1.test2()

# 引入模块中的部分内容
# 语法 from 模块名 import 变量....
# from 模块名 import* 引入模块所有变量
# from module_test import test
# test()


# 引入的变量设置别名
# from module_test import test as t
# t()

import module_test
