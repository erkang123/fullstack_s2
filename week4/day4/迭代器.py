#__author:"HYK"
#DATE:2018/4/22


#迭代器 （iterator）
#满足两个条件：
    # 1.有iter方法  2.有next方法

# 生成器都是迭代器，迭代器不一定是生成器

#list , tuple dict string Iterable(可迭代对象)


#for循环内部三件事
# 1.调用可迭代对象的iter方法 返回一个迭代器对象
# 2.不断调用迭代器对象的next方法


l = [1,2,3,4,5]

d = iter(l)  #返回了一个迭代器对象
print(d)


from collections import Iterator,Iterable

print(isinstance([1,2,3,4],list))

print(isinstance(l,list))
print(isinstance(l,Iterator))  #判断列表是否是迭代器
print(isinstance(l,Iterable))  #判断列表是否是可迭代器对象
print(isinstance(d,Iterable))