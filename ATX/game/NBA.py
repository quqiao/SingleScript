#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
import os
log = logutils.getLogger(__name__)


class Game(public.Methods):
    def game_update(self,driver):
        sleep(10)
        self.click_images(driver,"game_update_01@auto.png")
        sleep(30)
        driver.click(0.5,0.5)
        sleep(2)
        driver.click(0.5,0.5)
        self.click_images(driver,"game_update_02@auto.png") 
        sleep(2)
        driver.swipe(500,439,800,439,50)  # 滑动调整年龄
        self.click_images(driver,"game_update_03@auto.png")
        self.click_images(driver,"game_update_04@auto.png")
        if self.wait_gone_images(driver,'game_update_04@auto.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
    def game_pre(self,driver):
        self.click_images(driver,"game_pre_01@auto.png")  # 继续
        if self.wait_gone_images(driver,'game_pre_01@auto.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
        
    def guide(self,driver):
        '''引导'''
        ##########################################################
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
        ##########################################################
        # if self.images_or_none(driver,'guide_001@auto.png'):
        '''教程-运球'''
        while (0<1):
            if self.images_or_none(driver, 'guide_01@auto.png'):
                break
        driver.click(x*980, y*880)  # 继续
        sleep(2)
        driver.click(x*963, y*885)  # 开始
        sleep(2)
        self.images_or_none(driver, "guide_02@auto.png")
        driver.click(500, 500)    # 点击任意继续
        sleep(1)
        driver.swipe(x*234, y*895, x*350, y*925, 70)    #长按移动
        sleep(1)
        driver.swipe(x*234, y*895, x*340, y*800, 70)    #长按移动
        '''教程-投篮'''
        sleep(5)
        driver.click(500, 500)    #点击任意继续
        sleep(1)
        driver.swipe(x*1746, y*710, x*1746, y*710, 20)    #长按跳投
        '''教程-三分投篮'''
        sleep(6)
        driver.click(500, 500)    #点击任意继续
        sleep(3)
        driver.swipe(x*234, y*895, x*330, y*924, 40)    #长按移动
        sleep(2)
        driver.swipe(x*1746, y*710, x*1746, y*710, 20)    #长按跳投
        '''教程-如何冲刺'''
        sleep(6)
        driver.click(500, 500)    #点击任意继续
        sleep(3)
        driver.swipe(x*1746, y*920, x*1746, y*920, 300)    #长按冲刺
        '''教程-如何灌篮'''
        sleep(6)
        driver.click(500, 500)    #点击任意继续
        sleep(3)
        driver.swipe(x*1746, y*920, x*1746, y*920, 25)   # 长按冲刺
        driver.swipe(x*1746, y*920, x*1746, y*680, 30)    # 灌篮
        '''教程-教程结束'''
        sleep(6)
        driver.click(500, 500)    # 点击任意继续
        sleep(3)
        driver.swipe(x*1746, y*920, x*1746, y*920, 25)   # 长按冲刺
        driver.swipe(x*1746, y*920, x*1746, y*680, 30)    # 灌篮
        '''教程结果'''
        sleep(5)
        driver.click(x*1298, y*975)  # 继续
        '''组建球队'''
        sleep(6)
        driver.click(x*959, y*878)  # 继续
        sleep(2)
        driver.click(x*900, y*420)  # 队名输入框
        sleep(1)
        driver.type('wedfg')
        sleep(1)
        driver.click(500, 500)  # 任意键
        sleep(1)
        driver.click(x*950, y*850)  # 继续
        sleep(5)
        driver.click(x*1280, y*468)  # 火箭队
        sleep(1)
        driver.click(x*960, y*990)  # 选择并继续
        '''商店'''
        sleep(6)
        driver.swipe(x*1796, y*38, x*1796, y*38, 10)  # 商店
        sleep(8)
        driver.click(x*280, y*680)  # 领取
        sleep(8)
        driver.click(x*1680, y*1025)  # 打开卡包
        sleep(8)
        driver.click(x*1680, y*1025)  # 全部显示
        '''升级球队'''
        sleep(3)
        driver.click(x*1190, y*1020)  # 升级球队
        sleep(5)
        driver.click(x*1680, y*1025)  # 继续
        sleep(3)
        driver.click(x*890, y*430)  # 我的球队
        sleep(3)
        driver.click(x*630, y*460)  # 可升级球员
        sleep(3)
        driver.click(x*1289, y*126)  # 训练球员
        sleep(2)
        driver.click(x*810, y*480)  # 升级球员
        sleep(2)
        driver.click(x*122, y*955)  # 训练点数
        sleep(1)
        driver.click(x*1135, y*720)  # 应用训练
        sleep(2)
        driver.click(x*665, y*889)  # 升级
        sleep(5)
        driver.click(x*980, y*800)  # 点击继续
        '''在线赛事'''
        sleep(3)
        driver.click(x*855, y*898)  # 在线赛事
        sleep(3)
        driver.click(x*720, y*990)  # 继续
        sleep(3)
        driver.click(x*960, y*680)  # 好的
        for i in range(6):
            sleep(2)
            driver.click(x*970, y*980)  # 领取并完成
        log.info('游戏引导完成')
        # self.click_images(driver,"guide_020@auto.png")
        # else:
        #     driver.click(1320,980)  # 在线赛事
        #     sleep(2)
        #     driver.click(960,660)  # 好的
        #     log.info('游戏已过引导')
        if self.wait_gone_images(driver, 'guide_02@auto.png'):
            log.info('引导成功')
            return 'ok'
        else:
            log.info('引导失败')
            return None

    def basicFunction(self, driver):
        sleep(1)
        driver.click(15,585)  # 打开菜单
        sleep(2)
        driver.click(120,730)  # 我的球队
        sleep(2)
        driver.click(15,585)  # 打开菜单
        sleep(2)
        driver.click(120,840)  # 我的球队
        sleep(2)
        driver.click(15,585)  # 打开菜单
        sleep(2)
        driver.click(120,185)  # 在线赛事
        sleep(2)
        driver.click(1625,45)  # 篮球
        sleep(2)
        driver.click(40,40)  # 返回
        sleep(2)
        driver.click(1700,60)  # 邮件
        sleep(2)
        driver.click(1570,86)  # 关闭
        sleep(2)
        driver.click(1790,45)  # 购物车
        sleep(2)
        driver.click(40,40)  # 返回
        sleep(2)
        if self.wait_gone_images(driver,'guide_001@auto.png'):
            log.info('基本功能检查成功')
            return 'ok'
        else:
            log.info('基本功能检查失败')
            return None

    def live(self, driver):
        log.info('NBA暂时没有直播')
        if self.wait_gone_images(driver, 'guide_001@auto.png'):
            log.info('直播忽略成功')
            return 'ok'
        else:
            log.info('直播忽略失败')
            return None

    def gonglue(self, driver):
        log.info('NBA暂时没有攻略')
        if self.wait_gone_images(driver, 'guide_001@auto.png'):
            log.info('攻略忽略成功')
            return 'ok'
        else:
            log.info('攻略忽略失败')
            return None

    def saishi(self, driver):
        log.info('NBA暂时没有赛事')
        if self.wait_gone_images(driver, 'guide_001@auto.png'):
            log.info('赛事忽略成功')
            return 'ok'
        else:
            log.info('赛事忽略失败')
            return None

    def lingzuan(self, driver):
        log.info('NBA暂时没有领钻')
        if self.wait_gone_images(driver,'guide_001@auto.png'):
            log.info('领钻忽略成功')
            return 'ok'
        else:
            log.info('领钻忽略失败')
            return None

    def store(self, driver):
        log.info('NBA暂时没有市场')
        if self.wait_gone_images(driver,'guide_001@auto.png'):
            log.info('市场忽略成功')
            return 'ok'
        else:
            log.info('市场忽略失败')
            return None

    def talking(self, driver):
        log.info('NBA暂时没有对话')
        if self.wait_gone_images(driver,'guide_001@auto.png'):
            log.info('对话忽略成功')
            return 'ok'
        else:
            log.info('对话忽略失败')
            return None
