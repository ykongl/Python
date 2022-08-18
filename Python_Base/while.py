# # while循环
# # 初始变量
# k = 3
# # 条件表达式
# while k != 0:
#     # 更新表达式
#     k -= 1
#     print("jjj")
# else:
#     print("kkk")
#
# # 练
# i = 0
# sum = 0
# while i < 100:
#     i += 1
#     if(i % 2 != 0):
#         sum += i
# print(sum)
#
# # 水仙花数
# i = 100
# while i < 1000:
#     a = i // 100
#     b = i //10 %10
#     c = i % 10
#     if a ** 3 + b ** 3 + c ** 3 == i:
#         print(i)
#     i += 1
#
# # 质数
# z = int(input("请输入一个数(>1)："))
# i = 2
# flag = True
# if z == 1:
#     print("既不是质数，也不是合数")
# while i < z:
#     if z % i == 0:
#         flag = False
#     i += 1
# if flag:
#     print(z,"质数")
# else:
#     print(z,"不是质数")
# i = 0
# 循环嵌套
# while i < 5:
#     j = 0
#     while j < 5:
#         print("*",end='')
#         j += 1
#     print()
#     i += 1

## 九九乘法表
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print(j,'*',i,'=',i * j,' ',end='')
#         j += 1
#     i += 1
#     print()
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j, '*', i, '=', i * j, ' ', end='')
#     print()
# 100以内的质数
# from time import *
# begin = time()
# i = 2
# while i <= 10000:
#     j = 2
#     flag = True
#     while j < i/2:
#         if i % j == 0:
#             flag = False
#             break
#         j += 1
#     if flag:
#         print(i)
#     i += 1
# # 0.6652975082397461
# # 0.7689764499664307
# # 7.027227401733398
# # 优化
# print(time() - begin , '秒')