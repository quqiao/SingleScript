#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Game(public.Methods):
    def game_update(self,driver):
        sleep(10)
        self.click_images(driver,"game_update_01@auto.png")
        self.click_images(driver,"game_update_02@auto.png")
        if self.wait_gone_images(driver,'game_update_02@auto.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
    def game_pre(self,driver):
        sleep(15)
        self.click_images(driver, "game_pre_01@auto.png")
        if self.wait_gone_images(driver, 'game_pre_01@auto.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
    def guide(self,driver):
        '''创建人物'''
        sleep(5)
        if self.images_or_none(driver, 'guide_001@auto.png'):
            self.click_images(driver, "guide_001@auto.png")
            self.click_images(driver, "guide_002@auto.png")
            '''指导操作'''
            sleep(10)
            for i in range(6):
                sleep(1)
                driver.click(0.5,0.5)
            self.click_images(driver,"guide_003@auto.png")#点击屏幕继续
            sleep(1)
            driver.swipe(559, 653, 310, 923,50)#滑动攻击
            sleep(20)
            for i in range(3):
                sleep(1)
                driver.click(0.5,0.5)
            self.long_click_images(driver,"guide_004@auto.png")#长按爬行
            self.long_click_images(driver,"guide_004@auto.png")#长按爬行
            sleep(1)
            driver.click(0.5,0.5)
            driver.click(0.5,0.5)
            self.click_images(driver,"guide_005@auto.png")#连发弹
            driver.swipe(1122, 608, 887, 842,50)#滑动攻击
            sleep(20)
            driver.click(0.5,0.5)
            sleep(2)
            driver.click(0.5,0.5)
            self.click_images(driver,"guide_006@auto.png")#怒气值
            sleep(2)
            driver.swipe(934, 661, 735, 953,50)#滑动攻击
            sleep(6)
            for i in range(11):
                sleep(2)
                driver.click(500, 500)  # 点击任意键
            '''冒险'''
            self.click_images(driver, "guide_007@auto.png")
            self.click_images(driver, "guide_008@auto.png")
            '''第1-1关'''
            self.click_images(driver, "guide_009@auto.png")
            self.click_images(driver, "guide_010@auto.png")
            '''战斗'''
            sleep(9)
            for i in range(5):
                driver.click(500, 500)  # 点击任意键
                sleep(1)
            self.click_images(driver, "guide_011@auto.png")  # 飞行器
            self.click_images(driver, "guide_003@auto.png")  # 击屏幕继续
            sleep(3)
            driver.swipe(724, 806, 457, 1000, 50)
            sleep(15)
            for i in range(3):
                driver.click(0.5,0.5)
                sleep(1)
            self.click_images(driver,"guide_012@auto.png")#散射弹
            sleep(2)
            driver.swipe(1054, 659, 1423, 747, 50)#滑动攻击
            sleep(12)
            for i in range(3):
                driver.click(0.5,0.5)
                sleep(1)
            self.click_images(driver,"guide_013@auto.png")#威力弹
            sleep(2)
            driver.swipe(1026, 662, 1285, 880,50)
            sleep(10)
            for i in range(5):
                driver.click(0.5,0.5)
                sleep(1)
            '''导航栏'''
            self.click_images(driver,"guide_014@auto.png")
            self.click_images(driver,"guide_015@auto.png")
            self.click_images(driver,"guide_016@auto.png")
            sleep(2)
            driver.click(0.5,0.5)
            self.click_images(driver,"guide_017@auto.png")
            '''第1-2关'''
            self.click_images(driver,"guide_018@auto.png")
            self.click_images(driver,"guide_010@auto.png")
            '''战斗'''
            sleep(5)
            for i in range(5):
                driver.click(0.5,0.5)
                sleep(1)
            sleep(3)
            driver.swipe(1079, 652, 1487, 848,50)
            sleep(11)
            driver.swipe(1079, 652, 1487, 848,50)
            sleep(11)
            driver.swipe(1079, 652, 1487, 848,50)
            sleep(5)
            for i in range(10):
                driver.click(500,500)
                sleep(2)
            '''导航栏'''
            self.click_images(driver,"guide_014@auto.png")
            self.click_images(driver,"guide_019@auto.png")
            self.click_images(driver,"guide_020@auto.png")
            self.click_images(driver,"guide_021@auto.png")
            self.click_images(driver,"guide_022@auto.png")
            self.click_images(driver,"guide_023@auto.png")
            self.click_images(driver,"guide_024@auto.png")
            self.click_images(driver,"guide_025@auto.png")
            '''任务'''
            self.click_images(driver,"guide_026@auto.png")
            self.click_images(driver,"guide_027@auto.png")
            sleep(2)
            driver.click(0.5,0.5)
            self.click_images(driver,"guide_028@auto.png")
            '''第1-3关'''
            self.click_images(driver,"guide_029@auto.png")
            self.click_images(driver,"guide_010@auto.png")
            '''战斗'''
            sleep(9)
            for i in range(5):
                sleep(1)
                driver.click(0.5,0.5)
            self.click_images(driver,"guide_003@auto.png")#点击屏幕继续
            sleep(2)
            driver.swipe(1181, 703, 1639, 817,50)
            self.click_images(driver,"guide_030@auto.png")#新技能一级核弹
            sleep(3)
            driver.swipe(1181, 703, 1639, 817,50)
            for i in range(8):
                sleep(2)
                driver.click(0.5,0.5)
            self.click_images(driver,"guide_031@auto.png")
            sleep(2)
            driver.click(500,500)
            '''导航栏'''
            self.click_images(driver,"guide_014@auto.png")
            sleep(2)
            self.click_images(driver,"guide_026@auto.png")
            self.click_images(driver,"guide_027@auto.png")
            sleep(2)
            driver.click(500,500)
            sleep(2)
            driver.click(500,500)
            '''角色'''
            self.click_images(driver,"guide_032@auto.png")
            self.click_images(driver,"guide_033@auto.png")
            self.click_images(driver,"guide_034@auto.png")
            self.click_images(driver,"guide_035@auto.png")
            '''任务'''
            self.click_images(driver,"guide_026@auto.png")
            self.click_images(driver,"guide_027@auto.png")
            sleep(2)
            driver.click(0.5,0.5)
            self.click_images(driver,"guide_028@auto.png")
            '''第1-4关'''
            self.click_images(driver,"guide_036@auto.png")
            self.click_images(driver,"guide_010@auto.png")
            '''战斗'''
            sleep(5)
            self.click_images(driver,"guide_037@auto.png")
            sleep(2)
            driver.swipe(1366, 624, 1600, 700,50)
            sleep(5)  
            sleep(9)
            driver.click(0.5,0.5)
            '''导航栏'''
            self.click_images(driver,"guide_014@auto.png")
            sleep(2)
            self.click_images(driver,"guide_026@auto.png")
            self.click_images(driver,"guide_027@auto.png")
            for i in range(6):
                sleep(1)
                driver.click(500,500)
            '''锻造'''
            self.click_images(driver,"guide_038@auto.png")
            self.click_images(driver,"guide_039@auto.png")
            self.click_images(driver,"guide_040@auto.png")
            self.click_images(driver,"guide_035@auto.png")
            '''任务'''
            self.click_images(driver,"guide_026@auto.png")
            self.click_images(driver,"guide_027@auto.png")
            sleep(2)
            driver.click(500,500)
            self.click_images(driver,"guide_028@auto.png")
            '''第1-5关'''
            self.click_images(driver,"guide_041@auto.png")
            self.click_images(driver,"guide_010@auto.png")
            sleep(5)
            for i in range(5):
                sleep(1)
                driver.click(0.5,0.5)
            '''战斗'''
            
            self.click_images(driver,"guide_012@auto.png")
            sleep(2)
            driver.swipe(549, 650, 60, 947,50)
            self.click_images(driver,"guide_013@auto.png")
            sleep(2)
            driver.swipe(549, 650, 60, 947,50)
            sleep(2)
            self.click_images(driver,"guide_021@auto.png")
            sleep(2)
            driver.swipe(560, 630, 360, 800,50)
            sleep(3)
            for i in range(15):
                sleep(1)
                driver.click(0.5,0.5)
            '''导航栏'''
            self.click_images(driver,"guide_014@auto.png")
            self.click_images(driver,"guide_026@auto.png")
            self.click_images(driver,"guide_027@auto.png")
            sleep(2)
            driver.click(500,500)
            sleep(2)
            driver.click(500,500)
            self.click_images(driver,"guide_042@auto.png")
            self.click_images(driver,"guide_028@auto.png")
            '''第2-1关'''
            self.click_images(driver,"guide_043@auto.png")
            self.click_images(driver,"guide_010@auto.png")
            '''战斗'''
            self.click_images(driver,"guide_012@auto.png")
            sleep(2)
            driver.swipe(563, 704, 99, 812,50)
            self.click_images(driver,"guide_013@auto.png")
            sleep(2)
            driver.swipe(563, 704, 99, 812,50)
            #self.click_images(driver,"guide_021@auto.png")
            #sleep(2)
            #driver.swipe(549, 647, 99, 812,50)
            sleep(5)
            for i in range(5):
                driver.click(0.5,0.5)
                sleep(1)
            '''导航栏'''
            self.click_images(driver,"guide_014@auto.png")
            sleep(2)
            self.click_images(driver,"guide_026@auto.png")
            self.click_images(driver,"guide_027@auto.png")
            sleep(2)
            driver.click(500,500)
            sleep(2)
            driver.click(500,500)
            '''返回大厅'''
            self.click_images(driver,"guide_044@auto.png")
            self.click_images(driver,"guide_045@auto.png")
            self.click_images(driver,"guide_045@auto.png")
            self.click_images(driver,"guide_046@auto.png")
            self.click_images(driver,"guide_046@auto.png")
        else:
            print "引导已结束"
        if self.wait_gone_images(driver,'guide_046@auto.png'):
            log.info('引导成功')
            return 'ok'
        else:
            log.info('引导失败')
            return None
        
        
        
        
        
        
        
        
        
                
        
        
        
        
        
        
        
        
        
        
            
        
        
        
        
        
        