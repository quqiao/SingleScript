# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
import configure
import os
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
        driver.prepare_ime()  # 准备输入法
        sleep(10)
        if self.images_or_none(driver, 'login_01@auto.png',way_name='channel'):
            driver.click(self.info1(driver) *1253, self.info2(driver) *903)#平台账号登录
            sleep(2)
            driver.click(self.info1(driver) * 859, self.info2(driver) * 458)  # 账号输入框
            driver.clear_text()
            print "请输入账号:"
            account = raw_input()
            driver.type(account,next=True)
            sleep(2)
            driver.click(self.info1(driver) * 835, self.info2(driver) *633)  # 密码输入框
            driver.clear_text()
            print "请输入密码:"
            password = raw_input()
            driver.type(password)
            sleep(2)
            driver.click(self.info1(driver) *958, self.info2(driver) *799)  # 登录
            sleep(2)
            if self.images_or_none(driver,'channel_binding@auto.png',way_name='channel'):#绑定手机
                driver.click(self.info1(driver) * 1289, self.info2(driver) * 183)  # 以后再说
            if self.wait_gone_images(driver,'login_01@auto.png',way_name='channel'):
                log.info('账号密码登录成功')
                return 'ok'
            else:
                log.info('账号密码登录失败')
                return None
        else:
            if self.images_or_none(driver,'channel_binding@auto.png',way_name='channel'):#绑定手机
                driver.click(self.info1(driver) * 1289, self.info2(driver) * 183)  # 以后再说
            if self.wait_gone_images(driver,'login_01@auto.png',way_name='channel'):
                log.info('自动登录成功')
                return 'ok'
            else:
                log.info('自动登录失败')
                return None

    def ali(self,driver):
        u"支付宝支付"
        
        self.click_images(driver,"guanfang_pay@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay_back@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    def wechat(self,driver):
        u"微信支付"
        
        self.click_images(driver,"wechat@auto.png",way_name='channel')
        self.click_images(driver,"guanfang_pay@auto.png",way_name='channel')
        self.click_images(driver,"wechat_back@auto.png",way_name='channel')
        self.click_images(driver,"wechat_back_cancel@auto.png",way_name='channel')
        sleep(2)
        driver.keyevent('BACK')
        driver.keyevent('BACK')
        if self.images_or_none(driver, 'exists_02@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    # def youyuwan(self,driver):
    #     u"游娱玩支付"
    #     if self.get_view_info(driver) == channel_pay_activity:
    #         self.click_images(driver,"youyuwan@auto.png",way_name='channel')
    #         self.click_images(driver,"guanfang_pay@auto.png",way_name='channel')
    #         self.click_images(driver,"youyuwan_pay_back@auto.png",way_name='channel')
    #         self.click_images(driver,"youyuwan_pay_back_yes@auto.png",way_name='channel')
            
            
    # def phonePay(self,driver):
    #     u"充值卡支付"
    #     if self.get_view_info(driver) == channel_pay_activity:
    #         self.click_images(driver,"phonePay@auto.png",way_name='channel')
    #         self.click_images(driver,"guanfang_pay@auto.png",way_name='channel')
    #         self.click_images(driver,"yingyongdou_pay_back_yes@auto.png",way_name='channel')
            

            
    def exitGame(self,driver):
        # self.click_images(driver,"setting@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_01@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_02@auto.png",way_name='channel')
        log.info('该渠道没有退出游戏')
        if self.wait_gone_images(driver, 'exitGame_02@auto.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None




            



