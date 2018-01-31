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
        self.images_or_none(driver, "login_01@auto.png", way_name='channel')
        driver.click(self.info1(driver)*650, self.info2(driver)*920)  # 取消实名
        log.info('自动登录')

        if self.wait_gone_images(driver, 'login_01@auto.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
    
    def fubiao(self,driver):
        u"浮标检查"
        sleep(2)
        driver.swipe(15,590,15,800,50)  # 移动浮标
        # self.click_images(driver,"fubiao_01@auto.png",way_name='channel')
        # self.click_images(driver,"fubiao_02@auto.png",way_name='channel')
        # driver(className="android.widget.RelativeLayout", resourceId="com.huawei.gamebox:id/player_nickname").click()
        # sleep(2)
        # driver.press.back()
        # driver(index=0, resourceId="com.huawei.gamebox:id/mine_score_linearlayout").click()
        # driver(className="android.widget.ImageView", resourceId="com.huawei.gamebox:id/back_to_homepage").click()
        # driver(index=1, resourceId="com.huawei.gamebox:id/mine_score_linearlayout").click()
        # sleep(2)
        # driver.press.back()
        # driver(index=2, resourceId="com.huawei.gamebox:id/mine_score_linearlayout").click()
        # sleep(2)
        # driver.press.back()
        # driver(index=3, resourceId="com.huawei.gamebox:id/mine_score_linearlayout").click()
        # sleep(2)
        # driver.press.back()
        # sleep(2)
        # driver.press.back()
        # driver.press.back()
        if self.wait_gone_images(driver, 'fubiao_02@auto.png',way_name='channel'):
            log.info('浮标检查成功')
            return "OK"
        else:
            log.info('浮标检查失败')
            return None
        
        
            
    def ali(self,driver):
        u'''支付宝支付'''
        '''
        sleep(2)
        #driver(className='android.widget.ListView',index=1).child(className="android.widget.LinearLayout",index=1).click()  #支付宝支付
        driver(className="android.widget.Button",index=3).click()
        sleep(8)
        driver(className='android.view.View',index=0).child(className="android.view.View",index=1).click() #支付宝返回
        driver(className='android.view.View',index=0).child(className="android.view.View",index=11).click() #支付宝确认返回
        '''
        self.click_images(driver,"ali_01@auto.png",way_name='channel')
        self.click_images(driver,"ali_02@auto.png",way_name='channel')
        self.click_images(driver,"ali_03@auto.png",way_name='channel')
        self.click_images(driver,"ali_04@auto.png",way_name='channel')
        if self.images_or_none(driver, 'ali_01@auto.png',way_name='channel'):
            log.info('支付宝支付成功')
            return "OK"
        else:
            log.info('支付宝支付失败')
            return None
        
    def wechat(self,driver):
        u'''微信支付'''
        '''
        driver(className='android.widget.ListView',index=1).child(className="android.widget.LinearLayout",index=2).click() #微信支付
        driver(className='android.widget.Button',index=3).click()
        sleep(3)
        driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.ImageView",index=0).click() #退出微信
        sleep(2)
        driver.keyevent('BACK')
        driver(className='android.widget.LinearLayout',index=1).child(className="android.widget.Button",index=1).click() #支付退出确定
        '''
        self.click_images(driver,"wechat_01@auto.png",way_name='channel')
        self.click_images(driver,"ali_02@auto.png",way_name='channel')
        self.click_images(driver,"wechat_02@auto.png",way_name='channel')
        self.click_images(driver,"wechat_03@auto.png",way_name='channel')
        self.click_images(driver,"wechat_04@auto.png",way_name='channel')
        if self.wait_gone_images(driver, 'exists_02@auto.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
        
    
        
        
        
                
        
        
        
        
        
                
        
        
