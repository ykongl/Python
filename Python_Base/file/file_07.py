
# 二进制文件

file_name = 'resource/57851069.jpg'

# t 读取文本文件（默认值）
# b 读取二进制文件

with open(file_name,'rb') as file_obj:
    # 读取文本文件时，size是以字符为单位
    # 读取二进制文件时，size是以字节为单位
    # print(file_obj.read(100))
    new_name = 'resource/155.jpg'
    # 将读取到的内容写出来
    # 定义一个新的文件


    with open(new_name,'wb') as new_obj:
        # 定义每次读取的大小
        chunk = 1024 * 100

        # 从已有的对象中读取数据
        c = file_obj.read(chunk)

        # 将读取到的数据写入到新对象中
        new_obj.write(c)