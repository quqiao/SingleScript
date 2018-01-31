# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'login_01@auto.png',way_name='channel'):
            sleep(1)
            driver.click(665,643)  # QQ登录
            sleep(6)
            driver.click(580,1485)  # 登录
            sleep(2)
            log.info('QQ登录')
            # self.click_images(driver,"idInput@auto.png",way_name='channel')
            # sleep(1)
            # driver.type("yzrtest7")
            # self.click_images(driver,"pswInput@auto.png",way_name='channel')
            # sleep(1)
            # driver.type("123456")
            # self.click_images(driver,"login@auto.png",way_name='channel')
            # self.click_images(driver,"login_bangdingshouji@auto.png",way_name='channel')
        else:
            sleep(1)
            driver.click(960,690)  # 直接登录
            log.info('直接登录')
        if self.wait_gone_images(driver,"login_01@auto.png",way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
              

    def ali(self,driver):
        u"支付宝支付"
        
        self.click_images(driver,"guanfang_pay@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay_back@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    def wechat(self,driver):
        u"微信支付"
        
        self.click_images(driver,"wechat@auto.png",way_name='channel')
        self.click_images(driver,"guanfang_pay@auto.png",way_name='channel')
        self.click_images(driver,"wechat_back@auto.png",way_name='channel')
        self.click_images(driver,"wechat_back_cancel@auto.png",way_name='channel')
        sleep(2)
        driver.keyevent('BACK')
        driver.keyevent('BACK')
        if self.images_or_none(driver, 'exists_02@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None 
            
    # def youyuwan(self,driver):
    #     u"游娱玩支付"
    #     if self.get_view_info(driver) == channel_pay_activity:
    #         self.click_images(driver,"youyuwan@auto.png",way_name='channel')
    #         self.click_images(driver,"guanfang_pay@auto.png",way_name='channel')
    #         self.click_images(driver,"youyuwan_pay_back@auto.png",way_name='channel')
    #         self.click_images(driver,"youyuwan_pay_back_yes@auto.png",way_name='channel')
            
            
    # def phonePay(self,driver):
    #     u"充值卡支付"
    #     if self.get_view_info(driver) == channel_pay_activity:
    #         self.click_images(driver,"phonePay@auto.png",way_name='channel')
    #         self.click_images(driver,"guanfang_pay@auto.png",way_name='channel')
    #         self.click_images(driver,"yingyongdou_pay_back_yes@auto.png",way_name='channel')
            

            
    def exitGame(self,driver):
        # self.click_images(driver,"setting@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_01@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame@auto.png",way_name='channel')
        # self.click_images(driver,"exitGame_02@auto.png",way_name='channel')
        log.info('该渠道没有退出游戏')
        if self.wait_gone_images(driver, 'exitGame_02@auto.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None




            



