
# 高阶函数
# 接收函数作为参数，或者将参数作为返回值的函数是高阶函数

l1 = [1,2,3,4,5,6]

def fn(lst):
    def f2(i):
        if i % 2 == 0:
            return True
        return False

    new_list = []
    for n in l1:
        if f2(n):
            new_list.append(n)
    return new_list


print(fn(l1))

# 匿名函数
#   lambda函数表达式专门用来创建一些简单的函数。
#   lambda 参数列表：返回值
#   匿名函数一般都是作为参数使用，其他地方不会使用

def fn5(a,b):
    return a + b


print((lambda a, b: a + b)(1,2))

r = filter(lambda i : i > 5, l1)

# print(list(r))
# map()函数可以对可跌倒对象中的所有元素做指定的操作，然后将其添加到一个新的对象中返回

r = map(lambda i : i ** 2,l1)
# print(list(r))

# sort()
# 该方法用来对列表中的元素进行排序
# sort()默认是直接比较列表中的元素的大小
# 在sort()可以接收一个关键字参数,key
# key需要一个函数作为参数,当设置了函数作为参数
# 每次都会以列表中的一个元素作为参数来调用函数,并且使用函数的返回值来比较元素的大小
l = ['bb','aaaa','cc','dddddddd','fffff']
l.sort()
print(l)

l3 = [1,5,'2','9',4]
l3.sort(key=int)
print(l3)


# sorted()
# 用法与sort基本一致.
# sorted()可以对任意的序列进行
# 并且使用sorted()排序不会影响原来的对象,而是返回一个新对象

l = '1223344567876456'
print(sorted(l,key = int))