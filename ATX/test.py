#coding=utf-8


# gameName = raw_input("please input gameName:")   # 输入游戏名
#
#
# dict_gameName = {"一起来飞车":"yqlfc","全民枪战":""}
#
# GameName = dict_gameName.get(gameName)
#
# print GameName



# def info1(self,driver):
#         a = driver.info
#         print a
#         b = a.get(u'displayWidth')
#         print b
#         c = b/1920.0
#         print c
#         return c
# print
#
# def info2(self,driver):
#     a = driver.info
#     b = a.get( u'displayHeight')
#     c = b/1080.0
#     return c
import os
# import re

# cmd = "adb shell wm size"
# print cmd
# a = os.popen(cmd).read()
# print a
# c = a.split()
# print c
# d = c[2]
# print d
# e = d.split('x')
# print e
#
# screen_x = e[1]
# print screen_x
# screen_y = e[0]
# print screen_y

# cmd = "adb shell wm size"
# print cmd
# a = os.popen(cmd).read()
# print a
# line = "Cats are smarter than dogs";
# b= re.search( '(.*) x (.*) .*',line , re.M|re.I)
#
# print b


# line = "Cats are smarter than dogs";
#
# searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
#
# print searchObj
#
# if searchObj:
#    print "searchObj.group() : ", searchObj.group()
#    print "searchObj.group(1) : ", searchObj.group(1)
#    print "searchObj.group(2) : ", searchObj.group(2)
# else:
#    print "Nothing found!!"


# import random
#
# print "uniform(5, 10) 的随机数为 : ",  random.uniform(5, 10)

# def changeInt(a):
#    a = 10
#
# b = 2
# changeInt(b)
# print b

Money = 2000
def AddMoney():
   # 想改正代码就取消以下注释:
   global Money
   Money = Money + 1

print Money
AddMoney()
print Money
