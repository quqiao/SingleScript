#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
packages_name   activity_name  可以在终端 输入 python -m atx apkparse <package_path> 
'''
##########################################跑所有内容配置用############################################
# import os
# import sys
#
# type = sys.getfilesystemencoding()
#
# # """游戏名获取"""
# # gameName = raw_input("请输入游戏名:".decode('utf-8').encode('gbk'))  # 输入游戏名
# # test = gameName.decode('GBK')
# # dict_gameName = {u"一起来飞车":"yqlfc", u"全民枪战":"crisisfire","yife":"test",u"极无双":"jws",u"一起来冒险":"yqlmx"}
# # GameName = dict_gameName.get(test)
# # json_gameNaameName
# # GameName = dime = json.dumps(dict_gameName, encoding="UTF-8", ensure_ascii=False)
# # print json_gct_gameName.get(test)
# # game_name = GameName
#
#
#
# """渠道名获取"""
# channelName = raw_input("please input channelName:")  # 输入渠道名
# dict_channelName = {u"华为":"huawei",u"4399":"f399",u"PPS":"pps",u"三星":"samsung",u"当乐":"DL",u"联通沃商店":"wolt",
#                     u"搜狗":"sougou",u"360":"qihoo",u"触手":"cstv",u"应用宝":"qmqzhero",u"百度":"baidu",u"啪啪":"papa",
#                     u"朋友玩":"yq",u"TT语音":"tt",u"美图":"meitu",u"安智":"anzhi",u"拇指玩":"mzw",u"电信爱游戏":"egame",
#                     u"小米":"mi",u"新浪":"sina_wyx",u"叉叉助手（安卓）":"guopan",u"豌豆荚":"wdj",u"益玩":"ewan",
#                     u"37玩":"sy37",u"VIVO步步高":"vivo",u"UC":"uc",u"OPPO":"nearme",u"魅族":"mz",u"联想":"lenovo",
#                     u"金立":"am", u"乐视手机":"leshi", u"酷派":"kp","HTC":"joloplay",u"应用汇":"yyh",u"靠谱助手":"kaopu",
#                     u"38玩":"sy38",u"酷狗":"kugou",u"斗鱼":"douyu",u"草花游戏":"caohua",u"优酷":"youku",
#                     u"17173":"game17173",u"安趣":"anqu",u"唱吧":"changba",u"迅雷":"niux",u"游艺春秋":"iccgame",
#                     u"盟宝":"mengbao",u"应用宝":"qmqzhero",u"怪猫":"gm",u"B站":"bili",u"A站":"acfun",u"百事通":"bestv",
#                     u"PPTV":"pptv",u"今日头条":"jrtt",u"快看":"kuaikan",u"虎牙":"mcbg"}
# test2 = channelName.decode('GBK')
# ChannelName = dict_channelName.get(test2)
# channel_name = ChannelName  # 渠道名
#
#
#
# """ 获取package_name和activity_name"""
# package_path = raw_input("package_path:")  # 输入所测游戏包的路径
# cmd = 'python -m atx apkparse ' + package_path  # 执行的命令
# print cmd
# # decode = cmd.decode('utf-8').encode(type)
# # print decodes
# resultGet = os.popen(cmd).read()  # 输出结果
# dictoration = eval(resultGet)  # 字符串转字典
# # print dictoration
# main_activity = dictoration.get('main_activity')  # 提取main_activity
# getPackagName = dictoration.get('package_name')  # 提取package_name
# package_name = getPackagName  # 游戏包名
# activity_name = main_activity  # 游戏主activity
#
#
# """获取设备名"""
# device = raw_input("device_name:")
# device_dict = {u"oppoR7":"917ec8bc", u"oppoR9s":"174cda58",u"小米5":"9134cd25",u"HTC816":"HC44XWW01011" ,
#                u"华为荣耀8":"WTK7N16930008544",u"努比亚NX569H":"fce9eadb",u"vivoX9i":"a94bcac0",
#                u"乐视":"LE67A06150018510",u"金立":"MREQQO4PZPWO8LHQ",u"三星C5000":"6205c8bf",u"酷派":"90ed423",
#                u"vivoX7":"a20ce85b",u"魅族pro6":"80QBCPD222MK"}
# test3 = device.decode('GBK')
# device_name = device_dict.get(test3)  # 设备名
#
# """通过包名获取游戏名"""
# gameName = ("yqlfc", "crisisfire", "jws", "yqlmx")
# for i in range(len(gameName)):
#     if gameName[i] in package_name:
#         game_name1 = gameName[i]
#         break
# game_name = game_name1
#
#
#
#  area = raw_input("area_name:")
# dict = {u"1区":"game_pre_03@auto.png",u"2区":"game_pre_02@auto.png"}
# test2 = area.decode('GBK')
# # test21 = dict.has_key(test2)
# # print test21
# # if test21 == True:
# #     print u"输入成功"
# # else:
# #     print u"输入错误！！！！"
# area_name = dict.get(test2)
#########################################跑所有内容配置用###########################################


############################################跑引导用################################################
"""获取设备名"""
device = raw_input("请输入设备名:".decode('utf-8').encode('gbk'))
device_dict = {u"oppoR7":"917ec8bc", u"oppoR9s":"174cda58", u"小米5":"9134cd25",u"HTC816":"HC44XWW01011",
               u"华为荣耀8":"WTK7N16930008544", u"努比亚NX569H":"fce9eadb", u"vivoX9i":"a94bcac0",
               u"乐视":"LE67A06150018510", u"金立":"MREQQO4PZPWO8LHQ", u"三星C5000":"6205c8bf",u"酷派":"90ed423",
               u"vivoX7":"a20ce85b", u"魅族pro6":"80QBCPD222MK", u"小米MIX2":"e263b3d8",u"锤子":"542ae538",
               u"360手机":"82cfea33"}
test3 = device.decode('GBK')
DeviceName = device_dict.get(test3)  # 设备名
device_name = DeviceName  # 设备名
"""获取游戏名"""
gameName = raw_input("请输入游戏名:".decode('utf-8').encode('gbk'))  # 输入游戏名
test = gameName.decode('GBK')
dict_gameName = {u"一起来飞车":"yqlfc", u"全民枪战":"crisisfire", u"极无双":"jws", u"一起来冒险":"yqlmx",
                 u"吃豆大作战":"doudou",u"NBA":"NBA",u"赤潮":"zzys",u"疯狂像素人":"xsqs",u"影之刃2":"yzr",
                 u"一起来跳舞":"yqltw",u"夏目的美丽日记":"summer",u"装甲联盟": "tank"}
GameName = dict_gameName.get(test)
game_name = GameName
channel_name = "anzhi"


