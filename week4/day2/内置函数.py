#__author:"HYK"
#DATE:2018/4/21

#重要内置函数

str = ['a','b','c','d']

# def fun1(s):
#     if s != 'a':
#         return s
#
# ret = filter(fun1,str)
#
# print(list(ret))


# def fun2(s):
#     return s + "alvin"
#
# ret = map(fun2,str)
# print(list(ret))


from functools import reduce
#
# def add(x,y):
#     return x + y
# print(reduce(add,range(1,10)))  #
#
#
# lambda x,y :x+y

a = reduce((lambda x,y:x+y),range(1,10))
print(a)