
# 文件
# I/O (input/Output)
# 打开
# 如果目标文件和当前文件在同一级目录下,直接使用文件名(路径)
# windows系统使用路径时,可以使用/代替\
# 或者用\\代替\
# 或者使用原始字符串
# filename = r'123.txt'
# file_name = '123.txt'
# file_obj = open(file_name)
#
# # 读取文件内容
# # read(),读取文件中内容,将内容存为字符串返回
# content = file_obj.read()
# print(content)
#
# # 关闭文件
# # close()
# file_obj.close()


# # with...as 语句
# with open(file_name) as file_obj:
#     # 在with语句中可以直接使用file_obj来做文件操作
#     # 此时这个文件只能在with中使用,一旦with结束则文件会自动close()
#     print(file_obj.read())

file_name = 'resource/123.txt'

try:
    with open(file_name) as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print('文件不存在')
else:
    print('文件存在!')