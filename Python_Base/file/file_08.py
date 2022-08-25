
with open('resource/155.jpg','rb') as file_obj:

    # seek()可以修改当前读取的位置
    file_obj.seek(55)
    file_obj.seek(80)

    # seek()两个参数
    # 第一个要切换的位置
    # 第二个计算位置
    #   0:从头计算，默认值
    #   1：从当前位置计算
    #   2：从最后位置计算
    # print(file_obj.read(55))

    # tell()方法用来查看当前读取的位置
    print(file_obj.tell())
