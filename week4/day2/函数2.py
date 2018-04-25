#__author:"HYK"
#DATE:2018/4/21

#高阶函数
# def f(n):
#     return n*n
#
# def foo(a,b,func):
#     return func(a)+func(b)
#
# a = foo(1,2,f)
# print(a)


# too = f

#1. 函数名可以进行赋值
#2. 函数名可以作为函数参数，还可以作为函数的返回值

def foo2():
    x = 5
    return  x

print(foo2())

def foo3():
    def inner():
        return 8
    return inner()

print(foo3())