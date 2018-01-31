# coding=utf-8


from time import sleep, strftime
import public.methods as public
from public import logutils
import os
import configure
log = logutils.getLogger(__name__)


class Channel(public.Methods):
    def info1(self,driver):
        cmd = "adb -s %s shell wm size" %configure.device_name
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[1]
        g = float(f)
        x = g/1920.0
        return x

    def info2(self,driver):
        cmd = "adb -s %s shell wm size" %configure.device_name
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
        sleep(20)
        if self.images_or_none(driver, 'login_01@auto.png', way_name='channel'):
            ################################################################
            driver.click(self.info1(driver)*820, self.info2(driver)*1210)  # 切换账号登录
            sleep(2)
            driver.click(self.info1(driver)*500, self.info2(driver)*670)  # 用户名输入
            sleep(1)
            driver.type("15198139230",next=True)
            sleep(1)
            driver.type("a123123")
            sleep(1)
            driver.click(self.info1(driver)*540, self.info2(driver)*1010)  # 登录
            log.info('输入账号密码登录')
            # # self.click_images(driver,"idInput@auto.png",way_name='channel')
            # # sleep(1)
            # # driver.type("15198139230")
            # # self.click_images(driver,"pswInput@auto.png",way_name='channel')
            # # sleep(1)
            # # driver.type("a123123")
            # # self.click_images(driver,"login@auto.png",way_name='channel')
            #################################################################
            # driver.click(self.info1(driver)*240, self.info2(driver)*1520)  # 极速登录
            # log.info("急速登录")
        else:
            log.info('自动登录')
        if self.wait_gone_images(driver,"login_01@auto.png",way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
              

    def ali(self,driver):
        u"支付宝支付"
        self.click_images(driver,"pay_shiming_close@auto.png",way_name='channel')
        self.click_images(driver,"ali@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay_back@auto.png",way_name='channel')
        self.click_images(driver,"ali_pay_back_yes@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
    def wechat(self,driver):
        u"微信支付"
        self.click_images(driver,"wechat@auto.png",way_name='channel')
        self.click_images(driver,"wechat_back@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
            return 'ok'
        else:
            return None
            
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
        u"手机支付"
        if self.get_view_info(driver) == channel_pay_activity:
            self.click_images(driver,"phonePay@auto.png",way_name='channel')
            self.click_images(driver,"phonePay_back@auto.png",way_name='channel')

    def exitGame(self,driver):
        log.info('应用汇没有渠道退出')
        if self.wait_gone_images(driver,"login_01@auto.png",way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            log.info('退出游戏失败')
            return None

    def fubiao(self,driver):
        log.info('暂时不用浮标')
        # driver.click(10,869)  # 隐藏浮标
        # sleep(1)
        # driver.click(60,900)  # 浮标
        # sleep(2)
        # driver.click(535,450)  # 礼包
        # sleep(2)
        # driver.click(868,450)  # 消息
        # sleep(2)
        # driver.click(950,130)  # 关闭
        # sleep(2)
        if self.wait_gone_images(driver,"fubiao_01@auto.png",way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            log.info('退出游戏失败')
            return None





            



