# coding=utf-8

import os
gameName = raw_input("please input gameName:", )
channelName = raw_input("please input channelName:", )

def getPackagName():
    cmd = 'adb -s MREQQO4PZPWO8LHQ shell pm list packages -e ' + gameName + ' -e ' + channelName
    resultGet = os.popen(cmd).read()
    subStr = resultGet.split(":", 1)
    return subStr[-1].split()

def getDeviceID():
    cmd="adb devices"
    resultGet=os.popen(cmd).read()
    listStr=resultGet.split("\n")
    subList=listStr[1].split("\t")
    return subList[0]