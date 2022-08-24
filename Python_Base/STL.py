
# 标准库
# 开箱即用
# sys模块,提供了一些变量和函数,是我们可以获取到python解析器的信息
# 或者通过函数操作python解析器
# 引入sys模块
# import pprint
# import sys
# # print(sys)
# # sys.argv
# # 获取执行代码时,命令行中所包含的参数
# # 是一个列表,列表中保存了当前命令的所有参数
# # print(sys.argv)
#
#
# # sys.modules
# # 获取当前程序中引入的所有模块
# # modules是一个字典,key是模块的名字,value是模块的对象
# print(sys.modules)
#
# # pprint模块提供了一个方法pprint() 对打印的数据进行简单的格式化
# pprint.pprint(sys.modules)
#
# # sys.path
# #
# pprint.pprint(sys.path)
#
# # sys.platform
# # 表示当前python运行的平台
#
# print(sys.platform)
#
# # sys.exit()
# # 退出程序
# sys.exit()

# os模块让我们可以对操作系统进行访问
import os

# os.environ
# 可以获取到系统的环境变量path
import pprint
pprint.pprint(os.environ['path'])

# os.system()
# 可以用来执行操作系统的名字
os.system('notepad')