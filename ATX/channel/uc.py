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

    # def inputUser(self,driver):
    #     self.click_images(driver,'ucSDK_inputUN@auto.png',way_name='channel')
    #     driver.type("18980158564", next=True)
    #     sleep(2)
    #     driver.type("123456")
    #     sleep(2)
    #     self.click_images(driver, 'ucSDK_enterGame@auto.png', way_name='channel')
    #     if self.wait_gone_images(driver, 'ucSDK_enterGame@auto.png', way_name='channel'):
    #         log.info("输入帐号密码成功")
    #         return 'ok'
    #     else:
    #         log.info("输入帐号密码失败")
    #         return None

    # def QuickLogin(self,driver):
    #     sleep(2)
    #     driver.click(890,930)  # 快速注册
    #     sleep(1)
    #     driver.click(800,450)  # 输入框
    #     sleep(1)
    #     driver.type("123456")
    #     sleep(1)
    #     driver.click(900,650)  # 进入游戏
    #     if self.wait_gone_images(driver, 'ucSDK_enterGame@auto.png', way_name='channel'):
    #         log.info("快速注册成功")
    #         return 'ok'
    #     else:
    #         log.info("快速注册失败")
    #         return None

    def login(self, driver):
        if self.images_or_none(driver, 'login_01@auto.png', way_name='channel'):
            driver.click(880, 920)  # 快速注册可能性1
            sleep(1)
            driver.click(1200, 860)  # 快速注册可能性2
            sleep(2)
            driver.click(900, 450)  # 密码输入框
            sleep(1)
            driver.type("123456")
            sleep(2)
            driver.click(900, 650)  # 进入游戏
            sleep(2)
            driver.click(1354,127)  # 关闭实名认证
            log.info("快速注册")
        else:
            sleep(2)
            driver.click(1354,127)  # 关闭实名认证
            log.info("自动登录")

        if self.wait_gone_images(driver, 'login_01@auto.png', way_name='channel'):
            log.info('自动登录成功')
            return 'ok'
        else:
            log.info('自动登录失败')
            return None

        # driver.prepare_ime()  # 准备输入法
        # while (0 < 1):
        #     if self.images_or_none(driver, "login_01@auto.png", way_name="channel"):
        #         break
        # if self.images_or_none(driver, 'login_01@auto.png',way_name='channel'):
        #     # driver.click(self.info1(driver)*1198, self.info2(driver)*877)  # 快速注册
        #     driver(resourceId='cn.uc.gamesdk.account:id/btn_login_register',text="快速注册",className="android.widget.Button").click()
        #     sleep(2)
        #     driver.click(self.info1(driver)*786, self.info2(driver)*467)  # 密码
        #     print "请输入账号密码:"
        #     password = raw_input()
        #     driver.type(password)
        #     sleep(2)
        #     driver.click(self.info1(driver)*895, self.info2(driver)*654)  # 进入游戏
        #     if self.images_or_none(driver, 'push_close@auto.png',way_name='channel'):
        #         driver.click(self.info1(driver) * 1683, self.info2(driver) * 90) # 关闭顶部渠道推送
        #     if self.images_or_none(driver, 'verification@auto.png', way_name='channel'):#等待实名认证
        #         self.click_images(driver,"verification@auto.png",way_name='channel')
        #     if self.wait_gone_images(driver,'verification@auto.png', way_name='channel'):
        #         log.info("一键注册成功")
        #         return "Ok"
        #     else:
        #         log.info("一键注册失败")
        #         return None
        # else:
        #     if self.images_or_none(driver, 'verification@auto.png', way_name='channel'):#等待实名认证
        #         self.click_images(driver,"verification@auto.png",way_name='channel')
        #     if self.wait_gone_images(driver, 'verification@auto.png', way_name='channel'):
        #         log.info('自动登录成功')
        #         return 'ok'
        #     else:
        #         log.info('自动登录失败')
        #         return None

    def fubiao(self,driver):
        self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_02@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_04@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_05@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_06@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_07@auto.png",way_name='channel')
        sleep(2)
        driver.swipe(20,355,960,909)
        self.click_images(driver,"fubiao_08@auto.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_01@auto.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None            
    
    def QQ_Pay(self,driver):
        u"QQ支付"
        if self.images_or_none(driver,'ucSDK_pay_show@auto.png',way_name='channel'):
            if self.images_or_none(driver,'ucSDK_QQpay@auto.png',way_name='channel'):
                self.click_images(driver, "ucSDK_pay_sure@auto.png", way_name='channel')
        if self.images_or_none(driver,'ucSDK_pay_QQ_sureInfo@auto.png', way_name='channel') or self.images_or_none(driver,'ucSDK_pay_QQ_login@auto.png', way_name='channel'):
            os.popen("adb shell input keyevent 4")
        sleep(2)
        self.click_images(driver, "ucSDK_pay_backGame@auto.png", way_name='channel')
        if self.wait_gone_images(driver, 'ucSDK_pay_backGame@auto.png', way_name='channel'):
            log.info("QQ支付跳转成功")
            return 'ok'
        else:
            return None

    def wechat(self,driver):
        u"微信支付"
        sleep(2)
        if self.images_or_none(driver,'ucSDK_pay_show@auto.png',way_name='channel'):
            self.click_images(driver, "ucSDK_other_pay@auto.png", way_name='channel')
        sleep(2)
        if self.images_or_none(driver,'ucSDK_pay_choice@auto.png',way_name='channel'):
            self.click_images(driver, "ucSDK_pay_wechat@auto.png", way_name='channel')
        sleep(2)
        if self.images_or_none(driver, 'ucSDK_pay_sure@auto.png', way_name='channel'):
            self.click_images(driver, "ucSDK_pay_sure@auto.png", way_name='channel')
        sleep(2)
        if self.images_or_none(driver, 'ucSDK_wechat_back@auto.png', way_name='channel'):
            self.click_images(driver, "ucSDK_wechat_back@auto.png", way_name='channel')
        sleep(2)
        self.click_images(driver, "ucSDK_pay_backGame@auto.png", way_name='channel')
        if self.images_or_none(driver, 'ucSDK_pay_backGame@auto.png',way_name='channel'):
            log.info("微信支付跳转成功")
            return 'ok'
        else:
            return None
            
    def yinhangka(self,driver): 
        u"银行卡支付"
        self.click_images(driver,"yinhangka@auto.png",way_name='channel')
        self.click_images(driver,"PPS_pay_certain@auto.png",way_name='channel')
        self.click_images(driver,"yinhangka_close@auto.png",way_name='channel')
        self.click_images(driver,"yinhangka_close_yes@auto.png",way_name='channel')
        self.click_images(driver,"pps_pay_fail_yes@auto.png",way_name='channel')
    
    def mo9(self,driver): 
        u"mo9支付"
        self.click_images(driver,"mo9@auto.png",way_name='channel')
        self.click_images(driver,"PPS_pay_certain@auto.png",way_name='channel')
        self.click_images(driver,"mo9_close@auto.png",way_name='channel')
        self.click_images(driver,"PPS_return_game@auto.png",way_name='channel')      

    def caifutong(self,driver): 
        u"财付通支付"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"caifutong@auto.png",way_name='channel')
            self.click_images(driver,"PPS_pay_certain@auto.png",way_name='channel')
            self.click_images(driver,"caifutong_close@auto.png",way_name='channel')
            self.click_images(driver,"PPS_return_game@auto.png",way_name='channel')
            
    def unionPay(self,driver): 
        u"财付通支付"
        if self.get_view_info(driver) == channel_login_activity:
            self.click_images(driver,"unionPay    @auto.png",way_name='channel')
            self.click_images(driver,"PPS_pay_certain@auto.png",way_name='channel')
            self.click_images(driver,"caifutong_close@auto.png",way_name='channel')
            self.click_images(driver,"PPS_return_game@auto.png",way_name='channel')
            
    def exitGame(self,driver):
        # self.click_images(driver,"setting@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_01@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_02@auto.png",way_name='channel')
        if self.images_or_none(driver, 'ucSDK_exitGame@auto.png', way_name='channel'):
            self.click_images(driver, "ucSDK_exitGame@auto.png", way_name='channel')
        if self.wait_gone_images(driver, 'ucSDK_exitGame@auto.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
