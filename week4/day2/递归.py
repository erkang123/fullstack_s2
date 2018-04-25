#__author:"HYK"
#DATE:2018/4/21

#阶层
'''
5! = 5*4*3*2*1
7! = 7*6*5*4*3*2*1
'''

# def fat(n):
#     ret = 1
#     for i in range(1,n+1):
#         ret = ret*i
#     return ret
#
# print(fat(5))

#关于递归的特点：
"""
1. 调用自身函数
2. 有一个结束条件
3. 
"""
#但凡是递归可以写的循环都可以解决
#递归的效率在很多时候效率很低
def fact(n):
    if n ==1:
        return 1
    return n * fact(n-1)

print(fact(5))