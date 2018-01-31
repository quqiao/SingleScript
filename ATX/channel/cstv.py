#!/usr/bin/env python
# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
import os
import configure
log = logutils.getLogger(__name__)

class Channel(public.Methods):
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

    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'login_01@auto.png', way_name='channel'):
            driver.click(self.info1(driver)*600, self.info2(driver)*850)  # 一键注册
            sleep(1)
            driver.click(self.info1(driver)*1330, self.info2(driver)*220)  # 返回游戏
            sleep(1)
            driver.click(self.info1(driver)*1370, self.info2(driver)*120)  # 实名认证返回游戏
            log.info('一键登录')
        else:
            driver.click(self.info1(driver)*650, self.info2(driver)*720)  # 立即登录
            sleep(1)
            driver.click(self.info1(driver)*1370, self.info2(driver)*120)  # 实名认证返回游戏
            log.info('自动登录')
        driver.swipe(30, 535, 30, 800, 50)  # 移动浮标
        if self.wait_gone_images(driver, 'login_01@auto.png', way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

        # if self.images_or_none(driver, 'fastRegister@auto.png', way_name='channel'):
        #     self.click_images(driver,'fastRegister@auto.png',way_name='channel')
        # if self.wait_gone_images(driver, 'login_logo@auto.png', way_name='channel'):
        #     log.info('一键注册成功')
        #     return 'ok'
        # else:
        #     log.info('一键注册失败')
        #     if self.images_or_none(driver, 'login_btn@auto.png', way_name='channel'):
        #         sleep(2)
        #         driver.click(self.info1(driver)*860, self.info2(driver)*469)  # 点击账号输入框
        #         sleep(1)
        #         driver.clear_text()
        #         sleep(2)
        #         driver.type("15198139230", next=True)
        #         sleep(1)
        #         driver.type("a123123")
        #         sleep(2)
        #         driver.click(self.info1(driver)*900, self.info2(driver)*850)  # 登录按钮
        #         sleep(3)
        #         driver.click(self.info1(driver)*1368, self.info2(driver)*119)  # 返回游戏
        #     if self.images_or_none(driver, 'login_rightNow@auto.png', way_name='channel'):
        #         self.click_images(driver, 'login_rightNow@auto.png', way_name='channel')
        #     if self.wait_gone_images(driver, 'login_shiming_returnGame.1920x1080.png', way_name='channel'):
        #         log.info('登录成功')
        #         return 'ok'
        #     else:
        #         log.info('登录失败')
        #         return None

            
    def fubiao(self,driver):
        self.click_exists(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_02.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_exists(driver,"fubiao_04.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        
        
        
        

    def ali(self,driver):
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')    
        self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
        sleep(1)
        driver.keyevent('BACK')
        if self.images_or_none(driver, 'exists_01.1920x1080.png'):
            return 'ok'
        else:
            return None 

    def phonePay(self,driver):
        self.click_images(driver,"phonePay.1920x1080.png",way_name='channel')
        sleep(2) 
        driver.keyevent('BACK')
        sleep(2)
        driver.keyevent('BACK')
        if self.images_or_none(driver, 'exists_01.1920x1080.png'):
            return 'ok'
        else:
            return None 

    def exitGame(self,driver):
        log.info('该游戏没有渠道退出')
        if self.wait_gone_images(driver, 'exitGame_02.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
    


