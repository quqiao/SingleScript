#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
import os
import configure
log = logutils.getLogger(__name__)

class Game(public.Methods):

    def info1(self, driver):
        cmd = "adb -s %s shell wm size" % configure.device_name
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[1]
        g = float(f)
        x = g/1920.0
        return x

    def info2(self, driver):
        cmd = "adb -s %s shell wm size" % configure.device_name
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[0]
        g = float(f)
        y = g/1080.0
        return y

    def guide(self, driver):
        driver.click(self.info1(driver)*960, self.info1(driver)*880)  # 战场公告
        for i in range(10):
            for i in range(10):
                driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 完成前置
            if self.images_or_none(driver, "guide_01@auto.png"):
                break
        sleep(2)
        driver.click(self.info1(driver)*960, self.info1(driver)*950)  # 我知道了
        sleep(1)
        driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 我知道了
        sleep(2)
        '''教学'''
        driver.long_click(self.info1(driver)*290, self.info1(driver)*800)  # 长按移动
        sleep(2)
        driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 我知道了
        sleep(1)
        driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 我知道了
        sleep(1)
        driver.long_click(self.info1(driver)*290, self.info1(driver)*800)  # 长按移动
        sleep(1)
        driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 攻击
        sleep(1)
        driver.long_click(self.info1(driver)*290, self.info1(driver)*800)  # 长按移动
        sleep(2)
        driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 我知道了
        sleep(2)
        driver.long_click(self.info1(driver)*290, self.info1(driver)*800)  # 长按移动
        for i in range(40):
            driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 攻击
        sleep(1)
        driver.long_click(self.info1(driver)*290, self.info1(driver)*800)  # 长按移动
        sleep(2)
        driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 我知道了
        sleep(1)
        driver.long_click(self.info1(driver)*290, self.info1(driver)*800)  # 长按移动
        sleep(1)
        driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 我知道了
        sleep(1)
        driver.long_click(self.info1(driver)*290, self.info1(driver)*800)  # 长按移动
        for i in range(25):
            driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 攻击
        sleep(1)
        driver.click(self.info1(driver)*960, self.info1(driver)*880)  # 确定完成
        '''引导操作'''
        for i in range(5):
            driver.click(500, 500)  # 任意键
        sleep(2)
        driver.click(self.info1(driver)*960, self.info1(driver)*700)  # 战利品确定
        sleep(2)
        for i in range(5):
            driver.click(500, 500)  # 任意键
        sleep(2)
        driver.click(self.info1(driver)*580, self.info1(driver)*980)  # 五星
        sleep(2)
        driver.click(self.info1(driver)*520, self.info1(driver)*80)  # 名牌
        sleep(2)
        driver.click(self.info1(driver)*520, self.info1(driver)*430)  # 解锁
        sleep(2)
        driver.click(self.info1(driver)*520, self.info1(driver)*430)  # 装备
        sleep(2)
        driver.click(self.info1(driver)*1800, self.info1(driver)*1000)  # 返回
        sleep(2)
        for i in range(5):
            driver.click(500, 500)  # 任意键
        '''训练赛'''
        while ( 0<1 ):
            driver.click(self.info1(driver)*950, self.info1(driver)*950)  # 知道了
            if self.images_or_none(driver,"guide_02@auto.png"):
                break
        sleep(2)
        driver.click(self.info1(driver)*960, self.info1(driver)*880)  # 确定完成
        '''引导操作'''
        for i in range(5):
            driver.click(500, 500)  # 任意键
        sleep(2)
        driver.click(self.info1(driver)*960, self.info1(driver)*700)  # 战利品确定
        sleep(2)
        for i in range(5):
            driver.click(500, 500)  # 任意键
        sleep(2)
        driver.click(self.info1(driver)*420, self.info1(driver)*980)  # 人物
        sleep(1)
        driver.click(self.info1(driver)*1620, self.info1(driver)*580)  # 右转
        sleep(1)
        driver.click(self.info1(driver)*1620, self.info1(driver)*580)  # 右转
        sleep(1)
        driver.click(self.info1(driver)*1620, self.info1(driver)*580)  # 右转
        sleep(1)
        driver.click(self.info1(driver)*320, self.info1(driver)*890)  # 雇佣
        sleep(1)
        driver.click(self.info1(driver)*320, self.info1(driver)*890)  # 前往战场
        sleep(2)
        for i in range(5):
            driver.click(500, 500)  # 任意键
        sleep(1)
        driver.click(self.info1(driver)*1690, self.info1(driver)*960)  # 开始战斗
        '''训练赛'''
        sleep(1)
        driver.click(self.info1(driver)*1450, self.info1(driver)*760)  # 训练赛
        while ( 0<1 ):
            driver.click(self.info1(driver)*1680, self.info1(driver)*480)  # 知道了
            sleep(1)
            driver.click(self.info1(driver)*1680, self.info1(driver)*480)  # 知道了
            if self.images_or_none(driver, "guide_02@auto.png"):
                break
        sleep(2)
        driver.click(self.info1(driver)*960, self.info1(driver)*880)  # 确定完成
        ''''''
        sleep(2)
        for i in range(5):
            driver.click(500, 500)  # 任意键
        sleep(2)
        driver.click(self.info1(driver)*960, self.info1(driver)*700)  # 战利品确定
        sleep(2)
        for i in range(5):
            driver.click(500, 500)  # 任意键
        sleep(1)
        driver.click(self.info1(driver)*80, self.info1(driver)*980)  # 房子
        sleep(1)
        driver.click(self.info1(driver)*350, self.info1(driver)*790)  # 500金币
        sleep(6)
        driver.click(self.info1(driver)*960, self.info1(driver)*1000)  # 确定
        sleep(1)
        driver.click(self.info1(driver)*200, self.info1(driver)*100)  # 返回
        sleep(2)
        for i in range(5):
            driver.click(500, 500)  # 任意键
        '''升级箱'''
        sleep(1)
        driver.click(self.info1(driver)*250, self.info1(driver)*980)  # 升级箱
        sleep(2)
        for i in range(5):
            driver.click(500, 500)  # 任意键
        sleep(1)
        driver.click(self.info1(driver)*650, self.info1(driver)*260)  # 强化模块
        sleep(1)
        driver.click(self.info1(driver)*1500, self.info1(driver)*280)  # 生命
        sleep(1)
        driver.click(self.info1(driver)*160, self.info1(driver)*110)  # 返回
        for i in range(5):
            driver.click(500, 500)  # 任意键
        sleep(1)
        driver.click(self.info1(driver)*1690, self.info1(driver)*960)  # 开始战斗
        '''排位赛'''
        sleep(1)
        driver.click(self.info1(driver)*550, self.info1(driver)*620)  # 排位赛
        sleep(1)
        driver.click(self.info1(driver)*960, self.info1(driver)*1000)  # 撤退





