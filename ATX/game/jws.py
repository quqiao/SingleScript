#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
import os
import configure
log = logutils.getLogger(__name__)



class Game(public.Methods):

    # def info1(self, driver):
    #     cmd = "adb -s %s shell wm size" %configure.device_name
    #     a = os.popen(cmd).read()
    #     c = a.split()
    #     d = c[2]
    #     e = d.split('x')
    #     f = e[1]
    #     g = float(f)
    #     x = g/1920.0
    #     return x
    #
    # def info2(self, driver):
    #     cmd = "adb -s %s shell wm size" %configure.device_name
    #     a = os.popen(cmd).read()
    #     c = a.split()
    #     d = c[2]
    #     e = d.split('x')
    #     f = e[0]
    #     g = float(f)
    #     y = g/1080.0
    #     return y

    def info1(self, driver):
        a = driver.info
        b = a.get(u'displayWidth')
        c = b/1920
        return c

    def info2(self, driver):
        a = driver.info
        b = a.get(u'displayHeight')
        c = b/1080.0
        return c

    def game_update(self, driver):
        sleep(40)
        self.images_or_none(driver, "game_update_01@auto.png")
        driver.click(self.info1(driver)*1120, self.info1(driver)*630)  # 提示更新确定
        sleep(20)
        self.images_or_none(driver, "game_update_02@auto.png")
        driver.click(self.info1(driver)*1120, self.info1(driver)*930)  # 公告确定
        if self.wait_gone_images(driver,'game_update_01@auto.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None

    def game_pre(self, driver):
        # sleep(20)
        self.images_or_none(driver, "game_pre_01@auto.png")
        driver.click(self.info1(driver)*950, self.info2(driver)*820)  # 更换服务器
        sleep(1)
        driver.click(self.info1(driver)*360, self.info2(driver)*780)  # 141-150区
        sleep(1)
        # driver.click(self.info1(driver)*760, self.info1(driver)*300)  # 乱世佳人
        driver.click(self.info1(driver)*1350, self.info2(driver)*280)  # 铁血沙场
        sleep(1)
        driver.click(self.info1(driver)*960, self.info2(driver)*940)  # 进入游戏
        self.images_or_none(driver, 'game_pre_02@auto.png')
        sleep(1)
        driver.click(500, 500)  # 点击屏幕继续
        sleep(3)
        driver.click(500, 500)  # 点击屏幕继续
        sleep(1)
        driver.click(self.info1(driver)*1820, self.info1(driver)*60)  # 跳过
        if self.wait_gone_images(driver, 'game_pre_02@auto.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None

    def guide(self,driver):
        '''开始引导，第一场战斗'''
        ###########################################################
        cmd = "adb shell wm size"
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[1]
        g = float(f)
        f1 = e[0]
        g1 = float(f1)
        x = g/1920.0
        y = g1/1080.0
        ############################################################
        # a = driver.info
        # print a
        # b1 = a.get( u'displayHeight')
        # print b1
        # y = b1/1080.0
        # print y
        # a2 = driver.info
        # print a2
        # b2 = a2.get( u'displayWidth')
        # print b2
        # x = b2/1920.0
        # print x
        ############################################################
        #if self.images_or_none(driver, 'guide_001@auto.png'):
        '''开始引导'''
        while ( 0<1 ):
            driver.click((x*300.0), (y*800.0))
            driver.click((x*300.0), (y*800.0))
            driver.click((x*300.0), (y*800.0))
            if self.images_or_none(driver, "guide_001@auto.png"):
                break
        driver.click((x*300.0), (y*800.0))  # 推动摇杆
        sleep(1)
        driver.click((x*1800.0), (y*950.0))  # 攻击
        for i in range(1000):
            driver.click((x*1690.0), (y*720.0))  # 鬼神惊
            for i in range(20):
                driver.click((x*1790.0), (y*950.0))  # 攻击
            if self.exist(driver, 'guide_002@auto.png'):
                driver.long_click((x*1820.0), (y*480.0))  # 逆鳞无双
                break
        '''第二场战斗'''
        for i in range(1000):
            driver.swipe((x*500.0), (y*682.0), (x*500.0), (y*300.0), 10)
            for i in range(40):
                driver.click((x*1790.0), (y*950.0))  # 攻击
            if self.exist(driver,'guide_003@auto.png'):
                driver.click((x*1680.0), (y*720.0))  # 鬼神惊
                break
        '''第三场战斗'''
        for i in range(1000):
            driver.swipe((x*500.0), (y*682.0), (x*500.0), (y*300.0), 10)
            driver.click((x*1690.0), (y*720.0))  # 鬼神惊
            for i in range(20):
                driver.click((x*1790.0), (y*950.0))  # 攻击
            if self.exist(driver, 'guide_004@auto.png'):
                driver.long_click((x*1850.0), (y*180.0))  # 切换视角
                break
        for i in range(1000):
            driver.swipe((x*500.0), (y*682.0), (x*500.0), (y*300.0), 10)
            driver.click((x*1690.0), (y*720.0))  # 鬼神惊
            for i in range(20):
                driver.click((x*1790.0), (y*950.0))  # 攻击
            if self.exist(driver,'guide_005@auto.png'):
                driver.long_click((x*1830.0), (y*660.0))  # 十文字斩
                break

        for i in range(1000):
            driver.swipe((x*500.0), (y*682.0), (x*500.0), (y*300.0), 10)
            driver.click((x*1690.0), (y*720.0))  # 鬼神惊
            for i in range(39):
                driver.click((x*1790.0), (y*950.0))  # 攻击
            if self.exist(driver, 'guide_006@auto.png'):
                driver.click((x*1305.0), (y*475.0))  # 点击随机骰子
                break
        '''出征'''
        sleep(2)
        driver.click((x*960.0), (y*690.0))  # 出征
        self.images_or_none(driver, 'guide_010@auto.png')
        driver.click(500, 500)  # 随机
        sleep(2)
        driver.click((x*190.0), (y*380.0))  # 颍川之战
        sleep(2)
        driver.click((x*620.0), (y*330.0))  # 颍川之战1-1
        sleep(2)
        driver.click((x*1620.0), (y*800.0))  # 进入
        sleep(2)
        driver.click((x*1750.0), (y*1000.0))  # 确定
        sleep(5)
        '''第四场战斗'''
        for i in range(1000):
            driver.swipe((x*500.0), (y*682.0), (x*500.0), (y*300.0), 10)
            driver.click((x*1690.0), (y*720.0))  # 鬼神惊
            for i in range(50):
                driver.click((x*1789.0), (y*950.0))
            if self.exist(driver, 'guide_007@auto.png'):
                driver.click((x*1650.0), (y*1020.0))  # 装备
                break
        '''装备'''
        sleep(2)
        driver.click((x*100.0), (y*820.0))  # 空框1
        sleep(2)
        driver.click((x*1500.0), (y*320.0))  # 护腕
        sleep(2)
        driver.click((x*755.0), (y*910.0))  # 装备
        sleep(3)
        driver.click((x*100.0), (y*620.0))  # 空框2
        sleep(2)
        driver.click((x*1500.0), (y*320.0))  # 戒指
        sleep(2)
        driver.click((x*755.0), (y*910.0))  # 装备
        sleep(2)
        driver.click((x*125.0), (y*50.0))  # 返回
        '''颍川别战'''
        sleep(2)
        driver.click((x*185.0), (y*380.0))  # 颍川之战
        sleep(5)
        for i in range(10):
            driver.click(500, 500)  # 随机
            sleep(1)
        self.images_or_none(driver, "guide_011@auto.png")
        driver.click((x*1230.0), (y*820.0))  # 点击屏幕继续
        sleep(3)
        driver.click((x*185.0), (y*380.0))  # 决战傀儡
        sleep(2)
        driver.click((x*310.0), (y*410.0))  # 颍川别战
        sleep(2)
        driver.click((x*1620.0), (y*800.0))  # 进入
        sleep(2)
        driver.click((x*1750.0), (y*1000.0))  # 确定
        sleep(5)
        self.images_or_none(driver, "guide_008@auto.png")
        for i in range(10):
            sleep(1)
            driver.click((x*1790.0), (y*950.0))  # 攻击
        sleep(2)
        driver.click((x*960.0), (y*1030.0))  # 自动战斗
        sleep(40)
        self.images_or_none(driver, "guide_008@auto.png")
        '''决战傀儡'''
        for i in range(1000):
            for i in range(20):
                driver.click(500, 500)  # 随机
            if self.exist(driver, 'guide_009@auto.png'):
                driver.click((x*1670.0), (y*1000.0))  # 继续
                break
        self.images_or_none(driver, "guide_012@auto.png")
        driver.click((x*280.0), (y*620.0))  # 决战傀儡1-2
        sleep(2)
        driver.click((x*1620.0), (y*800.0))  # 进入
        sleep(2)
        driver.click((x*1750.0), (y*1000.0))  # 确定
        sleep(90)  # 等待战斗结束
        for i in range(10):
            driver.click(500, 500)  # 随机
            sleep(1)
        self.images_or_none(driver, "guide_009@auto.png")
        driver.click((x*1670.0), (y*1000.0))  # 继续
        '''装备'''
        self.images_or_none(driver,"guide_007@auto.png")
        sleep(2)
        driver.click((x*1650.0), (y*1020.0))  # 装备
        sleep(2)
        driver.click((x*100.0), (y*620.0))  # 空框2
        sleep(2)
        driver.click((x*1500.0), (y*320.0))  # 戒指
        sleep(2)
        driver.click((x*1280.0), (y*910.0))  # 装备
        sleep(2)
        driver.click((x*125.0), (y*50.0))  # 返回
        sleep(2)
        driver.click((x*185.0), (y*380.0))  # 决战傀儡
        sleep(3)
        driver.click((x*1230.0), (y*820.0))  # 点击屏幕继续
        sleep(2)
        driver.click((x*185.0), (y*380.0))  # 江夏之战
        sleep(2)
        driver.click((x*185.0), (y*380.0))  # 江夏之战
        '''羌林杀机'''
        sleep(2)
        driver.click((x*630.0), (y*600.0))  # 羌林杀机
        sleep(2)
        driver.click((x*1620.0), (y*800.0))  # 进入
        sleep(2)
        driver.click((x*1750.0), (y*1000.0))  # 确定
        for i in range(1000):
            for i in range(20):
                driver.click(500, 500)  # 随机
            if self.exist(driver, 'guide_015@auto.png'):
                break
        sleep(2)
        driver.click((x*1670.0), (y*1000.0))  # 继续
        '''江夏之战'''
        sleep(6)
        driver.click((x*980.0), (y*460.0))  # 羌林杀机
        sleep(2)
        driver.click((x*1620.0), (y*800.0))  # 进入
        sleep(2)
        driver.click((x*1750.0), (y*1000.0))  # 确定
        for i in range(1000):
            for i in range(20):
                driver.click(500, 500)  # 随机
            if self.exist(driver, 'guide_016@auto.png'):
                break
        sleep(2)
        driver.click((x*1670.0), (y*1000.0))  # 继续
        self.images_or_none(driver, "guide_013@auto.png")
        driver.click((x*1730.0), (y*180.0))  # 关闭弹窗
        '''装备-一键强化'''
        sleep(2)
        driver.click((x*1650.0), (y*1000.0))  # 装备
        sleep(2)
        driver.click((x*430.0), (y*480.0))  # 强化
        sleep(2)
        driver.click((x*100.0), (y*620.0))  # 空框2
        sleep(2)
        driver.click((x*1710.0), (y*420.0))  # 一键强化
        sleep(2)
        driver.click((x*1710.0), (y*420.0))  # 一键强化
        sleep(2)
        driver.click((x*420.0), (y*270.0))  # 装备
        sleep(2)
        driver.click((x*1500.0), (y*310.0))  # 护腕
        sleep(2)
        driver.click((x*1270.0), (y*900.0))  # 护腕
        sleep(2)
        driver.click((x*125.0), (y*50.0))  # 返回
        ###############################################################
        # else:
        #     log.info('没有引导')
        ###############################################################
        if self.wait_gone_images(driver, 'guide_013@auto.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
            

    '''
    def basicFunction(self,driver):
        
    def live(self,driver):
        
    def gonglue(self,driver):
        
    def store(self,driver):
        
    def lingzuan(self,driver):
        
    def saishi(self,driver):
        
    def talking(self,driver):
    '''
