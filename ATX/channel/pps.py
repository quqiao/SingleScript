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
            ##############输入账号密码登录############
            # sleep(1)
            # driver.click(1245,909)  # 已有账号登录
            # sleep(2)
            # driver.click(800,369)  # 点击输入框
            # sleep(2)
            # driver.type("18583238812",next=True)
            # sleep(1)
            # driver.type("qatest123")
            # sleep(1)
            # driver.click(950,710)  # 进入游戏
            # log.info('输入账号密码登录')
            ##########################################################
            sleep(1)
            driver.click(self.info1(driver)*700, self.info2(driver)*890)  # 快速游戏
            sleep(1)
            log.infp('快速游戏')
        else:
            log.info('自动登录成功')
        driver.swipe(20,430,960,975,100)  # 移动浮标隐藏
        if self.wait_gone_images(driver, 'login_01@auto.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
            
    def fubiao(self,driver):
        self.click_exists(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_02@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_04@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_05@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_06@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_07@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_03@auto.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None 
        

    def ali(self,driver):
        u"支付宝支付"
        
        self.click_images(driver,"ali@auto.png",way_name='channel')
        self.click_images(driver,"PPS_pay_certain@auto.png",way_name='channel')
        sleep(2)
        self.click_images(driver,"aliBack@auto.png",way_name='channel')
        self.click_images(driver,"ali_exit_yes@auto.png",way_name='channel')
        self.click_images(driver,"pps_pay_fail_yes@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None   
    
        
    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"PPS_pay_certain@auto.png",way_name='channel')
        self.click_images(driver,"wechat_Back@auto.png",way_name='channel')
        self.click_images(driver,"pps_pay_fail_yes@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
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
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
    
    def mo9(self,driver): 
        u"mo9支付"
        self.click_images(driver,"mo9@auto.png",way_name='channel')
        self.click_images(driver,"PPS_pay_certain@auto.png",way_name='channel')
        self.click_images(driver,"mo9_close@auto.png",way_name='channel')
        self.click_images(driver,"PPS_return_game@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None    

    def caifutong(self,driver): 
        u"财付通支付"
        self.click_images(driver,"caifutong@auto.png",way_name='channel')
        self.click_images(driver,"PPS_pay_certain@auto.png",way_name='channel')
        self.click_images(driver,"caifutong_close@auto.png",way_name='channel')
        self.click_images(driver,"PPS_return_game@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def unionPay(self,driver): 
        u"财付通支付"
        self.click_images(driver,"unionPay    @auto.png",way_name='channel')
        self.click_images(driver,"PPS_pay_certain@auto.png",way_name='channel')
        self.click_images(driver,"caifutong_close@auto.png",way_name='channel')
        self.click_images(driver,"PPS_return_game@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
    def exitGame(self,driver):
        self.click_exists(driver,"exitGame_02@auto.png",way_name='channel')
        if self.wait_gone_images(driver, 'exitGame_02@auto.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
            

