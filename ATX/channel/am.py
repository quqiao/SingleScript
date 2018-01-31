# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)
import os


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
        f= e[0]
        g = float(f)
        y = g/1080.0
        return y

    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver, 'login_01@auto.png',way_name='channel'):
            sleep(1)
            driver.click(self.info1(driver)*818, self.info2(driver)*1848)  # 登录账号
            sleep(2)
            driver.click(self.info1(driver)*500, self.info2(driver)*300)  # 账号输入框
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("15202828543", next=True)
            sleep(1)
            driver.type("123456")
            sleep(2)
            driver.click(self.info1(driver)*540, self.info2(driver)*790)  # 登录
            sleep(3)
            driver.click(self.info1(driver)*724, self.info2(driver)*698)  # 稍后认证
            sleep(2)
            driver.click(self.info1(driver)*1357, self.info2(driver)*157)  # 关闭福利
            log.info('输入账号密码登录')
        else:
            sleep(3)
            driver.click(self.info1(driver)*724, self.info2(driver)*698)  # 稍后认证
            sleep(2)
            driver.click(self.info1(driver)*1357, self.info2    (driver)*157)  # 关闭福利
            log.info('自动登录')
        driver.swipe(10, 69, 10, 800, 50)  # 移动浮标
        if self.wait_gone_images(driver, 'login_01@auto.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
    
    def fubiao(self,driver):
        u"浮标检查"
        sleep(1)
        driver.swipe(15,40,15,770,50)  # 移动浮标
        log.info('移动浮标')
        # self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_02@auto.png",way_name='channel')
        # driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.TextView",index=0).click()
        # self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_03@auto.png",way_name='channel')
        # driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.TextView",index=0).click()
        # self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_04@auto.png",way_name='channel')
        # driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.TextView",index=0).click()
        # self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_05@auto.png",way_name='channel')
        # driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.TextView",index=0).click()
        # self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_06@auto.png",way_name='channel')
        # driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.TextView",index=0).click()
        if self.wait_gone_images(driver, 'fubiao_06@auto.png',way_name='channel'):
            log.info('浮标检查成功')
            return "OK"
        else:
            log.info('浮标检查失败')
            return None
        
    def ali(self,driver):
        u'''支付宝支付'''
        driver(className='android.widget.RelativeLayout',resourceId="com.gionee.gsp:id/other_chan_rela_layout").click()
        driver(className='android.widget.RelativeLayout',index=1).click() #支付宝支付
        sleep(2)
        driver.press.back()
        #self.click_images(driver,"ali_pay_back@auto.png",way_name='channel')
        #self.click_images(driver,"ali_pay_back_yes@auto.png",way_name='channel')
        if self.images_or_none(driver, 'exists_02@auto.png',way_name='channel'):
            log.info('支付宝支付成功')
            return "OK"
        else:
            log.info('支付宝支付失败')
            return None
        
    def wechat(self,driver):
        u'''微信支付'''
        sleep(1)
        driver(className='android.widget.ListView',index=2).child(className='android.widget.RelativeLayout',index=0).click() #微信支付
        sleep(3)
        driver(className='android.widget.LinearLayout',index=0).child(className="android.widget.ImageView",index=0).click() #退出微信
        driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.ImageView",index=0).click() #支付退出确定
        if self.wait_gone_images(driver, 'exists_02@auto.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
        
    def exitGame(self,driver):
        # self.click_images(driver,"exitGame_01@auto.png",way_name='channel')
        sleep(1)
        driver.click(1160,652)
        if self.wait_gone_images(driver, 'exitGame_01@auto.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
    
        
        
        
                
        
        
        
        
        
                
        
        

        
    
        
        
        
                
        
        
        
        
        
                
        
        
