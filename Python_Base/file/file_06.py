
# 文件的写入

file_name = 'resource/456.txt'

# 使用open()打开文件时必须指定文件所需的操作(读,写,追加)
# 默认为读r
# 写w,如果写入文件,文件不存在时会创建文件,如果文件存在则会截断文件
# 截断文件指删除原来文件中的所有内容
# a表示追加,如果文件不存在,则创建文件,存在就追加内容

# x 用来新建文件,如果文件不存在则创建,否则报错
# + 为操作符增加功能
# r+ 既可读又可写
# w+
# a+
with open(file_name, 'w', encoding='utf-8') as file_obj:
    # 向文件中写入内容,是字符串类型
    # 该方法可以分多次向文件中写入内容
    file_obj.write('456\n天动万象')
    file_obj.write('456\n巴巴托斯')
    file_obj.write('456\n凯瑞亚')
    print(file_obj.read())
