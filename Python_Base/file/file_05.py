
# 文件_readline
import pprint

file_name = 'resource/123.txt'

with open(file_name,encoding='utf-8') as file_obj:
    # print(file_obj.read())
    # readline可以读取一行内容
    # print(file_obj.readline(),end='')
    # print(file_obj.readline(),end='')
    # print(file_obj.readline())
    # readlines()
    # 该方法用于一行一行的读取内容,一次性的将内容封装到一个列表中返回
    # r = file_obj.readlines()
    # pprint.pprint(r)
    for i in file_obj:
        print(i,end='')

