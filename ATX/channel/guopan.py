#!/usr/bin/env python
# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
import os
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def info1(self,driver):
        cmd = "adb shell wm size"
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[1]
        g = float(f)
        x = g/1920.0
        return x

    def info2(self,driver):
        cmd = "adb shell wm size"
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
        if self.images_or_none(driver, 'login_01@auto.png',way_name='channel'):
            sleep(1)
            driver.click(self.info1(driver)*980, self.info2(driver)*900)  # 果盘帐号注册
            sleep(2)
            driver.click(self.info1(driver)*820, self.info2(driver)*620)  # 点击密码
            sleep(1)
            driver.type("123456")
            sleep(1)
            driver.click(self.info1(driver)*960, self.info2(driver)*800)  # 立即注册
            sleep(2)
            driver.click(self.info1(driver)*1164, self.info2(driver)*887) # 我知道了
            log.info("果盘帐号注册")

            ##############输入帐号密码登录#################
            # self.click_images(driver,u"idInput@auto.png",way_name='channel')
            # sleep(1)
            # driver.type("17713623912")
            # self.click_images(driver,u"pswInput@auto.png",way_name='channel')
            # sleep(1)
            # driver.type("test123")
            # self.click_images(driver,u"login@auto.png",way_name='channel')
            # sleep(1)
            # driver.click(1025,339)  # 点击输入框
            # sleep(1)
            # driver.clear_text()
            # sleep(1)
            # driver.type("17713623912",next = True)
            # sleep(1)
            # driver.type("test123")
            # sleep(1)
            # driver.click(960,720)  # 登录按钮
            # log.info('输入帐号密码登录')

        ###########有帐号密码直接按输入键#############
        # elif self.images_or_none(driver, 'loginid_exit@auto.png',way_name='channel'):
        #     self.click_images(driver,"login@auto.png",way_name='channel')
        #     log.info('有帐号密码直接按输入键')
        #     return 'ok'

        else:
            log.info('自动登录成功')

        if self.wait_gone_images(driver,u"login@auto.png",way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
            
    def fubiao(self,driver):
        self.click_exists(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_02@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_04@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_05@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_06@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_07@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_08@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_09@auto.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_09@auto.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None 

    def ali(self,driver):
        u'支付宝支付'
        self.click_images(driver,"ali@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay_back@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None

    def wechat(self,driver):
        u'微信支付'
        self.click_images(driver,"wechat@auto.png",way_name='channel')
        self.click_images(driver,"wechat_back@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None


    def guopan(self,driver):
        u'''果盘支付'''
        self.click_images(driver,"guopan@auto.png",way_name='channel')
        self.click_images(driver,"guopan_pay_back@auto.png",way_name='channel')
        self.click_images(driver,"guopan_pay_back_close@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_02@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
    def exitGame(self,driver):
        # self.click_exists(driver,"setting@auto.png",way_name='channel')
        # self.click_exists(driver,"exitGame@auto.png",way_name='channel')
        # self.click_exists(driver,"exitGame_01@auto.png",way_name='channel')
        # self.click_exists(driver,"exitGame@auto.png",way_name='channel')
        self.click_exists(driver,"exitGame_02@auto.png",way_name='channel')
        if self.wait_gone_images(driver, 'exitGame_02@auto.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None

