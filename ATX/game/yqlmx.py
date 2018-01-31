#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
import os
import configure
log = logutils.getLogger(__name__)

class Game(public.Methods):

    # def info1(self,driver):
    #     a = driver.info
    #     print a
    #     b = a.get(u'displayWidth')
    #     print b
    #     c = b/1920.0
    #     print c
    #     return c
    #
    # def info2(self,driver):
    #     a = driver.info
    #     b = a.get( u'displayHeight')
    #     c = b/1080.0
    #     return c

    def info1(self, driver):
        cmd = "adb -s %s shell wm size" %configure.device_name
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[1]
        g = float(f)
        x = g/1920.0
        return x

    def info2(self, driver):
        cmd = "adb -s %s shell wm size" %configure.device_name
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[0]
        g = float(f)
        y = g/1080.0
        return y

    def game_pre(self, driver):
        self.click_images(driver, "game_pre_01@auto.png")  # 换区
        self.click_images(driver, configure.area_name)



    def guide(self,driver):
        # if self.images_or_none(driver, 'guide_17@auto.png'):
        ###################################################################################
        '''建造1'''
        while ( 0<1 ):
            if self.images_or_none(driver, "guide_01@auto.png"):  # 跳过
                break
        sleep(2)
        driver.swipe((self.info1(driver)*1830.0), (self.info2(driver)*80.0),(self.info1(driver)*1830.0), (self.info2(driver)*80.0), 10)
        self.images_or_none(driver, "guide_01@auto.png")  # 跳过
        driver.swipe((self.info1(driver)*1830.0), (self.info2(driver)*80.0),(self.info1(driver)*1830.0), (self.info2(driver)*80.0), 10)
        self.images_or_none(driver, "guide_16@auto.png")  # 等待对话出现
        for i in range(8):
            sleep(1)
            driver.click(500, 500)  # 任意键
        sleep(2)
        driver.click((self.info1(driver)*980.0), (self.info2(driver)*550.0))  # 升级基地
        sleep(2)
        driver.click((self.info1(driver)*1040.0), (self.info2(driver)*650.0))  # 升级建筑
        sleep(2)
        driver.click((self.info1(driver)*1520.0), (self.info2(driver)*950.0))  # 建造
        self.images_or_none(driver, "guide_02@auto.png")  # 领取血钻
        driver.click((self.info1(driver)*980.0), (self.info2(driver)*550.0))  # 领取血钻
        sleep(2)
        driver.click((self.info1(driver)*1660.0), (self.info2(driver)*990.0))  # 建设
        sleep(2)
        driver.click((self.info1(driver)*350.0), (self.info2(driver)*520.0))  # 矿石
        sleep(2)
        driver.click((self.info1(driver)*1520.0), (self.info2(driver)*950.0))  # 建造
        self.images_or_none(driver, "guide_03@auto.png")  # 血钻完成
        driver.click((self.info1(driver)*540.0), (self.info2(driver)*750.0))  # 血钻完成
        sleep(2)
        driver.click((self.info1(driver)*950.0), (self.info2(driver)*760.0))  # 立即完成
        sleep(2)
        driver.click((self.info1(driver)*450.0), (self.info2(driver)*640.0))  # 挖掘机1级
        self.images_or_none(driver, "guide_01@auto.png")  # 跳过
        driver.swipe((self.info1(driver)*1830.0), (self.info2(driver)*80.0),(self.info1(driver)*1830.0), (self.info2(driver)*80.0), 10)
        sleep(3)
        driver.click((self.info1(driver)*450.0), (self.info2(driver)*640.0))  # 挖掘机1级
        sleep(2)
        driver.click((self.info1(driver)*1660.0), (self.info2(driver)*990.0))  # 建设
        sleep(2)
        driver.click((self.info1(driver)*350.0), (self.info2(driver)*880.0))  # 起重机
        sleep(2)
        driver.click((self.info1(driver)*1520.0), (self.info2(driver)*950.0))  # 建造
        sleep(2)
        driver.click((self.info1(driver)*850.0), (self.info2(driver)*750.0))  # 完成
        sleep(2)
        driver.click((self.info1(driver)*950.0), (self.info2(driver)*760.0))  # 立即完成
        sleep(2)
        driver.click((self.info1(driver)*780.0), (self.info2(driver)*640.0))  # 起重机1级1次
        sleep(2)
        driver.click((self.info1(driver)*780.0), (self.info2(driver)*640.0))  # 起重机1级2次
        sleep(2)
        driver.click((self.info1(driver)*1660.0), (self.info2(driver)*990.0))  # 建设
        sleep(2)
        driver.click((self.info1(driver)*350.0), (self.info2(driver)*510.0))  # 能源核心3级
        sleep(2)
        driver.click((self.info1(driver)*1520.0), (self.info2(driver)*950.0))  # 建造
        sleep(2)
        driver.click((self.info1(driver)*1050.0), (self.info2(driver)*650.0))  # 完成
        sleep(2)
        driver.click((self.info1(driver)*950.0), (self.info2(driver)*760.0))  # 立即完成
        '''建造2'''
        self.images_or_none(driver, "guide_04@auto.png")  # 能源核心 3级
        driver.click((self.info1(driver)*980.0), (self.info2(driver)*540.0))  # 能源核心 3级
        for i in range(30):
            sleep(1)
            driver.click(500,500)  # 任意键
        sleep(2)
        driver.click((self.info1(driver)*1650.0), (self.info2(driver)*990.0))  # 建设
        sleep(2)
        driver.click((self.info1(driver)*350.0), (self.info2(driver)*520.0))  # 兵营
        sleep(2)
        driver.click((self.info1(driver)*1520.0), (self.info2(driver)*950.0))  # 建造
        sleep(5)
        driver.click((self.info1(driver)*1650.0), (self.info2(driver)*990.0))  # 建设
        sleep(2)
        driver.click((self.info1(driver)*350.0), (self.info2(driver)*520.0))  # 靶场
        sleep(2)
        driver.click((self.info1(driver)*1520.0), (self.info2(driver)*950.0))  # 建造
        sleep(2)
        driver.click((self.info1(driver)*60.0), (self.info2(driver)*40.0))  # 返回
        sleep(2)
        driver.click((self.info1(driver)*350.0), (self.info2(driver)*890.0))  # 面包房
        sleep(2)
        driver.click((self.info1(driver)*1520.0), (self.info2(driver)*950.0))  # 建造
        sleep(6)
        driver.click((self.info1(driver)*1230.0), (self.info2(driver)*530.0))  # 面包房1级
        sleep(2)
        driver.click((self.info1(driver)*1230.0), (self.info2(driver)*530.0))  # 面包房1级
        sleep(2)
        driver.click((self.info1(driver)*1650.0), (self.info2(driver)*990.0))  # 建设
        sleep(2)
        driver.click((self.info1(driver)*350.0), (self.info2(driver)*520.0))  # 靶场
        sleep(2)
        driver.click((self.info1(driver)*1520.0), (self.info2(driver)*950.0))  # 建造
        for i in range(40):
            sleep(1)
            driver.click(500, 500)  # 任意键
        sleep(2)
        driver.click((self.info1(driver)*1350.0), (self.info2(driver)*550.0))  # 寻找勇者
        '''扭蛋'''
        sleep(2)
        driver.click((self.info1(driver)*410.0), (self.info2(driver)*750.0))  # 普通扭蛋
        sleep(2)
        driver.click((self.info1(driver)*550.0), (self.info2(driver)*710.0))  # 1次
        sleep(15)
        driver.click((self.info1(driver)*1650.0), (self.info2(driver)*1000.0))  # 人物背景
        sleep(2)
        driver.click((self.info1(driver)*960.0), (self.info2(driver)*960.0))  # 确认
        sleep(2)
        driver.click((self.info1(driver)*890.0), (self.info2(driver)*750.0))  # 精英扭蛋
        sleep(2)
        driver.click((self.info1(driver)*1060.0), (self.info2(driver)*720.0))  # 1次
        sleep(15)
        driver.click((self.info1(driver)*1650.0), (self.info2(driver)*1000.0))  # 人物背景
        sleep(2)
        driver.click((self.info1(driver)*960.0), (self.info2(driver)*960.0))  # 确认
        sleep(2)
        driver.click((self.info1(driver)*60.0), (self.info2(driver)*40.0))  # 返回
        '''欢迎'''
        self.images_or_none(driver, "guide_05@auto.png")  # 欢迎
        driver.click((self.info1(driver)*960.0), (self.info2(driver)*820.0))  # 欢迎
        sleep(6)
        driver.click((self.info1(driver)*960.0), (self.info2(driver)*820.0))  # 欢迎
        sleep(2)
        driver.click((self.info1(driver)*1650.0), (self.info2(driver)*990.0))  # 建设
        sleep(2)
        driver.click((self.info1(driver)*350.0), (self.info2(driver)*520.0))  # 核心能源4级
        sleep(2)
        driver.click((self.info1(driver)*1520.0), (self.info2(driver)*950.0))  # 建造
        '''出城'''
        sleep(2)
        driver.click((self.info1(driver)*1800.0), (self.info2(driver)*980.0))  # 出城
        driver.long_click((self.info1(driver)*1800.0), (self.info2(driver)*980.0))  # 出城
        self.images_or_none(driver,"guide_01@auto.png")  # 跳过
        driver.swipe((self.info1(driver)*1830.0), (self.info2(driver)*80.0),(self.info1(driver)*1830.0), (self.info2(driver)*80.0), 10)
        '''第一章'''
        self.images_or_none(driver,"guide_06@auto.png")  # 第一章
        driver.click((self.info1(driver)*490.0), (self.info2(driver)*490.0))  # 第一章
        self.images_or_none(driver,"guide_07@auto.png")  # 圣域
        driver.click((self.info1(driver)*450.0), (self.info2(driver)*520.0))  # 圣域
        sleep(2)
        driver.click((self.info1(driver)*1500.0), (self.info2(driver)*970.0))  # 攻击
        sleep(2)
        driver.click((self.info1(driver)*480.0), (self.info2(driver)*700.0))  # 选择勇士1
        sleep(2)
        driver.click((self.info1(driver)*480.0), (self.info2(driver)*960.0))  # 选择勇士2
        sleep(2)
        '''开战'''
        driver.click((self.info1(driver)*1600.0), (self.info2(driver)*880.0))  # 开战
        sleep(2)
        self.images_or_none(driver,"guide_08@auto.png")  # 等待对话出现
        for i in range(4):
            sleep(1)
            driver.click(500,500)  # 任意键
        sleep(2)
        driver.click((self.info1(driver)*120.0), (self.info2(driver)*980.0))  # 坦克出战
        self.images_or_none(driver, "guide_09@auto.png")  # 召唤勇者
        driver.click((self.info1(driver)*330.0), (self.info2(driver)*980.0))  # 召唤勇者
        self.images_or_none(driver, "guide_10@auto.png")  # 等待对话出现
        for i in range(3):
            sleep(1)
            driver.click(500, 500)  # 任意键
        self.images_or_none(driver, "guide_11@auto.png")  # 释放合体技
        driver.click((self.info1(driver)*660.0), (self.info2(driver)*520.0))  # 释放合体技
        sleep(3)
        self.images_or_none(driver, "guide_12@auto.png")  # 退出战斗
        driver.click((self.info1(driver)*1650.0), (self.info2(driver)*950.0))  # 退出战斗
        sleep(2)
        for i in range(10):
            sleep(1)
            driver.click(500, 500)  # 任意键
        sleep(15)
        driver.click((self.info1(driver)*1650.0), (self.info2(driver)*1000.0))  # 人物背景
        sleep(2)
        driver.click((self.info1(driver)*60.0), (self.info2(driver)*40.0))  # 返回
        self.images_or_none(driver, "guide_01@auto.png")  # 跳过
        driver.swipe((self.info1(driver)*1830.0), (self.info2(driver)*80.0),(self.info1(driver)*1830.0), (self.info2(driver)*80.0), 10)
        sleep(2)
        driver.click((self.info1(driver)*960.0), (self.info2(driver)*760.0))  # 确定
        '''女神湖'''
        self.images_or_none(driver, "guide_13@auto.png")  # 女神湖
        driver.click((self.info1(driver)*760.0), (self.info2(driver)*700.0))  # 女神湖
        sleep(2)
        driver.click((self.info1(driver)*1500.0), (self.info2(driver)*970.0))  # 攻击
        sleep(6)
        driver.click((self.info1(driver)*700.0), (self.info2(driver)*700.0))  # 加入新勇士
        sleep(2)
        driver.click((self.info1(driver)*1600.0), (self.info2(driver)*880.0))  # 开战
        sleep(8)
        driver.click((self.info1(driver)*120.0), (self.info2(driver)*980.0))  # 坦克出战
        sleep(8)
        driver.click((self.info1(driver)*320.0), (self.info2(driver)*980.0))  # 召唤勇者1
        sleep(2)
        driver.click((self.info1(driver)*530.0), (self.info2(driver)*980.0))  # 召唤勇者2
        self.images_or_none(driver, "guide_14@auto.png")  # 退出战斗
        driver.click((self.info1(driver)*1650.0), (self.info2(driver)*950.0))  # 退出战斗
        sleep(6)
        driver.click(500,500)  # 任意键
        self.images_or_none(driver, "guide_15@auto.png")  # 返回
        driver.click((self.info1(driver)*90.0), (self.info2(driver)*40.0))  # 返回
        log.info("引导完成")
        #####################################################################################################
        # else:
        #     log.info("不用引导")
        if self.wait_gone_images(driver, 'guide_15@auto.png'):
            log.info('游戏引导成功')
            return 'ok'
        else:
            log.info('游戏引导失败')
            return None










