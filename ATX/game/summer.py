#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep,time
import public.methods as public
from public import logutils
import os
log = logutils.getLogger(__name__)

class Game(public.Methods):
    def guide(self,driver):
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
        '''创建昵称'''
        self.images_or_none(driver, "guide_01@auto.png")  # 等待输入名字
        driver.click((x*900), (y*500))  # 点击骰子
        sleep(1)
        driver.click((x*150), (y*1330))  # 射手座
        sleep(1)
        driver.click((x*540), (y*1850))  # 确定
        sleep(3)
        driver.long_click((x*1020), (y*1880))  # 点击关闭
        sleep(3)
        for i in range(11):
            sleep(1)
            driver.click((x*540), (y*1470))  # 下标
        '''尤塞塔工作室'''
        sleep(1)
        driver.click((x*250), (y*450))  # 尤塞塔工作室
        sleep(2)
        driver.click((x*850), (y*1440))  # 开始旅程
        sleep(2)
        for i in range(50):
            sleep(1)
            driver.click((x*540), (y*1470))  # 下标
        sleep(2)
        driver.click((x*740), (y*890))  # 确定
        '''服装设计师'''
        sleep(3)
        driver.click((x*720), (y*460))  # 连衣裙分类
        sleep(1)
        driver.click((x*940), (y*340))  # 换上
        sleep(1)
        driver.long_click((x*940), (y*340))  # 长按
        sleep(1)
        driver.click((x*720), (y*320))  # 头发
        sleep(1)
        driver.click((x*940), (y*340))  # 换上
        sleep(1)
        driver.click((x*620), (y*1830))  # 换好了
        self.images_or_none(driver, "guide_02@auto.png")
        for i in range(3):
            driver.click(500, 500)  # 任意键
            sleep(1)
        sleep(2)
        driver.click((x*550), (y*1840))  # 继续游戏
        '''过关奖励'''
        sleep(2)
        driver.click((x*1000), (y*150))  # 过关奖励
        sleep(2)
        driver.click((x*850), (y*710))  # 领取
        sleep(2)
        for i in range(2):
            driver.click(500, 500)  # 任意键
            sleep(2)
        sleep(2)
        driver.click((x*560), (y*1720))  # 点击空白处关闭
        '''丽斯帕特的占卜屋'''
        sleep(2)
        driver.click((x*630), (y*530))  # 丽斯帕特的占卜屋
        sleep(2)
        for i in range(10):
            sleep(1)
            driver.click((x*560), (y*1720))  # 点击空白处关闭
        sleep(2)
        driver.click((x*850), (y*1440))  # 开始旅程
        sleep(1)
        for i in range(28):
            sleep(1)
            driver.click((x*540), (y*1470))  # 下标
        sleep(2)
        driver.click((x*740), (y*890))  # 确定
        '''服装商城'''
        sleep(2)
        driver.click((x*950), (y*1740))  # 服装商城
        sleep(2)
        driver.long_click((x*290), (y*1850))  # 连衣裙
        sleep(2)
        driver.long_click((x*660), (y*440))  # 分红管家
        sleep(2)
        driver.long_click((x*260), (y*1650))  # 购买
        sleep(2)
        driver.long_click((x*70), (y*88))  # 返回
        sleep(2)
        driver.click((x*720), (y*460))  # 连衣裙分类
        sleep(1)
        driver.click((x*940), (y*340))  # 换上
        sleep(1)
        driver.click((x*620), (y*1830))  # 换好了
        self.images_or_none(driver, "guide_02@auto.png")
        for i in range(3):
            driver.click(500, 500)  # 任意键
            sleep(2)
        driver.click((x*550), (y*1840))  # 继续游戏
        '''精灵扭蛋 '''
        sleep(2)
        driver.click((x*100), (y*1800))  # 主页
        sleep(2)
        driver.click((x*590), (y*580))  # 精灵扭蛋
        sleep(2)
        driver.click((x*290), (y*1420))  # 免费扭一个
        sleep(5)
        for i in range(3):
            driver.click(500, 500)  # 任意键
            sleep(2)
        driver.click((x*1038), (y*666))  # 向右
        sleep(2)
        driver.click((x*290), (y*1420))  # 免费扭一个
        sleep(5)
        for i in range(3):
            driver.click(500, 500)  # 任意键
            sleep(2)
        driver.click((x*960), (y*150))  # 徽记兑换
        sleep(2)
        for i in range(3):
            driver.click(500, 500)  # 任意键
            sleep(2)
        driver.click((x*80), (y*90))  # 返回
        sleep(2)
        driver.click((x*80), (y*90))  # 返回
        '''化妆盒'''
        sleep(2)
        driver.click((x*250), (y*1700))  # 化妆盒
        sleep(2)
        for i in range(3):
            driver.click(500, 500)  # 任意键
            sleep(2)
        driver.click((x*120), (y*220))  # 提示
        sleep(2)
        driver.click((x*80), (y*90))  # 返回
        '''开始故事'''
        sleep(2)
        driver.click((x*369), (y*1350))  # 开始故事
        sleep(2)
        driver.click((x*960), (y*750))  # 爱心标志
        for i in range(10):
            sleep(1)
            driver.click((x*540), (y*1470))  # 下标
        sleep(2)
        driver.click((x*540), (y*480))  # 要好关系
        for i in range(4):
            sleep(1)
            driver.click((x*540), (y*1470))  # 下标
        sleep(2)
        '''支线任务'''
        driver.click((x*870), (y*540))  # 支线任务
        for i in range(22):
            sleep(1)
            driver.click((x*540), (y*1470))  # 下标
        sleep(2)
        driver.click((x*540), (y*640))  # 选A
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        if self.wait_gone_images(driver, 'guide_001@auto.png'):
            log.info('游戏引导结束')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None