# coding=utf-8

from time import sleep, strftime
import public.methods as public
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
        u"渠道login"
        driver.prepare_ime() # 准备输入法
        while (0 < 1):
            if driver(resourceId='com.meizu.gamecenter.service:id/tv_add_account', className='android.widget.TextView',
           text='登录其他账号').exists:
                break
        if self.images_or_none(driver, 'login_logo@auto.png',way_name='channel'):
            if driver(resourceId='com.meizu.gamecenter.service:id/tv_add_account', className='android.widget.TextView',
           text='登录其他账号').exists:
                driver(resourceId='com.meizu.gamecenter.service:id/tv_add_account', className='android.widget.TextView',
                       text='登录其他账号').click()
                sleep(2)
            driver.click(self.info1(driver) * 831, self.info2(driver) * 367)  # 账号输入框
            print "请输入账号:"
            account = raw_input()
            driver.type(account,next=True)
            sleep(2)
            print "请输入密码:"
            password= raw_input()
            driver.type(password)
            sleep(2)
            driver.click(self.info1(driver) * 958, self.info2(driver) *802)  #登录
            sleep(2)
            if driver(resourceId='com.meizu.gamecenter.service:id/tv_add_account', className='android.widget.TextView',
                      text='登录其他账号').wait.gone(timeout=3000):
                log.info('账号密码登录成功')
                return 'OK'
            else:
                log.info('账号密码登录失败')
                None
        else:
            if driver(resourceId='com.meizu.gamecenter.service:id/tv_add_account', className='android.widget.TextView',
           text='登录其他账号').wait.gone(timeout=3000):
                log.info('自动登录成功')
                return 'OK'
            else:
                log.info('自动登录失败')
                None

    def ali(self,driver):
        u'''支付宝支付'''
        driver(className='android.widget.LinearLayout',index=3).child(className='android.widget.LinearLayout',index=0).click() #支付宝支付
        driver(className="android.widget.LinearLayout").child(text=u"支付宝").click()
        driver(className="android.widget.RelativeLayout").child(text=u"立即支付").click()
        sleep(5)
        driver.press.back()
        if self.images_or_none(driver, 'exists_02@auto.png',way_name='channel'):
            log.info('支付宝支付成功')
            return "OK"
        else:
            log.info('支付宝支付失败')
            return None
        
    def wechat(self,driver):
        u'''微信支付'''
        sleep(1)
        driver(className='android.widget.LinearLayout',index=3).child(className='android.widget.LinearLayout',index=0).click()  #微信支付
        driver(className="android.widget.LinearLayout").child(text=u"微信支付").click()
        driver(className="android.widget.RelativeLayout").child(text=u"立即支付").click()
        driver(className='android.widget.LinearLayout',index=0).child(className='android.widget.ImageView',index=0).click()
        driver(resourceId="com.meizu.gamecenter.service:id/iv_close",index=1).click()
        if self.wait_gone_images(driver, 'exists_02@auto.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
        
    def exitGame(self,driver):
        sleep(2)
        driver(className="android.widget.LinearLayout").child(text=u"离开游戏").click()
        if self.wait_gone_images(driver, 'exists_03@auto.png',way_name='channel'):
            log.info('退出游戏成功')
            return "OK"
        else:
            log.info('退出游戏失败')
            return None
    