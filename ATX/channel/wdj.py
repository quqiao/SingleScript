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
            driver.click(self.info1(driver)*800, self.info2(driver)*560)  # 输入框
            sleep(2)
            driver.type("13986959965")
            sleep(1)
            driver.click(self.info1(driver)*896, self.info2(driver)*720)  # 一键注册
            sleep(2)
            driver.click(self.info1(driver)*900, self.info2(driver)*720)  # 进入游戏
            sleep(2)
            driver.click(self.info1(driver)*1355, self.info2(driver)*120)  # 关闭实名认证
            log.info("一键登录")
            # self.click_images(driver,"exist_id@auto.png",way_name='channel')
            # sleep(1)
            # self.click_images(driver,"idInput@auto.png",way_name='channel')
            # sleep(1)
            # driver.type("15202828543")
            # self.click_images(driver,"pswInput@auto.png",way_name='channel')
            # sleep(1)
            # driver.type("menglong")
            # self.click_images(driver,"login@auto.png",way_name='channel')
            # self.click_images(driver,"login_shiming_close@auto.png",way_name='channel')
        else:
            sleep(2)
            driver.click(self.info1(driver)*1355, self.info2(driver)*120)  # 关闭实名认证
            log.info('自动登录成功')
        if self.wait_gone_images(driver,"login_shiming_close@auto.png",way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None


    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"ali@auto.png",way_name='channel')
        self.click_images(driver,"aliBack@auto.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
        
    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"change_pay@auto.png",way_name='channel')
        self.click_images(driver,"wechat@auto.png",way_name='channel')
        self.click_images(driver,"wechat_pay@auto.png",way_name='channel')
        self.click_images(driver,"wechat_back@auto.png",way_name='channel')
        self.click_images(driver,"wechat_pay_exit@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
    def unionPay(self,driver): 
        u"银联卡支付"
        self.click_images(driver,"change_pay@auto.png",way_name='channel')
        self.click_images(driver,"unionPay@auto.png",way_name='channel')
        self.click_images(driver,"unionPay_pay@auto.png",way_name='channel')
        self.click_images(driver,"unionPay_pay_back@auto.png",way_name='channel')
        self.click_images(driver,"unionPay_pay_back_yes@auto.png",way_name='channel')
            
    def phonePay(self,driver): 
        u"手机支付"
        self.click_images(driver,"change_pay@auto.png",way_name='channel')
        self.click_images(driver,"phonePay@auto.png",way_name='channel')
        self.click_images(driver,"phonePay_pay@auto.png",way_name='channel')
        self.click_images(driver,"wangdoujia_pay_back@auto.png",way_name='channel')
