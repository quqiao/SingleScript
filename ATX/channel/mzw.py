# coding=utf-8

from time import sleep, strftime
import public.methods as public
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

    def inputLogin(self, driver):
        driver.click(self.info1(driver)*950, self.info2(driver)*425)  # 点击输入框
        sleep(1)
        driver.type_clear()
        sleep(1)
        driver.type("18482311990", next=True)
        sleep(2)
        driver.type("123456")
        sleep(2)

    def normalRegister(self, driver):
        driver.click(self.info1(driver)*628, self.info2(driver)*268)  # 快速注册
        sleep(2)
        driver.click(self.info1(driver)*522, self.info2(driver)*865)  #普通注册
        sleep(2)
        driver.click(self.info1(driver)*603, self.info2(driver)*320)  #用户名输入框
        print "请输入账号:"
        account = raw_input()
        driver.type(account,next=True)
        sleep(2)
        print "请输入密码:"
        password = raw_input()
        driver.type(password)
        sleep(2)
        driver.click(self.info1(driver)*890, self.info2(driver)*656)  #完成注册
        if self.images_or_none(driver, 'channel_advertising@auto.png', way_name='channel'):
            driver.click(self.info1(driver) * 1375, self.info2(driver) * 132)  # 关闭渠道弹窗
        return "调用账号密码注册方法"

    def login(self, driver):
        driver.prepare_ime()  # 准备输入法
        while (0 < 1):
            normalLogo=self.images_or_none(driver, "login_01@auto.png", way_name="channel")
            autoLogo=self.images_or_none(driver, 'channel_advertising@auto.png', way_name='channel')
            if normalLogo or autoLogo:
                break
        if self.images_or_none(driver, 'login_01@auto.png',way_name='channel'):
            self.normalRegister(driver)
            if self.wait_gone_images(driver, "channel_advertising@auto.png", way_name='channel'):
                log.info("账号密码注册登录成功")
                return "OK"
            else:
                log.info("账号密码注册登录失败")
                return None
        else:
            if self.images_or_none(driver, 'channel_advertising@auto.png', way_name='channel'):
                driver.click(self.info1(driver) * 1375, self.info2(driver) * 132)  # 关闭渠道弹窗
            if self.wait_gone_images(driver, "channel_advertising@auto.png", way_name='channel'):
                log.info('自动登录成功')
                return "OK"
            else:
                log.info('自动登录失败')
                return None

    def fubiao(self, driver):
        self.click_exists(driver, "fubiao_01@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_02@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_03@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_04@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_05@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_06@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_04@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_05@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_07@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_04@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_05@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_08@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_04@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_05@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_09@auto.png", way_name='channel')
        self.click_exists(driver, "fubiao_04@auto.png", way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_04@auto.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None 
              

    def ali(self,driver):
        u"支付宝支付" 
        self.click_images(driver,"muzhihui_pay@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay_back@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def wechat(self,driver):
        u"微信支付" 
        self.click_images(driver,"muzhihui_changge_pay@auto.png",way_name='channel')
        self.click_images(driver,"wechat@auto.png",way_name='channel')
        self.click_images(driver,"muzhihui_pay@auto.png",way_name='channel')
        self.click_images(driver,"wechat_back@auto.png",way_name='channel')
        self.click_images(driver,"pay_close@auto.png",way_name='channel')
        self.click_images(driver,"pay_close_yes@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_02@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def UnionPay(self,driver):
        u"银联支付"
        self.click_images(driver,"muzhihui_changge_pay@auto.png",way_name='channel')
        self.click_images(driver,"UnionPay@auto.png",way_name='channel')
        self.click_images(driver,"muzhihui_pay@auto.png",way_name='channel')
        self.click_images(driver,"UnionPay_back@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def VISAPay(self,driver):
        u"银联支付"
        self.click_images(driver,"muzhihui_changge_pay@auto.png",way_name='channel')
        self.click_images(driver,"VISA@auto.png",way_name='channel')
        self.click_images(driver,"muzhihui_pay@auto.png",way_name='channel')
        self.click_images(driver,"UnionPay_back@auto.png",way_name='channel')
            
    def gamePay(self,driver):
        u"游戏点卡支付"
        self.click_images(driver,"muzhihui_changge_pay@auto.png",way_name='channel')
        self.click_images(driver,"gamePay@auto.png",way_name='channel')
        self.click_images(driver,"muzhihui_pay@auto.png",way_name='channel')
        self.click_images(driver,"UnionPay_back@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def phonePay(self,driver):
        u"游戏点卡支付"
        self.click_images(driver,"muzhihui_changge_pay@auto.png",way_name='channel')
        self.click_images(driver,"phonePay@auto.png",way_name='channel')
        self.click_images(driver,"muzhihui_pay@auto.png",way_name='channel')
        self.click_images(driver,"UnionPay_back@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    

