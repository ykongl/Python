

# 阶层
def factorial(n):
    for i in range(1, n):
        n *= i
    return n


print(factorial(10))

# 递归
def fn1(n):
    if n == 1:
        return 1
    return n * fn1(n-1)


print(fn1(10))


# 求幂
def power(n, i):
    if i == 1:
        return n
    return n * power(n, i - 1)

print(power(2,3))


# 回文
def hui_wen(s):
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    return hui_wen(s[1:-1])

print(hui_wen('1abcba1'))