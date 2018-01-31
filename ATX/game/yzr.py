#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
import os
log = logutils.getLogger(__name__)


class Game(public.Methods):
    def game_update(self, driver):
        sleep(10)
        driver.click(500,500)
        sleep(5)
        driver.click(500,500)
        self.click_images(driver,"game_update_01@auto.png")
        self.click_images(driver,"game_update_02@auto.png")
        self.click_images(driver,"game_update_01@auto.png")
        sleep(10)
        driver.click(0.5,0.5)
        self.click_images(driver,"game_update_03@auto.png")
        if self.wait_gone_images(driver,'game_update_02@auto.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
    def game_pre(self, driver):
        self.click_images(driver, "game_pre_01@auto.png")
        if self.wait_gone_images(driver, 'game_update_01@auto.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
        
    def guide(self, driver):
        '''创建人物'''
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
        # sleep(3)
        # if self.images_or_none(driver, "guide_001@auto.png"):
        ############################################################
        self.images_or_none(driver, "guide_001@auto.png")  # 等待输入名字
        driver.click((x*1295.0), (y*305.0))  # 骰子
        sleep(2)
        driver.click((x*960.0), (y*980.0))  # 进入游戏
        sleep(2)
        while ( 0<1 ):
            driver.click(500, 500)  # 任意键
            if self.images_or_none(driver, "guide_002@auto.png"):
                break
        sleep(2)
        driver.long_click((x*1800.0), (y*55.0))  # 跳过对话
        '''教学'''
        sleep(2)
        driver.long_click((x*540.0), (y*960.0))  # 移动角色
        for i in range(240):
            driver.click((x*1645), (y*926))  # 攻击
        sleep(2)
        driver.click((x*1770), (y*720))  # 第一特殊技能
        for i in range(400):
            driver.click((x*1645), (y*926))  # 攻击
        driver.click((x*1450), (y*810))  # 第三特殊技能-霸
        sleep(5)
        driver.click((x*1600), (y*700))  # 第二特殊技能
        sleep(5)
        driver.click((x*1770), (y*720))  # 第一特殊技能
        sleep(1)
        for i in range(360):
            driver.click((x*1645), (y*926))  # 攻击
        '''战斗2'''
        sleep(2)
        driver.click((x*1440), (y*980))  # 第四特殊技能-奥义
        sleep(1)
        for i in range(460):
            driver.click((x*1645), (y*926))  # 攻击
        sleep(1)
        driver.click((x*1450), (y*810))  # 第三特殊技能-霸
        sleep(5)
        driver.long_click((x*1840), (y*930))  # 跳跃
        sleep(2)
        for i in range(500):
            driver.click((x*1645), (y*926))  # 攻击
        '''战斗3'''
        sleep(1)
        driver.click((x*1440), (y*980))  # 唤醒
        for i in range(50):
            driver.click((x*1645), (y*926))  # 攻击
        ##########################################################
        for i in range(20):
            sleep(1)
            driver.swipe((x*530), (y*964), (x*530), (y*964), 40)  # 右移动
            for i in range(40):
                driver.click((x*1645), (y*926))  # 攻击
            sleep(1)
            driver.swipe((x*110), (y*964), (x*110), (y*964), 40)  # 左移动
            for i in range(40):
                driver.click((x*1645), (y*926))  # 攻击
        '''战斗4'''
        for i in range(50):
            driver.click((x*1645), (y*926))  # 攻击
        driver.swipe((x*530), (y*964), (x*530), (y*964), 50)  # 右移动
        for i in range(11):
            sleep(1)
            driver.swipe((x*530), (y*964), (x*530), (y*964), 30)  # 右移动
            for i in range(40):
                driver.click((x*1645), (y*926))  # 攻击
            sleep(1)
            driver.swipe((x*110), (y*964), (x*110), (y*964), 10)  # 左移动
            for i in range(30):
                driver.click((x*1645), (y*926))  # 攻击
        ###########################################################
        '''合成英雄'''
        sleep(2)
        driver.click((x*1460), (y*460))  # 合成英雄
        self.images_or_none(driver, "guide_003@auto.png")  # 等待故事剧情
        driver.long_click((x*1823), (y*990))  # 英雄
        sleep(3)
        driver.click((x*380), (y*360))  # 银月
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.click((x*90), (y*40))  # 返回
        '''故事剧情'''
        sleep(2)
        driver.click((x*900), (y*290))  # 故事剧情
        sleep(2)
        driver.click((x*820), (y*510))  # 魂篇
        sleep(2)
        driver.click((x*1010), (y*700))  # 第一幕
        sleep(2)
        driver.click((x*1550), (y*1000))  # 开始战斗
        sleep(2)
        '''战斗1-1'''
        sleep(15)
        for i in range(100):
            driver.click((x*1645), (y*926))  # 攻击
        sleep(2)
        driver.click((x*70), (y*160))  # 属性相克
        sleep(1)
        driver.click(500, 500)  # 任意键
        sleep(1)
        driver.click(500, 500)  # 任意键
        sleep(1)
        driver.click((x*990), (y*970))  # 换人
        for i in range(9):
            sleep(1)
            driver.swipe((x*530), (y*964), (x*530), (y*964), 20)  # 右移动
            sleep(1)
            driver.swipe((x*530), (y*964), (x*530), (y*964), 20)  # 右移动
            for i in range(40):
                driver.click((x*1645), (y*926))  # 攻击
            sleep(1)
            driver.swipe((x*110), (y*964), (x*110), (y*964), 20)  # 左移动
            for i in range(30):
                driver.click((x*1645), (y*926))  # 攻击
        sleep(1)
        driver.click((x*990), (y*970))  # 换人
        for i in range(16):
            sleep(1)
            driver.click((x*530), (y*964))  # 右移动
            sleep(0.5)
            driver.click((x*530), (y*964))  # 右移动
            for i in range(40):
                driver.click((x*1645), (y*926))  # 攻击
            sleep(1)
            driver.click((x*110), (y*964))  # 左移动
            sleep(0.5)
            driver.click((x*110), (y*964))  # 左移动
            for i in range(25):
                driver.click((x*1645), (y*926))  # 攻击
        '''酒馆'''
        sleep(1)
        driver.click((x*1460), (y*450))  # 前往酒馆
        self.images_or_none(driver, "guide_003@auto.png")  # 等待
        driver.click((x*680), (y*430))  # 英雄酒馆
        sleep(3)
        driver.click((x*770), (y*930))  # 请喝一杯
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(3)
        driver.click((x*770), (y*930))  # 请喝一杯
        sleep(2)
        driver.click(500, 500)  # 任意键
        sleep(3)
        driver.click((x*860), (y*850))  # 玉露酒
        self.images_or_none(driver, "guide_004@auto.png")
        driver.click((x*770), (y*930))  # 返回
        sleep(2)
        driver.click((x*70), (y*30))  # 返回
        sleep(2)
        driver.click(500, 500)  # 任意键
        sleep(2)
        driver.click(500, 500)  # 任意键
        sleep(2)
        driver.click((x*70), (y*30))  # 返回
        ##############################################
        # else:
        #     print '没有引导'
        #     driver.click(100,400)
        #     sleep(3)
        #     driver.click(100,400)
        ##############################################
        if self.wait_gone_images(driver,'guide_003@auto.png'):
            log.info('游戏引导结束')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
