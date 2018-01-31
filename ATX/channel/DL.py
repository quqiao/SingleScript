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
            ##########################################
            # driver.click(1220, 930)  # 快速注册
            # sleep(2)
            # driver.click(900, 450)  # 输入帐号
            # sleep(1)
            # driver.clear_text()
            # sleep(1)
            # driver.type("ddd@qq.com", next = True)
            # sleep(1)
            # driver.type("123456")
            # sleep(1)
            # driver.click(900, 780)  # 下一步
            # log.inof("快速注册")
            ##########################################

            ###################################################
            driver.click(self.info1(driver)*520, self.info2(driver)*935)  # 点击帐号登录
            sleep(1)
            driver.click(self.info1(driver)*800, self.info2(driver)*450)  # 点击输入框
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("17713623912", next = True)
            # self.click_images(driver,u"pswInput.@auto.png",way_name='channel')
            sleep(1)
            driver.type("test123")
            sleep(1)
            driver.click(self.info1(driver)*900, self.info2(driver)*780)  # 点击登录
            log.info("帐号登录")
            ######################################################

        else:
            log.info("自动登录")
            # self.click_images(driver, "login_shiming_returnGame.@auto.png",way_name='channel')
        sleep(2)
        driver.swipe(20,70,20,800,50)  # 移动浮标
        if self.wait_gone_images(driver, 'login_01@auto.png', way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def fubiao(self,driver):
        self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_02@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_04@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_05@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_06@auto.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_05@auto.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None 

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"dangle_pay.@auto.png",way_name='channel')
        sleep(2)
        self.click_images(driver,"ali_pay_back.@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes.@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_02.@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"change_pay.@auto.png",way_name='channel')
        self.click_images(driver,"wechat.@auto.png",way_name='channel')
        self.click_images(driver,"dangle_pay.@auto.png",way_name='channel')
        self.click_images(driver,"wechat_back.@auto.png",way_name='channel')
        self.click_images(driver,"dangle_pay_close.@auto.png",way_name='channel')
        self.click_images(driver,"dangle_pay_close_yes.@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    def unionPay(self,driver):
        u"银联支付"
        self.click_images(driver,"change_pay.@auto.png",way_name='channel')
        self.click_images(driver,"unionPay.@auto.png",way_name='channel')
        self.click_images(driver,"dangle_pay.@auto.png",way_name='channel')
        self.click_images(driver,"unionPay_back.@auto.png",way_name='channel')
        self.click_images(driver,"unionPay_back_yes.@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.@auto.png'):
            return 'ok'
        else:
            return None 
        
    def exitGame(self,driver):
        # self.click_images(driver,"setting.@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame.@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_01.@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame.@auto.png",way_name='channel')
        self.click_images(driver,"exitGame_02.@auto.png",way_name='channel')
        if self.wait_gone_images(driver, 'exitGame_02.@auto.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
