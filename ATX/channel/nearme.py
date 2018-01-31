# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
import os
import configure

log = logutils.getLogger(__name__)


# OPPO渠道

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
        u'''渠道login'''
        if self.images_or_none(driver, 'login_01@auto.png',way_name='channel'):
            driver.click(self.info1(driver) * 900, self.info2(driver) * 930)  # 使用其他帐号
            sleep(1)
            driver.click(self.info1(driver) * 520, self.info2(driver) * 680)  # 帐号输入框
            driver.clear_text()
            driver.type("17780664240", next=True)
            sleep(1)
            driver.type("qa123456")
            driver.click(self.info1(driver) * 540, self.info2(driver) * 1120)  # 登录
            sleep(2)
            driver.click(self.info1(driver) * 730, self.info2(driver) * 850)  # 跳过
            sleep(2)
            driver.click(self.info1(driver) * 900, self.info2(driver) * 920)  # 好
            log.info("输入帐号密码登录")
        else:
            driver.click(self.info1(driver) * 730, self.info2(driver) * 850)  # 跳过
            sleep(2)
            driver.click(self.info1(driver) * 900, self.info2(driver) * 920)  # 好
            log.info("自动登录")


        # while (0 < 1):
        #     if driver(resourceId='com.nearme.game.service:id/nmgc_choose_account', className='android.widget.TextView',
        #           text='选择OPPO帐号').exists or driver(resourceId='com.nearme.game.service:id/nmgc_choose_account', className='android.widget.TextView',
        #           text='选择OPPO帐号').wait.gone(timeout=5000):
        #         break
        # if driver(resourceId='com.nearme.game.service:id/nmgc_choose_account', className='android.widget.TextView',
        #           text='选择OPPO帐号').exists:
        #     driver.click(self.info1(driver) * 960, self.info2(driver) * 920)  # 使用其他账号登录
        #     sleep(2)
        #     driver(resourceId='com.oppo.usercenter:id/multi_autocomple_text',
        #            className='android.widget.EditText').click()
        #     driver.clear_text()
        #     print "请输入账号:"
        #     account = raw_input()
        #     driver.type(account, next=True)
        #     sleep(2)
        #     print "请输入密码:"
        #     password = raw_input()
        #     driver.type(password)
        #     sleep(2)
        #     driver(resourceId='com.oppo.usercenter:id/btn_login', className='android.widget.Button').click()  # 登录
        #     if driver(resourceId='com.nearme.game.service:id/btn_nav', className='android.widget.TextView',
        #               text='跳过').exists:
        #         driver.click(self.info1(driver) * 785, self.info2(driver) * 845)  # 跳过
        #     if driver(resourceId='com.nearme.game.service:id/get_it',
        #               className='android.widget.TextView').exists:  # 可币券福利
        #         driver(resourceId='com.nearme.game.service:id/get_it', className='android.widget.TextView').click()
        #     if driver(resourceId='com.nearme.game.service:id/nmgc_choose_account', className='android.widget.TextView',
        #           text='选择OPPO帐号').wait.gone(timeout=3000):
        #         log.info('账号密码登录成功')
        #         return 'OK'
        #     else:
        #         log.info('账号密码登录失败')
        #         return None
        # else:
        #     if driver(resourceId='com.nearme.game.service:id/btn_nav', className='android.widget.TextView',
        #               text='跳过').exists:
        #         driver.click(self.info1(driver) * 785, self.info2(driver) * 845)  # 跳过
        #     if driver(resourceId='com.nearme.game.service:id/get_it',
        #               className='android.widget.TextView').exists:  # 可币券福利
        #         driver(resourceId='com.nearme.game.service:id/get_it', className='android.widget.TextView').click()
        #     if driver(resourceId='com.nearme.game.service:id/nmgc_choose_account', className='android.widget.TextView',
        #           text='选择OPPO帐号').wait.gone(timeout=3000):
        #         log.info('自动登录成功')
        #         return 'OK'
        #     else:
        #         log.info('自动登录失败')
        #         return None

        # if self.images_or_none(driver, 'exists_01@auto.png',way_name='channel'):
        #     driver(index=0, resourceId="com.oppo.usercenter:id/multi_autocomple_text").click()
        #     driver.clear_text()
        #     driver.type("17713623912")
        #     driver(index=0, resourceId="com.oppo.usercenter:id/edit_input_content").click()
        #     driver.clear_text()
        #     driver.type("test123")
        #     driver(index=4, resourceId="com.oppo.usercenter:id/btn_login").click()
        #     driver(index=0, resourceId="com.nearme.game.service:id/btn_nav").click()
        #     image = self.wait_gone_images(driver, 'exists_01@auto.png',timeout=40,way_name='channel')
        #     if image:
        #         log.info('登录成功')
        #         return 'ok'
        #     else:
        #         log.info('登录失败')
        #         return None
        # else:
        #     driver(index=0, resourceId="com.nearme.game.service:id/btn_nav").click()
        #     image = self.wait_gone_images(driver, 'exists_01@auto.png',way_name='channel')
        #     if image:
        #         log.info('自动登录成功')
        #         return 'ok'

    def fanhui(self, driver):
        sleep(3)
        driver(resourceId='com.nearme.atlas:id/btn_back', index=0).click()
        self.click_images(driver, "exit_pay_yes@auto.png", way_name='channel')
        # driver(resourceId='com.nearme.atlas:id/dialog_standard_bt_yes',index=1).click()
        if self.wait_gone_images(driver, 'exists_02@auto.png', way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None

    def fubiao(self, driver):
        u"浮标检查"
        log.info('暂时不处理浮标')
        # sleep(2)
        # driver.click(18,174)
        # driver.click(18,174)
        # driver(className="android.widget.RelativeLayout").child(text=u"福利").click()
        # driver(index=0, resourceId="com.nearme.game.service:id/back").click()
        # driver(className="android.widget.RelativeLayout").child(text=u"积分商城").click()
        # driver(index=0, resourceId="com.nearme.gamecenter:id/color_home_view").click()
        # driver(className="android.widget.RelativeLayout").child(text=u"可币券").click()
        # driver(index=0, resourceId="com.nearme.game.service:id/back").click()
        # driver(className="android.widget.RelativeLayout").child(text=u"论坛").click()
        # sleep(3)
        # driver.press.back()
        # driver(className="android.widget.RelativeLayout").child(text=u"消息").click()
        # driver(index=0, resourceId="com.nearme.game.service:id/back").click()
        # driver(className="android.widget.RelativeLayout").child(text=u"客服").click()
        # driver(index=0, resourceId="com.nearme.game.service:id/back").click()
        # driver(index=2, resourceId="com.nearme.game.service:id/close").click()
        # sleep(2)
        # driver.swipe(18,174,961,872)
        if self.wait_gone_images(driver, 'fubiao_01@auto.png', way_name='channel'):
            log.info('浮标检查成功')
            return "OK"
        else:
            log.info('浮标检查失败')
            return None

    def ali(self, driver):
        u'''支付宝支付'''
        driver(className='android.widget.ListView', index=6).child(className='android.widget.LinearLayout',
                                                                   index=0).click()  # 支付宝支付
        driver(className='android.widget.LinearLayout', index=1).child(className='android.widget.Button',
                                                                       index=0).click()
        sleep(10)
        driver.press.back()
        if self.images_or_none(driver, 'exists_02@auto.png', way_name='channel'):
            log.info('支付宝支付成功')
            return "OK"
        else:
            log.info('支付宝支付失败')
            return None

    def wechat(self, driver):
        u'''微信支付'''
        sleep(1)
        driver(className="android.widget.LinearLayout").child(text=u"微信支付").click()  # 微信支付
        driver(className='android.widget.LinearLayout', index=1).child(className='android.widget.Button',
                                                                       index=0).click()
        sleep(5)
        driver(className='android.widget.LinearLayout', index=0).child(className="android.widget.ImageView",
                                                                       index=0).click()  # 退出微信
        driver(resourceId='com.nearme.atlas:id/btn_back', index=0).click()
        self.click_images(driver, "exit_pay_yes@auto.png", way_name='channel')
        # sleep(2)
        # driver(resourceId='com.nearme.atlas:id/dialog_standard_bt_yes',index=1).click()
        if self.wait_gone_images(driver, 'exists_02@auto.png', way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None

    def exitGame(self, driver):
        sleep(2)
        driver(resourceIdclassName='com.nearme.game.service:id/exit_btn', index=1).click()
        sleep(2)
        if self.wait_gone_images(driver, 'exists_02@auto.png', way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
