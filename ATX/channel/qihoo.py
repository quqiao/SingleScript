#!/usr/bin/env python
# coding=utf-8

import public.methods as public
from time import sleep
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
        driver.prepare_ime()  # 准备输入法
        while (0 < 1):
            if self.images_or_none(driver, u"login_01@auto.png", way_name="channel"):
                break
        if self.images_or_none(driver, 'login_01@auto.png', way_name='channel'):
            # driver(className="android.widget.EditText").sibling(className="android.widget.ImageView").click()
            driver.click(self.info1(driver)*690, self.info2(driver)*791)  # 账号密码注册
            sleep(2)
            driver.click(self.info1(driver) * 780, self.info2(driver) *373)  # 请输入账号
            print "请输入账号密码:"
            account = raw_input()
            driver.type(account,next=True)
            sleep(2)
            print "请输入账号密码:"
            password = raw_input()
            driver.type(password)
            sleep(2)
            self.click_images(driver,"register_rightNow@auto.png", way_name="channel")#注册
            if self.images_or_none(driver, "verificationCode@auto.png", way_name="channel"):
                driver.click(self.info1(driver) * 775, self.info2(driver) *680)  # 验证码
                print "请输入验证码:"
                verificationCode = raw_input()
                driver.type(verificationCode)
                sleep(2)
                self.click_images(driver, "register_rightNow@auto.png", way_name="channel")#注册
            if self.images_or_none(driver,"channel_advertising@auto.png",way_name="channel"):#等待渠道广告出现
                driver.click(self.info1(driver)*1691, self.info2(driver)*109)  #渠道广告
            if self.images_or_none(driver, "certification_close@auto.png", way_name="channel"):
                self.click_images(driver,"certification_close@auto.png",way_name="channel")
            if self.wait_gone_images(driver, 'certification_close@auto.png', way_name='channel'):
                log.info("注册账号成功")
                return "OK"
            else:
                log.info("注册账号失败")
                return None
        else:
            if self.images_or_none(driver, "channel_advertising@auto.png", way_name="channel"):  # 等待渠道广告出现
                driver.click(self.info1(driver) * 1691, self.info2(driver) * 109)  # 渠道广告
            if self.images_or_none(driver, "certification_close@auto.png", way_name="channel"):
                self.click_images(driver, "certification_close@auto.png", way_name="channel")
            if self.wait_gone_images(driver, 'certification_close@auto.png', way_name='channel'):
                log.info("自动登录成功")
                return "OK"
            else:
                log.info("自动登录失败")
                return None

    def fubiao(self, driver):
        u'浮标操作'
        log.info('不用浮标操作')
        # self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_02@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_03@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_04@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_05@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_06@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_07@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_08@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_09@auto.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_01@auto.png', way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None

    def ali(self, driver):
        u"支付宝支付"
        self.click_images(driver, "ali@auto.png", way_name='channel')
        if self.images_or_none(driver,"notPsw@auto.png",way_name='channel'):
            self.click_images(driver, "notPsw@auto.png", way_name='channel')
        if self.images_or_none(driver, "ali_sure_pay@auto.png", way_name='channel'):
            self.click_images(driver, "ali_sure_pay@auto.png", way_name='channel')
        if self.images_or_none(driver, 'ali_login_moreInfo@auto.png',way_name='channel') or self.images_or_none(driver, 'ali_pay_sureInfo@auto.png',way_name='channel'):
            os.popen("adb shell input keyevent 4")
        sleep(3)
        if self.images_or_none(driver, "ali_pay_fail@auto.png", way_name='channel'):
            log.info('支付失败')
            self.click_images(driver, "ali_pay_fail_sure@auto.png", way_name='channel')
            if self.wait_gone_images(driver, 'ali@auto.png', way_name='channel'):
                log.info('支付宝检查完成')
                return 'ok'
            else:
                return None

        '''if self.images_or_none(driver,'close_shiming@auto.png', way_name='channel'):
            self.click_images(driver, "close_shiming@auto.png", way_name='channel')
        self.click_images(driver, "ali@auto.png", way_name='channel')
        self.click_images(driver, "alipay@auto.png", way_name='channel')
        ##########不支付退出#######################
        self.click_images(driver, "aliBack@auto.png", way_name='channel')
        self.click_images(driver, "ali_exit_yes@auto.png", way_name='channel')
        self.click_images(driver, "pay_fail_yes@auto.png", way_name='channel')
        '''
        ###########登录支付宝账号################
        '''if self.images_or_none(driver, 'exists_alipay01@auto.png',way_name='channel'):
            for i in range(10):
                self.click_images(driver,"alipay_login01@auto.png",way_name='channel')
                if self.wait_gone_images(driver,"alipay_login01@auto.png",way_name='channel'):
                    break
            self.click_images(driver,"alipay_login02@auto.png",way_name='channel')
            sleep(1)
            driver.type("18583762260")
            self.click_images(driver,"alipay_login03@auto.png",way_name='channel')
            sleep(1)
            driver.type("687411")
            self.click_images(driver,"alipay_login04@auto.png",way_name='channel')
            self.click_images(driver,"alipay_login05@auto.png",way_name='channel')
            self.click_images(driver,"alipay_login06@auto.png",way_name='channel')
            self.click_images(driver,"alipay_login07@auto.png",way_name='channel')
        ###########已支付过再用支付宝支付################
        if self.images_or_none(driver, 'alipay_login05@auto.png',way_name='channel'):
            self.click_images(driver,"alipay_login05@auto.png",way_name='channel')
            self.click_images(driver,"alipay_login06@auto.png",way_name='channel')
            self.click_images(driver,"alipay_login07@auto.png",way_name='channel')
        '''

    def wechat(self, driver):
        u"微信支付"
        # self.click_images(driver, "close_shiming@auto.png", way_name='channel')
        # self.click_images(driver, "wechat@auto.png", way_name='channel')
        # self.click_images(driver, "wechat_pay@auto.png", way_name='channel')
        # ############微信不支付#################
        # self.click_images(driver, "wechat_back@auto.png", way_name='channel')
        # self.click_images(driver, "pay_fail_yes@auto.png", way_name='channel')
        ################登录微信#####################
        if self.images_or_none(driver,'wechat_pay_showInSDK@auto.png',way_name='channel'):
            self.click_images(driver,'wechat_pay_showInSDK@auto.png',way_name='channel')
        self.click_images(driver,'go_wechat_pay@auto.png',way_name='channel')
        sleep(2)
        self.click_images(driver,'wechat_pay_back@auto.png',way_name='channel')
        sleep(2)
        if self.images_or_none(driver, 'wechat_pay_fail@auto.png', way_name='channel'):
            log.info("微信支付失败")
            self.click_images(driver, 'wechat_pay_sure@auto.png', way_name='channel')
            if self.images_or_none(driver, 'exists_01@auto.png', way_name='channel'):
                log.info('微信检查完成')
                return 'ok'
            else:
                return None


        '''
        if self.images_or_none(driver, 'wechatpay_login03@auto.png',way_name='channel'):
            self.click_images(driver,"wechatpay_login01@auto.png",way_name='channel')
            sleep(1)
            driver.type("18583762260")
            self.click_images(driver,"wechatpay_login02@auto.png",way_name='channel')
            sleep(1)
            driver.type("qatest2017")
            self.click_images(driver,"wechatpay_login03@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login04@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login05@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login06@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login07@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login08@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login09@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login09@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login10@auto.png",way_name='channel')
            sleep(2)
            driver.keyevent('BACK')
            self.click_images(driver,"wechatpay_login12@auto.png",way_name='channel')
            self.click_images(driver,"wechat_back@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login11@auto.png",way_name='channel')
            for i in xrange(10):
                self.click_images(driver,"pay_01@auto.png")
                sleep(2)
                if self.exist(driver,'exists_01@auto.png'):
                    print 'fail'
                    break
            if self.images_or_none(driver, 'exists_01@auto.png'):
                return 'ok'
            else:
                return None 
        if self.images_or_none(driver, 'wechatpay_login04@auto.png',way_name='channel'):
            self.click_images(driver,"wechatpay_login04@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login05@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login06@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login07@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login08@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login09@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login09@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login10@auto.png",way_name='channel')
            sleep(2)
            driver.keyevent('BACK')
            self.click_images(driver,"wechatpay_login12@auto.png",way_name='channel')
            self.click_images(driver,"wechatpay_login11@auto.png",way_name='channel')
            for i in xrange(10):
                self.click_images(driver,"pay_01@auto.png")
                sleep(2)
                if self.exist(driver,'exists_01@auto.png'):
                    print 'fail'
                    break
            if self.images_or_none(driver, 'exists_01@auto.png'):
                return 'ok'
            else:
                return None 
        '''


    def exitSDK_activityInfo(self, driver):
        # self.click_images(driver,"exitGame_01@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_02_close@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_01@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_01_huodong@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_01_huodong_close@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_01@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_02@auto.png",way_name='channel')
        # driver.click(685, 720)  # 退出游戏
        if self.images_or_none(driver,'360_exitSDK_moreActivity@auto.png',way_name='channel'):
            self.click_images(driver,'360_exitSDK_moreActivity@auto.png',way_name='channel')
            if self.images_or_none(driver,'360_exitSDK_activityInfo@auto.png',way_name='channel'):
                self.click_images(driver, '360_exitSDK_activityClose@auto.png', way_name='channel')
                if self.wait_gone_images(driver, 'exitGame_02_close@auto.png', way_name='channel'):
                    log.info('退出框—活动详情显示成功')
                    return 'ok'
                else:
                    log.info('退出框—活动详情显示失败')
                    return None
        else:
            log.info("调起渠道退出SDK框失败")
            return None

    def exitSDK_exitGame(self,driver):
        if self.images_or_none(driver,'360_exitSDK_exitGame@auto.png',way_name='channel'):
            self.click_images(driver, '360_exitSDK_exitGame@auto.png', way_name='channel')
            if self.wait_gone_images(driver, 'exitGame_02_close@auto.png', way_name='channel'):
                log.info('退出框—退出游戏成功')
                return 'ok'
            else:
                log.info("退出游戏失败")
                return None
        else:
            log.info("调起渠道退出SDK框失败")
            return None