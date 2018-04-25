#__author:"HYK"
#DATE:2018/4/20



# def print_info(name,age):
#     print('name: %s'%name)
#     print('age : %s' %age)

#1.必须参数
# print_info('erkang',22)

#2.关键字参数
# print_info(age = 39,name = 'alex')

# def print_info(name,age,sex='male'):
#     print('name: %s'%name)
#     print('age : %d' %age)
#     print('sex : %s' %sex)

#3.默认参数  （默认参数必须在其它参数后面）
# print_info('xiaohu',40)
# print_info('jinxin',40,'female')

#low加法器
# def add(x,y):
#     print(x+y)
#
# add(1,2)

#高大上 加法器
# def add(*args):
#     print(args)
#     sum = 0
#     for i in args:
#         sum+=i
#     print(sum)
#
# add(1,2,3,4)


# def print_info(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
#     for i in kwargs:
#         print('%s:%s'%(i,kwargs[i]))
# print_info('alex',18,'male',job = 'IT',hobby = 'girls',height = 188)
#print_info(job = 'IT','alex',18,'male',hobby = 'girls',height = 188)  #报错，位置关系

#关于不定长参数的位置：*args放在左边，**kwargs 参数放在右边
#如果有默认参数，放在左边
#关键参数放最左边》默认参数》不定长参数

def print_info1(sex = 'male',*args,**kwargs):
    print(sex)
    print(args)
    print(kwargs)

    for i in kwargs:
        print('%s:%s'%(i,kwargs[i]))

# print_info1()
print_info1('tttt',2,3,4,'female',name = 'hello')