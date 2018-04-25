#__author:"HYK"
#DATE:2018/4/22

import  time
'''  
过程

#遵守开放封闭原则
def foo():
    print('foo...')
    time.sleep(2)

# foo()


# def show_time(f):
#     start = time.time()
#     f()
#     end = time.time()
#     print('spend %s'%(end-start))
#
# show_time(foo)


def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('spend %s'%(end-start))

    return inner

foo = show_time(foo)
foo()   #相当于执行了inner函数

'''

#用到装饰器
# def show_time(f):
#     def inner():
#         start = time.time()
#         f()
#         end = time.time()
#         print('spend %s'%(end-start))
#
#     return inner
#
# @show_time  # foo = show_time(foo)
# def foo():
#     print('foo...')
#     time.sleep(2)
#
# foo()

# #功能函数加参数
# def show_time(f):
#     def inner(*x,**y):
#         start = time.time()
#         f(*x,**y)
#         end = time.time()
#         print('spend %s'%(end-start))
#
#     return inner
#
# @show_time  # add = show_time(add)
# def add(*a,**b):
#     sums = 0
#     for i in a:
#         sums +=i
#     print(sums)
#     time.sleep(1)
#
# add(1,2,3)


#装饰器加参数
def logger(flag):
    def show_time(f):
        def inner(*x,**y):
            start = time.time()
            f(*x,**y)
            end = time.time()
            print('spend %s'%(end-start))
            if flag == 'true':
                print("日志记录")
        return inner
    return show_time

@logger('true')  # @show_time
def add(*a,**b):
    sums = 0
    for i in a:
        sums +=i
    print(sums)
    time.sleep(1)

add(1,2,3)