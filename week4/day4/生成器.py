#__author:"HYK"
#DATE:2018/4/22


#生成器一共两种创建方式
# 1. (x*2 for x in range(10))
# 2.yield

'''
s = (x*2 for x in range(10))

print(s)  #<generator object <genexpr> at 0x000002879EC2D0A0>

# print(s.__next__())
print(next(s))  #等价于 s.__next__()   in py2: s.next()

#生成器就是一个可迭代对象（Iterable)
for i in s:
    print(next(i))

'''


# def foo():
#     print('ok')
#     yield 1
#
#     print('ok2')
#     yield 2
#
# g=foo() #生成器对象
#
# print(g)
#
# print(next(g))
# print(next(g))

#什么是可迭代对象(对象拥有iter方法的称为可迭代对象)
# l = [1,2,3]
# l.__iter__()
#
# t = (1,2,3)
# t.__iter__()
#
# d = {'name':'123'}
# d.__iter__()
#
# for i in [1,2,3,4]:
#     print(i)

'''
通过斐波那契数列来讲解yield
# def fib(max):
#     n,before,after = 0,0,1
#     while n<max:
#         print(after)
#         before,after  = after,before + after
#         n +=1
#
# fib(10)


def fib(max):
    n,before,after = 0,0,1
    while n<max:
        yield before
        before,after  = after,before + after
        n +=1

g = fib(10)
print(g)  #<generator object fib at 0x000001F5EFDED0A0>

print(next(g))

'''


#生成器的send()方法
def bar():
    print('ok1')
    count = yield 1
    print(count)

    yield 2
    print('ok2')

b = bar()
# next(b)

b.send(None)  #next(b) 第一次send前如果没有next ,只能传一个send(None)
# print(s)
b.send('eeee')