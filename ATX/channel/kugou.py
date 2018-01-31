# coding=utf-8


from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'idInput@auto.png',way_name='channel'):
            self.click_images(driver,"idInput@auto.png",way_name='channel')
            sleep(1)
            driver.type("17713623912") 
            self.click_images(driver,"pswInput@auto.png",way_name='channel')
            sleep(1)
            driver.type("test123")
            self.click_images(driver,"login@auto.png",way_name='channel')
        else:
            log.info('自动登录成功')
        if self.wait_gone_images(driver,"login@auto.png",way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
    
    def fubiao(self,driver):
        self.click_exists(driver,"fubiao_01@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_02@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_06@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_04@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_06@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_05@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_06@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_07@auto.png",way_name='channel')
        self.click_exists(driver,"fubiao_03@auto.png",way_name='channel')
        if self.wait_gone_images(driver, 'fubiao_10@auto.png',way_name='channel'):
            log.info('浮标已关闭')
            return 'ok'
        else:
            return None 
        
              

    def ali(self,driver):
        u"支付宝支付" 
        self.click_images(driver,"ali@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay@auto.png",way_name='channel')
        self.click_images(driver,"al_pay_close_known@auto.png",way_name='channel')
        self.click_images(driver,"pay_back@auto.png",way_name='channel')
        self.click_images(driver,"pay_back@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
        
        
    def exitGame(self,driver):
        # self.click_exists(driver,"setting@auto.png",way_name='channel')
        # self.click_exists(driver,"exitGame@auto.png",way_name='channel')
        # self.click_exists(driver,"exitGame_01@auto.png",way_name='channel')
        # self.click_exists(driver,"exitGame@auto.png",way_name='channel')
        # self.click_exists(driver,"exitGame_02@auto.png",way_name='channel')
        # self.click_exists(driver,"exitGame_03@auto.png",way_name='channel')
        # self.click_exists(driver,"exitGame@auto.png",way_name='channel')
        self.click_exists(driver,"exitGame_04@auto.png",way_name='channel')
        if self.wait_gone_images(driver, 'exitGame_04@auto.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None
