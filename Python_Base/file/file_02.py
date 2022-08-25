
# 文件简单读取

file_name = 'resource/123.txt'

# open()打开两种类型文件
# 一种是纯文本文件(使用utf-8等编码编写的文本文件)
# 一种是二进制文件(图片,MP3,ppt等)
# open()打开文件时,默认是以文本文件的形式打开的,但是open()默认的编码为None
# 处理文本文件时,需要指定编码
try:
    with open(file_name,encoding='utf-8') as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print('文件不存在!!')

