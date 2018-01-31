# coding=utf-8


from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        self.click_images(driver,u"yingyonghui_change_login@auto.png",way_name='channel')
        self.click_images(driver,u"idInput@auto.png",way_name='channel')
        sleep(1)
        driver.type("15198139230") 
        self.click_images(driver,u"pswInput@auto.png",way_name='channel')
        sleep(1)
        driver.type("a123123")
        self.click_images(driver,u"login@auto.png",way_name='channel')
              

    def ali(self,driver):
        u"支付宝支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"ali@auto.png",way_name='channel')
            self.click_images(driver,"ali_pay_back@auto.png",way_name='channel')
            self.click_images(driver,"ali_pay_back_yes@auto.png",way_name='channel')
            
    def wechat(self,driver):
        u"微信支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"wechat@auto.png",way_name='channel')
            self.click_images(driver,"wechat_back@auto.png",way_name='channel')
            
    def yingyongdou(self,driver):
        u"应用豆支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"yingyongdou@auto.png",way_name='channel')
            self.click_images(driver,"yingyongdou_pay_cancel@auto.png",way_name='channel')
            
    def caifutong(self,driver):
        u"财付通支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"caifutong@auto.png",way_name='channel')
            self.click_images(driver,"yingyongdou_pay_back@auto.png",way_name='channel')
            self.click_images(driver,"yingyongdou_pay_back_yes@auto.png",way_name='channel')
            
    def phonePay(self,driver):
        u"财付通支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"phonePay@auto.png",way_name='channel')
            self.click_images(driver,"phonePay_back@auto.png",way_name='channel')

            




            




