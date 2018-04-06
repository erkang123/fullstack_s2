#__author:"HYK"
#DATE:2018/4/6
# -*- coding:utf-8 -*-
s = '特斯拉'
s_to_unicode = s.decode("utf-8")
unicode_to_gbk = s_to_unicode.encode("gbk")
print(s)
print(s_to_unicode)
print(unicode_to_gbk)