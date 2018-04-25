#__author:"HYK"
#DATE:2018/4/21

# if  True:
#     x = 3
# print(x)
#
# def f():
#     a = 10
# print(a)

# x = int(2.9) # int buit-in
#
# g_count = 0 # global

# def outer():
#     o_count = 1  #enclosing
#     def inner():
#         i_count = 2 #local
#         print(i_count)
#
#     inner()
# outer()

count = 10
def outer():
    print(count)
    # count = 5
outer()
print(count)

# def outer():
#     count  = 10
#     def inner():
#         nonlocal count
#         count  = 20
#         print(count)
#     inner()
#     print(count)
# outer()

#小结
"""
(1) 变量查找顺序：LEGB,作用域 > 外层作用域 > 当前模块中的全局 > python内置作用域
(2) 只有模块，类，及函数才能引入新作用域
(3) 对于一个变量，内部作用域先声明就会覆盖外部变量，不声明直接使用，就会使用外部作用域的变量
(4) 内部作用域要修改外部作用域变量的值时，全局变量要使用global关键字，嵌套作用域变量要使用nonlocal关键字。nonlocal时python3新增的关键字，有了这个关键字，就能完美的实现闭包了。
"""