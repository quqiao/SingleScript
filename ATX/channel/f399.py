# coding=utf-8
#!/usr/bin/env python



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
        if self.images_or_none(driver, "login_01@auto.png", way_name='channel'):
            driver.click(300, 1020)  # 注册
            sleep(1)
            driver.click(810, 270)  # 用户名注册
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("20180110", next=True)
            sleep(1)
            driver.type("qatest2017")
            sleep(1)
            driver.click(540, 730)  # 注册
            sleep(2)
            driver.click(540, 1380)  # 注册
            log.info("快速注册")
        else:
            log.info("自动登录")
        sleep(2)
        driver.swipe(15, 580, 1000, 1000, 50)  # 拖动浮标隐藏
        if self.wait_gone_images(driver, 'login_01@auto.png', way_name='channel', timeout=40):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

        # while (0 < 1):
        #     if self.images_or_none(driver, u"channle_login_logo@auto.png",way_name="channel"):
        #         self.click_images(driver, u"channle_login_logo@auto.png",way_name="channel")
        #         break
        # if self.images_or_none(driver, u"channle_login_logo@auto.png", way_name='channel'):
        #     sleep(2)
        #     driver.click((self.info1(driver) * 760.0), (self.info2(driver) * 773.0))  # 快速注册
        #     driver.long_click((self.info1(driver) * 760.0), (self.info2(driver) * 773.0))  # 快速注册
        #     sleep(2)
        #     driver.click((self.info1(driver) * 1346.0), (self.info2(driver) * 212.0))  # 用户名注册
        #     driver.long_click((self.info1(driver) * 1346.0), (self.info2(driver) * 212.0))  # 用户名注册
        #     sleep(2)
        #     driver.click((self.info1(driver) * 541.0), (self.info2(driver) * 636.0))  # 输入密码
        #     driver.long_click((self.info1(driver) * 541.0), (self.info2(driver) * 636.0))  # 输入密码
        #     sleep(1)
        #     print "请输入账号密码:"
        #     password = raw_input()
        #     driver.type(password,next=True)
        #     sleep(2)
        #     if self.images_or_none(driver, u"login_verificationCode@auto.png", way_name="channel"):
        #         print "请输入验证码:"
        #         verificationCode = raw_input()
        #         driver.type(verificationCode)
        #         sleep(2)
        #     self.click_images(driver, u"channle_register@auto.png", way_name="channel")  # 注册
        #     image = self.wait_gone_images(driver, u'channle_login_logo@auto.png', way_name='channel', timeout=40)
        #     if image:
        #         log.info('登录成功')
        #         return 'ok'
        #     else:
        #         log.info('登录失败')
        #         return None
        # else:
        #     log.info("自动登录成功")
        #     return 'ok'


    def fubiao(self,driver):
        self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_02@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_04@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_05@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_06@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_05@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_07@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_05@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_08@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_09@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_10@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_05@auto.png",way_name='channel')
        self.click_images   (driver,"fubiao_11@auto.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_01@auto.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None  

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"ali@auto.png",way_name='channel')
        self.click_images(driver,"4399_pay_certain@auto.png",way_name='channel')
        self.click_images(driver,"aliBack@auto.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None

    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"wechat@auto.png",way_name='channel')
        self.click_images(driver,"4399_pay_certain@auto.png",way_name='channel')
        self.click_images(driver,"wechat_Back@auto.png",way_name='channel')
        self.click_images(driver,"4399_pay_close@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def QQ(self,driver): 
        u"QQ支付"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"exchange_pay@auto.png",way_name='channel')
            self.click_images(driver,"QQ@auto.png",way_name='channel')
            self.click_images(driver,"4399_pay_certain@auto.png",way_name='channel')
            driver.keyenvent("BACK")
            self.click_images(driver,"4399_pay_close@auto.png",way_name='channel')
            

    def caifutong(self,driver): 
        u"财付通支付"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"exchange_pay@auto.png",way_name='channel')
            self.click_images(driver,"caifutong@auto.png",way_name='channel')
            self.click_images(driver,"4399_pay_certain@auto.png",way_name='channel')
            driver.keyenvent("BACK")
            self.click_images(driver,"caifutong_exit_yes@auto.png",way_name='channel')
            self.click_images(driver,"4399_pay_close@auto.png",way_name='channel')
            
    def exitGame(self,driver):
        # self.click_images(driver,"setting@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_01@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_02@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_03@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_01@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_04@auto.png",way_name='channel')
        sleep(2)
        driver.click(665,810)  # 退出游戏
        if self.wait_gone_images(driver, 'exitGame_04@auto.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
        
            


