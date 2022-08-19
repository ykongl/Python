# EMS（员工管理系统）练习
print('=' * 20,'员工管理系统','=' * 20)
list1 = ['孙悟空\t18\t男']
while True:
    print('选择操作：')
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出系统')
    chose = int(input('请选择【1-4】:'))
    if chose == 1:
        print('\t序号\t姓名\t年龄\t性别')
        n = 1
        for j in list1:
            print(f'\t{n}\t{j}')
            n += 1
    elif chose == 2:
        name = input('请输入新增员工姓名：')
        age = input('请输入新增员工年龄：')
        sex = input('请输入新增员工性别：')
        list1.append(f'{name}\t{age}\t{sex}')
    elif chose == 3:
        del_num = int(input('请输入要删除的序号：'))
        if(0 < del_num <= len(list1)):
            print("请确认是否删除(Y/N):")
            tt = input()
            if tt == 'y':
                list1.pop(del_num - 1)
                print("删除成功！！！")
            else:
                print("删除取消！！！")
        else:
            print("序号不正确")
    elif chose == 4:
        print("退出成功！！！")
        break
    else:
        print("请重新选择【1-4】:")