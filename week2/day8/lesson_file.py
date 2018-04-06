#__author:"HYK"
#DATE:2018/4/6

#能调用方法的一定是对象
# li = [1,2,3]
# li.append('5')
# b = 'asc'.capitalize()
# print(li)
# print(b)


# data = open('小重山','r',encoding='utf-8').read()
# print(data)

#只读模式
# f = open('小重山','r',encoding='utf-8')
# data = f.read(5)
# print(data)
# f.close()
#只写模式
# f = open('小重山2','w',encoding='utf-8')
# data = f.write('hello world')
# f.close()
#追加模式
# f = open('小重山2','a',encoding='utf-8')
# data = f.write('hello world2 \n')
# print(f.fileno())
# print(f.mode)
# f.close()

#读取一行或多行的方法
# f = open('小重山','r',encoding='utf-8')
# data = f.readline()
# print(data)
# data1 = f.readline()  #打印一行
# data1 = f.readlines()  #打印所有行
# for i in data1:
#     print(i.strip())
# print(data1)
# f.close()

f = open('小重山','r',encoding='utf-8')
# number = 0
# for i in f.readlines():
#     number += 1
#     if number == 6:
#         i = ''.join([i.strip(),'iiii'])
#     print(i.strip())

for i in f: #这是for 内部将f对象做成一个迭代器，用一行取一行
    print(i.strip())