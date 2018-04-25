#__author:"HYK"
#DATE:2018/4/21


#return
#作用：1.结束函数，2返回某个对象
#注意点：1.如果函数没有return,会默认返回一个None
        # 2.如果return多个对象，那么python会帮我们把多个对象封装成一个元祖返回
# def f():
#     print('ok')
#     return 109
# a = f()
# print(a)
# print(f())

def foo():
    return 1,'123',[1,2,3]

b = foo()
print(b)