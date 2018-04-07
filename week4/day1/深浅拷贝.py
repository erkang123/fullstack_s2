#__author:"HYK"
#DATE:2018/4/7

# s = [1,'alex','alvin']
# s2 = s.copy()
# print(s2)
#
#
# s2[0] = 3
# print(s)
# print(s2)

s = [[1,2],'alex','alvin']
s3 = s.copy()
print(s3)

s3[0][1] = 3
print(s3)
print(s)  #s也变了

import copy
xiaosan  = copy.copy(s) #浅拷贝

xiaosan1 = copy.deepcopy(s) #深拷贝