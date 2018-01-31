# coding=utf-8


from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'change_login.1920x1080.png',way_name='channel'):
            self.click_images(driver,"change_login.1920x1080.png",way_name='channel')
            self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("18482311990") 
            self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("123456")
            self.click_images(driver,"login.1920x1080.png",way_name='channel')
            self.click_images(driver,"login_shiming_close.1920x1080.png",way_name='channel')
        else:
            self.click_images(driver,"login_shiming_close.1920x1080.png",way_name='channel')
            log.info('自动登录成功')
        if self.wait_gone_images(driver,"login_shiming_close.1920x1080.png",way_name='channel'):
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
            
            
    
        
    def chongzhika(self,driver):
        u"充值卡支付"
        self.click_images(driver,"chongzhika.1920x1080.png",way_name='channel')
        self.click_images(driver,"sina_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"sina_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"sina_pay_back_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
            
    def unionPay(self,driver): 
        u"银联卡支付"
        self.click_images(driver,"unionPay.1920x1080.png",way_name='channel')
        self.click_images(driver,"unionPay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"unionPay_back_yes.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
    def exitGame(self,driver):
        # self.click_images(driver,"setting.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_01.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame_02.1920x1080.png",way_name='channel')
        # self.click_images(driver,"exitGame.1920x1080.png",way_name='channel')
        self.click_images(driver,"exitGame_03.1920x1080.png",way_name='channel')
        if self.wait_gone_images(driver, 'exitGame_03.1920x1080.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
        

