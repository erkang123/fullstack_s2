#__author:"HYK"
#DATE:2018/4/7

# s = set('alex li')  #可以去重
# s1 = ['alvin','ee','alvin']
# print(s)
# s2  = set(s1)
# print(s2,type(s2))

#集合对象是一组无序排列的可哈希的值：集合成员可以做字典的键
# s3 = [[1,2],3,4]
# s4 = set(s3)
# print(s4)

#可变集合，不可变集合
# s = frozenset('yuan')  #不可变集合
# print(s)

# li = [2,3,'alex']
# s  = set(li)
# print(s)
#
# print( 2 in s)
# print(3 in s)


#更新集合
# s.add('uuuuu') #添加一个元素

# s.update('ops')

# s.remove(2)

# s.pop()

# s.clear()

# print(s)

#等价
# print(set('alex') == set('alexexex'))
#子集，超集
# print(set('alex')<set('alexwwwww')) # True
# print(set('alex')<set('alex'))      # False
#
#
# print(set('alexs') and set('alexw')) # 联合，所有的
# print(set('alexs') or set('alexw'))  #

a = set([1,2,3,4,5])
b = set([4,5,6,7,8])

#intersection()  #交集

print(a.intersection(b))

#union 并集
print(a.union(b))

#difference  差集
print(a.difference(b)) # in a but not in b  a-b
print(b.difference(a)) # in a but not in b  b-a

#反向交集
print(a.symmetric_difference(b)) #对称差集

print(a | b)  #求并集
print(a - b)  #差集
print(b - a)

print(a ^ b) #对称差集


#父集  超集

print(a.issuperset(b)) # a是否是b 的父集
print(a.issubset(b))  #子集 a 是否是b 的子集