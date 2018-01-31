# coding=utf-8


import os
#import unittest
#import atx
from time import sleep, strftime
import public.methods as public
#import configure
from public import logutils
import os
import configure
log = logutils.getLogger(__name__) 

class Channel(public.Methods):
    def info1(self, driver):
        cmd = "adb -s %s shell wm size" % configure.device_name
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[1]
        g = float(f)
        x = g / 1920.0
        return x

    def info2(self, driver):
        cmd = "adb -s %s shell wm size" % configure.device_name
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[0]
        g = float(f)
        y = g / 1080.0
        return y

    def login(self, driver):
        if self.images_or_none(driver, 'login_01@auto.png',way_name='channel'):
            ##############################################
            # driver.click(960, 770)  # 用户名注册
            # sleep(2)
            # driver.click(900, 250)  # 用户名
            # sleep(1)
            # driver.clear_text()
            # sleep(1)
            # driver.type("test2018", next=True)
            # sleep(1)
            # driver.type("123456")
            # sleep(1)
            # driver.click(960, 520)  # 注册
            # log.info("用户名注册")
            ###############################################
            driver.click(900, 250)  # 用户输入框
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("lytest112", next=True)
            sleep(1)
            driver.type("test1234")
            sleep(1)
            driver.click(970, 530)  # 登录
            log.info("帐号登录")
        else:
            log.info("自动登录")
        if self.wait_gone_images(driver, 'login_01@auto.png', way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

        # driver.prepare_ime()#准备输入法
        # while (0 < 1):
        #     if self.images_or_none(driver, u"login_01@auto.png", way_name="channel"):
        #         break
        # if self.images_or_none(driver,'login_01@auto.png',way_name='channel'):
        #     driver.click(self.info1(driver)*895, self.info2(driver)*720)  # 用户名注册
        #     sleep(2)
        #     driver.click(self.info1(driver)*620, self.info2(driver)*290)  # 请输入用户名
        #     print "请输入账号密码:"
        #     account = raw_input()
        #     driver.type(account, next=True)
        #     sleep(2)
        #     print "请输入账号密码:"
        #     password = raw_input()
        #     driver.type(password, next=True)
        #     sleep(2)
        #     self.click_images(driver, "channel_register@auto.png", way_name='channel')  # 注册
        #     if self.images_or_none(driver,'verificationCode_refresh@auto.png',way_name='channel'):
        #         driver.click(self.info1(driver) * 643, self.info2(driver) * 532)  # 验证码
        #         print "请输入验证码:"
        #         verificationCode = raw_input()
        #         driver.type(verificationCode)
        #         sleep(2)
        #         self.click_images(driver, "channel_register@auto.png", way_name='channel')#注册
        #     if self.wait_gone_images(driver,'channel_register@auto.png',way_name='channel'):
        #         log.info("账号注册成功")
        #         return "OK"
        #     else:
        #         log.info("账号注册失败")
        #         return None
        # else:
        #     log.info('自动登录')
        #     if self.wait_gone_images(driver,'login_01@auto.png',way_name='channel'):
        #         log.info('登录成功')
        #         return 'ok'
        #     else:
        #         log.info('登录失败')
        #         return None

    def fubiao (self, driver):
        log.info('暂时没有浮标')
        if self.wait_gone_images(driver, 'login@auto.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"ali@auto.png",way_name='channel')
        # self.click_images(driver,"aliBack@auto.png",way_name='channel')
        # self.click_images(driver,"ali_exit_yes@auto.png",way_name='channel')
        if self.images_or_none(driver,"aliPay_login@auto.png",way_name='channel') or self.images_or_none(driver,"aliPay_sureInfo@auto.png",way_name='channel'):
            os.popen("adb shell input keyevent 4")
        sleep(3)
        self.click_images(driver,"baidu_pay_return_game@auto.png",way_name='channel')
        return 'OK'
        
    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"wechat_pay@auto.png",way_name='channel')
        self.click_images(driver,"wechat_Back@auto.png",way_name='channel')
        self.click_images(driver,"baidu_pay_return_game@auto.png",way_name='channel')
        return 'OK'

    def QQ(self,driver): 
        u"银行卡支付"
        self.click_images(driver,"QQ@auto.png",way_name='channel')
        sleep(3)
        driver.keyevent('BACK')
        self.click_images(driver,"baidu_pay_return_game@auto.png",way_name='channel')
    

    def exit_HotGame(self,driver):
        if self.images_or_none(driver,'channel_exit_hotGame@auto.png',way_name='channel'):
            self.click_images(driver,'channel_exit_hotGame@auto.png',way_name='channel')#热门游戏
            if self.images_or_none(driver,'baidu_hotGame_showInfo@auto.png',way_name='channel'):
                os.popen("adb shell input keyevent 4")
        if self.wait_gone_images(driver, 'baidu_hotGame_showInfo@auto.png',way_name='channel'):
            log.info('百度渠道退出框_热门游戏显示完成')
            return 'ok'
        else:
            return None

    def exitGame(self, driver):
        if self.images_or_none(driver,'channel_sure_exit@auto.png', way_name='channel'):
            self.click_images(driver, 'channel_sure_exit@auto.png', way_name='channel')  # 确认退出
        if self.wait_gone_images(driver,'channel_sure_exit@auto.png', way_name='channel'):
            log.info('百度渠道退出框_退出游戏成功')
            return 'ok'
        else:
            return None