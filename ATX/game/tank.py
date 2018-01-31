#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
import os
log = logutils.getLogger(__name__)

class Game(public.Methods):
    def guide(self, driver):
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
        '''开始引导'''
        self.images_or_none(driver, "guide_01@auto.png")  # 等待创建帐号
        driver.click((x*270.0), (y*260.0))  # 选择初始成员
        sleep(2)
        driver.click((x*1570.0), (y*930.0))  # 确认选择
        sleep(2)
        driver.click((x*1210.0), (y*500.0))  # 骰子
        sleep(2)
        driver.click((x*960.0), (y*620.0))  # 创建
        sleep(2)
        self.images_or_none(driver, "guide_02@auto.png")  # 等待跳过
        driver.click((x*1820.0), (y*60.0))  # 跳过
        sleep(10)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        '''开始教学'''
        sleep(2)
        driver.swipe((x*1700.0), (y*560.0), (x*1000.0), (y*540.0), 100)  # 向左滑动
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.click((x*1720.0), (y*920.0))  # 开炮
        sleep(2)
        driver.swipe((x*1480.0), (y*510.0), (x*1680.0), (y*510.0), 100)  # 向右滑动
        sleep(2)
        driver.click((x*1720.0), (y*920.0))  # 开炮
        sleep(2)
        driver.click((x*1580.0), (y*710.0))  # 瞄准
        sleep(2)
        driver.click((x*1720.0), (y*920.0))  # 开炮
        sleep(2)
        driver.click((x*1580.0), (y*710.0))  # 瞄准
        sleep(2)
        driver.click((x*1720.0), (y*920.0))  # 开炮
        sleep(2)
        driver.click((x*1580.0), (y*710.0))  # 瞄准
        sleep(2)
        driver.click((x*1720.0), (y*920.0))  # 开炮
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.click((x*1580.0), (y*710.0))  # 瞄准
        sleep(2)
        driver.swipe((x*270.0), (y*620.0), (x*270.0), (y*620.0), 1000)  # 长按移动
        sleep(2)
        driver.click((x*1720.0), (y*920.0))  # 开炮
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.swipe((x*320.0), (y*620.0), (x*320.0), (y*620.0), 1000)  # 长按移动
        sleep(2)
        driver.click((x*1720.0), (y*920.0))  # 开炮
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.swipe((x*320.0), (y*620.0), (x*320.0), (y*620.0), 1000)  # 长按移动
        sleep(2)
        driver.click((x*1720.0), (y*920.0))  # 开炮
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        '''备战'''
        driver.click((x*1050.0), (y*1030.0))  # 备战
        sleep(2)
        driver.click((x*210.0), (y*780.0))  # 2号位炮手
        sleep(2)
        driver.click((x*800.0), (y*550.0))  # 上阵的成员
        sleep(2)
        driver.click((x*60.0), (y*30.0))  # 返回
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        '''车库'''
        driver.click((x*580.0), (y*1030.0))  # 车库
        sleep(2)
        driver.click((x*660.0), (y*900.0))  # 轻型
        sleep(2)
        driver.click((x*460.0), (y*1020.0))  # 坦克
        sleep(2)
        driver.click((x*1800.0), (y*280.0))  # 改造
        sleep(2)
        driver.click((x*1535.0), (y*240.0))  # 强化1
        sleep(2)
        driver.click((x*190.0), (y*990.0))  # 强化2
        sleep(2)
        driver.click((x*190.0), (y*990.0))  # 强化2
        sleep(2)
        driver.click((x*60.0), (y*30.0))  # 返回
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        '''世界版图'''
        driver.click((x*1550.0), (y*420.0))  # 世界版图
        sleep(2)
        driver.click((x*1235.0), (y*685.0))  # 经典模式
        sleep(15)
        driver.click((x*1300.0), (y*1000.0))  # 开始作战
        sleep(2)
        self.images_or_none(driver, "guide_03@auto.png")  # 等待跳过
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.swipe((x*280.0), (y*620.0), (x*280.0), (y*620.0), 100)  # 前进
        sleep(2)
        driver.click((x*970.0), (y*870.0))  # 暴走
        sleep(2)
        driver.swipe((x*280.0), (y*620.0), (x*280.0), (y*620.0), 100)  # 前进
        sleep(2)
        driver.swipe((x*280.0), (y*620.0), (x*280.0), (y*620.0), 100)  # 前进
        sleep(2)
        driver.swipe((x*280.0), (y*620.0), (x*280.0), (y*620.0), 100)  # 前进
        sleep(2)
        for i in range(100):
            driver.click((x*1720.0), (y*920.0))  # 开炮
            driver.click((x*1580.0), (y*710.0))  # 瞄准
            if self.exist(driver, "guide_04@auto.png"):
               break
        sleep(2)
        driver.click((x*1460.0), (y*930.0))  # 退出
        sleep(10)
        '''任务'''
        driver.click((x*100.0), (y*1030.0))  # 任务
        sleep(2)
        driver.click((x*100.0), (y*360.0))  # 主线
        sleep(2)
        driver.click((x*60.0), (y*30.0))  # 返回
        sleep(2)
        driver.click((x*1810.0), (y*60.0))  # 关闭1
        sleep(2)
        driver.click((x*1530.0), (y*250.0))  # 关闭2
        sleep(2)
        if self.wait_gone_images(driver, 'guide_04@auto.png'):
            log.info('游戏引导结束')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None











