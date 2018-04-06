#__author:"HYK"
#DATE:2018/4/5

#name = 'wuchao jinxing xiaohu sanpang ligang'

# a = ['wuchao','jinxing','xiaohu','sanpang','ligang']

#增删改查

#查   切片
# print(a[1:])    #取到最后
# print(a[1:-1]) #不包括最后一个元素
# print(a[1:-1:2]) #从左到右一个一个去取
# print(a[-2::-2]) #从左到右一个一个去取

#增 append  insert
# a.append("xuepeng")  #append的参数是需要添加的值,默认插到最后的位置
# print(a)

# a.insert(1,'xuepeng') #将数据插入到任意一个位置
# print(a)

#修改

# a[1] = 'haidilao'
# print(a)

# a[1:3]=['a','b']
# print(a)

#删除 remove pop del
# a.remove('wuchao')
# print(a)

# b = a.pop(1) #参数为索引值
# print(a)
# print(b)

# del a[0]  #列表之外的删除方法
# print(a)
#
# del a
# print(a)

#count:计算某元素出现次数
# a = ['wuchao','jinxing','xiaohu','sanpang','ligang'].count("wuchao")
# print(a)

#extend
# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# print(a)
# print(b)

#index:获取元素的标签，根据内容找位置
# a = ['wuchao','jinxing','xiaohu','sanpang','ligang']
# print(a.index('xiaohu'))

#reverse :对列表进行倒叙排序
# a = ['wuchao','jinxing','xiaohu','sanpang','ligang']
# a.reverse()
# print(a)

#sort :对列表进行排序
x = [4,2,15,657,54,1,3]
# x.sort()
# print(x)

x.sort(reverse=True)
print(x)