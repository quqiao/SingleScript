# coding=utf-8
#!/usr/bin/env python

from time import sleep, strftime
import public.methods as public
from public import logutils
import os
import configure
log = logutils.getLogger(__name__)

class Channel(public.Methods):

    def info1(self,driver):
        cmd = "adb -s %s shell wm size" % configure.device_name
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[1]
        g = float(f)
        x = g/1920.0
        return x

    def info2(self,driver):
        cmd = "adb -s %s shell wm size" % configure.device_name
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
        if self.images_or_none(driver, "login_01@auto.png", way_name='channel'):
            #######################################
            # sleep(1)
            # driver.click(self.info1(driver)*860, self.info2(driver)*350)  # 点击账号
            # sleep(1)
            # driver.clear_text()
            # sleep(1)
            # driver.type("17713623912", next=True)
            # sleep(1)
            # driver.type("test123")
            # sleep(1)
            # driver.click(self.info1(driver)*1342, self.info2(driver)*733)  # 点击账号
            # sleep(5)
            # driver.click(self.info1(driver)*1035, self.info2(driver)*128)  # 关闭真实信息登记
            # sleep(1)
            # log.info('输入账号登录')
            ########################################
            driver.click(self.info1(driver)*480, self.info2(driver)*750)  # 快速注册
            sleep(1)
            driver.click(self.info1(driver)*900, self.info2(driver)*800)  # 快速注册
            sleep(1)
            driver.click(self.info1(driver)*1035, self.info2(driver)*128)  # 关闭真实信息登记
            log.info('快速注册')
        else:
            driver.click(self.info1(driver)*960, self.info2(driver)*770)  # 立即注册
            sleep(1)
            driver.click(self.info1(driver)*1035, self.info2(driver)*128)  # 关闭真实信息登记
            sleep(1)
            log.info('自动登录')
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
        self.click_images(driver,"fubiao_04@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_06@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_04@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_07@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_04@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_08@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_04@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_09@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_04@auto.png",way_name='channel')
        self.click_images(driver,"fubiao_10@auto.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_10@auto.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None 
        
    def ali(self,driver):
        u"支付宝支付"
        #if self.get_view_info(driver) == channel_pay_activity:
        self.click_images(driver,"ali@auto.png",way_name='channel')
        self.click_images(driver,"anzhi_pay@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay_back@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes@auto.png",way_name='channel')
        self.click_images(driver,"anzhi_pay_back@auto.png",way_name='channel')
        self.click_images(driver,"anzhi_pay_back_yes@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    def wechat(self,driver):
        u"微信支付"
        #if self.get_view_info(driver) == channel_pay_activity:
        self.click_images(driver,"wechat@auto.png",way_name='channel')
        self.click_images(driver,"anzhi_pay@auto.png",way_name='channel')
        self.click_images(driver,"wechat_back@auto.png",way_name='channel')
        self.click_images(driver,"wechat_back_cancel@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_02@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None 
    '''        
    def UnionPay(self,driver):
        u"银联支付"
        #if self.get_view_info(driver) == channel_pay_activity:
        self.click_images(driver,"UnionPay@auto.png",way_name='channel')
        self.click_images(driver,"anzhi_pay@auto.png",way_name='channel')
        self.click_images(driver,"UnionPay_back@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_04@auto.png'):
            return 'ok'
        else:
            return None 
    '''
            
    """
    def VISAPay(self,driver):
        u"银联支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"muzhihui_changge_pay@auto.png",way_name='channel')
            self.click_images(driver,"VISA@auto.png",way_name='channel')
            self.click_images(driver,"muzhihui_pay@auto.png",way_name='channel')
            self.click_images(driver,"UnionPay_back@auto.png",way_name='channel')
    """
            
    def phonePay(self,driver):
        u"手机点卡支付"
        # if self.get_view_info(driver) == channel_pay_activity:
        self.click_images(driver,"anzhi_pay_changepay@auto.png",way_name='channel')
        self.click_images(driver,"phonePay@auto.png",way_name='channel')
        self.click_images(driver,"anzhi_pay@auto.png",way_name='channel')
        self.click_images(driver,"phonePay_back@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_04@auto.png'):
            return 'ok'
        else:
            return None
        
    def exitGame(self,driver):
        # self.click_images(driver,"setting@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_01@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_02@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_03@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_04@auto.png",way_name='channel')
        sleep(1)
        driver.click(655,569)  # 退出游戏
        sleep(2)
        if self.wait_gone_images(driver, 'exitGame_04@auto.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
        
        
        
        
            
    
