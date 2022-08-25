# 超大文件读取
# read()会读取文件中所有内容,超大文件不建议用read()
# read()可以接收一个size的参数,限定读取的长度

file_name = 'resource/123.txt'

try:
    with open(file_name, encoding='utf-8') as file_obj:
        size = 4
        while True:
            c = file_obj.read(size)
            if not c:
                break

            print(c,end='')
except FileNotFoundError:
    print('文件不存在!!')
