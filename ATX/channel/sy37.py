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
            driver.click(self.info1(driver)*900, self.info1(driver)*380)  # 帐号输入框
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("wan279378792", next=True) 
            # self.click_images(driver,"pswInput@auto.png",way_name='channel')
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("981298")
            self.click_images(driver,"login@auto.png",way_name='channel')
            log.info("输入账户密码登录")
        else:
            self.wait_gone_images(driver, 'login@auto.png',timeout=40,way_name='channel')
            log.info('自动登录')

        if self.wait_gone_images(driver, 'login_01@auto.png',timeout=40,way_name='channel'):
                log.info('登录成功')
                return 'ok'
        else:
            log.info('登录失败')
            return None
            
    def fubiao(self,driver):
        u'浮标操作'
        self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_02@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_04@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_05@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_06@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_05@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_07@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_08@auto.png",way_name='channel')
        for i in xrange(10):
                self.click_images(driver,"fubiao_09@auto.png",way_name='channel')
                sleep(1)
                if self.exist(driver,'exists_qmqz@auto.png',way_name='channel'):
                    print 'fail'
                    break
        if self.wait_gone_images(driver, 'fubiao_09@auto.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None          

    def exitGame(self,driver):
        log.info('没有内容')
        if self.wait_gone_images(driver, 'fubiao_09@auto.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"37_pay@auto.png",way_name='channel')
        self.click_images(driver,"ali@auto.png",way_name='channel')
        self.click_images(driver,"aliBack@auto.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes@auto.png",way_name='channel')
        self.click_images(driver,"37_return_game@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None

    def wangshangyinhang(self,driver):
        u"网上银行"
        self.click_images(driver,"37_pay@auto.png",way_name='channel')
        self.click_images(driver,"wangshangyinhang@auto.png",way_name='channel')
        self.click_images(driver,"aliBack@auto.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes@auto.png",way_name='channel')
        self.click_images(driver,"37_return_game@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def unionPay(self,driver): 
        u"银联卡"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay@auto.png",way_name='channel')
            self.click_images(driver,"unionPay@auto.png",way_name='channel')
            self.click_images(driver,"unionPay_cancel@auto.png",way_name='channel')

    def CreditPay(self,driver): 
        u"信用卡"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay@auto.png",way_name='channel')
            self.click_images(driver,"CreditPay@auto.png",way_name='channel')  
            self.click_images(driver,"unionPay_cancel@auto.png",way_name='channel')
            
    def caifutong(self,driver): 
        u"财付通"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay@auto.png",way_name='channel')
            self.click_images(driver,"caifutong@auto.png",way_name='channel')
            self.click_images(driver,"pay_return_game@auto.png",way_name='channel')
            
    def zhuanzhang(self,driver):
        u"转账汇款"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay@auto.png",way_name='channel')
            self.click_images(driver,"zhuanzhang@auto.png",way_name='channel')
            self.click_images(driver,"pay_return_game@auto.png",way_name='channel')
            
    def chinaMobile(self,driver):
        u"中国移动"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay@auto.png",way_name='channel')
            self.click_images(driver,"chinaMobile@auto.png",way_name='channel')
            self.click_images(driver,"pay_return_game@auto.png",way_name='channel')
        
    def chinaUnicom(self,driver):
        u"中国联通"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay@auto.png",way_name='channel')
            self.click_images(driver,"chinaUnicom@auto.png",way_name='channel')
            self.click_images(driver,"pay_return_game@auto.png",way_name='channel')
            
    def chinaTelecom(self,driver):
        u"中国电信"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay@auto.png",way_name='channel')
            self.click_images(driver,"chinaTelecom@auto.png",way_name='channel')
            self.click_images(driver,"pay_return_game@auto.png",way_name='channel')
            
    def junwang(self,driver):
        u"骏卡"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"37_pay@auto.png",way_name='channel')
            self.click_images(driver,"junwang@auto.png",way_name='channel')
            self.click_images(driver,"pay_return_game@auto.png",way_name='channel')

