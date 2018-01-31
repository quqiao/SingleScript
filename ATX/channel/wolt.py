# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        '''渠道login'''
        if self.images_or_none(driver, 'idInput.1920x1080.png',way_name='channel'):
            self.click_images(driver,"change_login.1920x1080.png",way_name='channel')
            self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("15202828543") 
            self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            sleep(1)
            driver.type("123456")
            self.click_images(driver,"login.1920x1080.png",way_name='channel')
        else:
            log.info('自动登录成功')
            return 'ok'
        if self.wait_gone_images(driver,"login.1920x1080.png",way_name='channel'):
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
        
    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"wechat.1920x1080.png",way_name='channel')
        self.click_images(driver,"wechat_Back.1920x1080.png",way_name='channel')
        self.click_images(driver,"unicom_pay_close.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_02.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def telecomPay(self,driver): 
        u"沃币支付"
        self.click_images(driver,"change_wo_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wo_pay.1920x1080.png",way_name='channel')
        self.click_images(driver,"wo_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"wo_pay_back.1920x1080.png",way_name='channel')
        self.click_images(driver,"unicom_pay_close.1920x1080.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01.1920x1080.png',way_name='channel'):
            return 'ok'
        else:
            return None
    

            


