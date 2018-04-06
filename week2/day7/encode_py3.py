#__author:"HYK"
#DATE:2018/4/6

import  sys
s = 'i am 特斯拉'
s_to_gbk = s.encode('gbk')
print(s)
print(s_to_gbk)
print(sys.getdefaultencoding())