#__author:"HYK"
#DATE:2018/4/6

# a = 10
# print(id(a))
# b = a
# print(id(b))
# b = 15
# print(id(b))
#
# print(a)
# print(b)

# dic = {'name':'alex','age':35,'hobby':{'girl_name':'铁锤','age':45},'is_handsome':True}
# print(dic)
# print(dic['name'])
# print(dic['hobby'])

#创建字典
# a = [1,2,3]
# a = list((1,2,3))
# print(a)

# dic1 = {}
# dic2 = dict((('name','alex'),))
# dic3 = dict((['name','alex'],))
# dic4 = dict([['name','alex'],])
# print(dic2)
# print(dic3)
# print(dic4)

'''
#增加
dic1 = {'name':'alex'}
dic1['age'] = 18    #增加键为age的数据

print(dic1)
#键存在，不改动，返回字典中相应的键对应的值
ret = dic1.setdefault('age',34) #如果存在键，不对字典做任何操作，如果没有，就添加,函数返回值
print(ret)

#键不存在，在字典中增加新的键值对，并返回相应的值
dic1.setdefault('job','IT') #如果存在键，不对字典做任何操作，如果没有，就添加
print(dic1)

#查
dic3 = {'name':'alex','age':35,'hobby':{'girl_name':'铁锤','age':45},'is_handsome':True}
print(dic3['name'])
print(dic3.keys())  #获取字典的键key
print(dic3.values())
print(dic3.items())

#改
dic4 = {'name':'alex','age':35,'hobby':{'girl_name':'铁锤','age':45},'is_handsome':True}
dic4['age'] = 20
dic5 = {'1':'1111','2':'222'}
dic4.update(dic5)  #类似于列表中的extend方法

#删除
dic6 = {'name':'alex','age':35,'hobby':{'girl_name':'铁锤','age':45},'is_handsome':True}
del dic6['name']        #删除字典中指定键值对
del  dic6               #删除整个字典
dic6.clear()            #清空字典，变为一个空字典
ret = dic6.pop('age')   #删除字典中指定键值对，并返回改键值对的值
a = dic6.popitem()      #随机删除某组键值对，并以元组方式返回值
print(ret)


#其它操作已经涉及到的方法
# dic7 = dict.fromkeys(['host1','host2','host3'],'test')
# print(dic7)

    #嵌套
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

print(av_catalog)
av_catalog['欧美']['www.youporn.com'][1] = '质量很好'   #修改
print(av_catalog)

    #排序
# dic = {5:'5555',2:'22234',3:'4444'}
# print(sorted(dic))
# print(sorted(dic.values()))
# print(sorted(dic.items()))

    #字典遍历
dic = {5:'5555',2:'22234',3:'4444'}
# for k,v in dic.items():
#     print(k,v)

for i in dic:
    print(i,dic[i]) #效率高
'''


#String 操作
# a = "Let's go "
# # print(a)
# #
# # print('hello'*3) #重复输出字符串
# #
# # print('helloworld'[2:]) #通过索引获取字符串中字符，这里和列表的切片操作是相同的

#关键字 in
# print('el' in 'hello')

#格式化字符串
# print('%s is a good teacher'%'alex')

a = '123'
b = 'abc'
d = '44'
# c = a+b
# print(c)

# c = ''.join([a,b])  #字符串拼接
# d = '****'.join([a,b])
# e = '-----'.join([a,b,d])
# print(c)
# print(d)
# print(e)

#String的内置方法
st = 'hello kitty'
# print(st.count('l'))  #统计元素个数
# print(st.capitalize()) #字符串首字母大写
# print(st.center(50,'-')) #字符串居中
# print(st.endswith('y')) #判断是否以某个字符结尾
# print(st.startswith('h')) #判断是否以某个字符开头
# st1 = 'he\tllo kitty'
# print(st1.expandtabs(tabsize=10)) #判断是否以某个字符开头
# print(st.find('e'))  #查找字符在字符串中的索引位置

st2 = 'hello kitty {name} is {age}'
# print(st2.format(name = 'alex',age = 37))  #格式化输出的另一种方式
# print(st2.format_map({'name':'alex','age':22}))
# print(st.index('t')) #查找字符在字符串中的索引位置
# print('abc'.isalnum()) #
# print('1232d'.isdecimal()) #
# print('1232'.isdigit()) #判断是否一个整数数字
# print('1232'.isnumeric()) #判断是否一个整数数字
# print('1232'.isidentifier()) #检测一段字符串可否被当作标志符，即是否符合变量命名规则
# print('1232'.islower()) #判断是否全小写
# print('1232'.isupper()) #判断是否全大写
# print('ABDcs'.lower()) #大写变小写
# print('ABDcs'.upper()) #大写变小写
# print('ABDcs'.swapcase()) #大写变小写,小写变大写
# print('ABDcs'.ljust(50,'*')) #大写变小写,小写变大写
# print('ABDcs'.rjust(50,'*')) #大写变小写,小写变大写
# print('ABD cs '.strip()) #去掉前后换行，空格符
# print('ABD cs '.lstrip()) #去掉左边换行，空格符
# print('ABD cs '.rstrip()) #去掉右边换行，空格符
# print('ABD cs '.replace('cs','lesson')) #进行替换
# print('my title'.split('t')) #以什么进行分割，变成一个列表
# print('my title'.title()) #把字符串变为标题

#摘一些重要的字符串方法
# print(st.count('l'))  #统计元素个数
# print(st.center(50,'-')) #字符串居中
# print(st.startswith('h')) #判断是否以某个字符开头
# print(st.find('e'))  #查找字符在字符串中的索引位置
# print(st2.format(name = 'alex',age = 37))  #格式化输出的另一种方式
# print('ABDcs'.lower()) #大写变小写
# print('ABDcs'.upper()) #大写变小写
# print('ABD cs '.strip()) #去掉前后换行，空格符
# print('ABD cs '.replace('cs','lesson')) #进行替换
# print('my title'.split('t')) #以什么进行分割，变成一个列表

a_lis   = [1,2,4]
res = a_lis.pop()
print(res)