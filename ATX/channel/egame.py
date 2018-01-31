# coding=utf-8
# 渠道电信爱游戏

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
        if self.images_or_none(driver, 'login_01.1920x1080.png', way_name='channel'):
            #############################
            # driver.click(self.info1(driver)*855, self.info2(driver)*320)  # 点击输入框
            # sleep(1)
            # driver.type("17713623912",next=True)
            # sleep(1)
            # driver.type("test123")
            # sleep(1)
            # driver.click(self.info1(driver)*900, self.info2(driver)*630)  # 点击登录
            # # self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            # # sleep(1)
            # # driver.type("17713623912")
            # # self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            # # sleep(1)
            # # driver.type("test123")
            # # self.click_images(driver,"login.1920x1080.png",way_name='channel')
            # log.info('输入账号和密码登录')
            ############################
            driver.click(self.info1(driver)*1120, self.info2(driver)*830)  # 快速注册
            sleep(1)
            driver.click(self.info1(driver)*1120, self.info2(driver)*250)  # 用户名
            sleep(1)
            driver.click(self.info1(driver)*800, self.info2(driver)*630)  # 登录密码
            sleep(1)
            driver.type("test123")
            sleep(1)
            driver.click(self.info1(driver)*860, self.info2(driver)*860)  # 注册并进入游戏
            log.info('快速注册')
        # elif self.images_or_none(driver, 'login_exit_id.1920x1080.png',way_name='channel'):
        #     self.click_images(driver,"login_exit_id.1920x1080.png",way_name='channel')
        #     log.info('已有账号和密码登录')
        else:
            log.info('自动登录成功')
        if self.wait_gone_images(driver, 'login_01.1920x1080.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
              

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"ali.1920x1080.png",way_name='channel')
        self.click_images(driver,"aliBack.1920x1080.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_Back.1920x1080.png",way_name='channel')
        sleep(2)
        self.click_images(driver,"telecom_pay_close.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def telecomPay(self,driver): 
        u"翼支付"
        self.click_images(driver,"telecomPay.1920x1080.png",way_name='channel')
        self.click_images(driver,"telecomPay_cancel.1920x1080.png",way_name='channel')
        self.click_images(driver,"telecom_close.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None

    def fubiao(self,driver):
        log.info('电信爱游戏没有浮标')
        if self.wait_gone_images(driver, 'login_01.1920x1080.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
        
    def exitGame(self,driver):
        sleep(2)
        driver.click(1120,920)  # 退出游戏
        # self.click_images(driver,"setting.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_02.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_03.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_04.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'exitGame_04.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
    

            

