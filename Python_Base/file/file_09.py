
# 文件其他操作

import os
from pprint import pprint

# 获取当前目录结构
# 路径作为参数，获取路径下的目录结构，返回一个列表
r = os.listdir('..')

# os.getcwd() 获取当前所在目录
s = os.getcwd()

# os.chdir() 切换当前所在的目录,
os.chdir('..')
t = os.getcwd()
pprint(t)

# 创建目录
# 在当前创建一个名字为aaa的目录
# os.mkdir('aaa')

# 删除目录
# os.rmdir('aaa')


# open('aa.txt','w')
# 删除文件
# os.remove('bb.txt')

# os.rename('旧命名','新命名')

# os.rename('aa.txt','bb.txt')

