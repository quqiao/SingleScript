# coding=utf-8

from time import sleep, strftime
import public.methods as public
from public import logutils
import configure
import os
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
        u'''渠道login'''
        driver.prepare_ime()  # 准备输入法
        while (0 < 1):
            if driver(resourceId='com.vivo.sdkplugin:id/email_reg_title', className='android.widget.TextView',
                      text='帐号登录').exists:
                break
        if driver(resourceId='com.vivo.sdkplugin:id/email_reg_title', className='android.widget.TextView',
                  text='帐号登录').exists:
            driver(className="android.widget.EditText", resourceId="com.vivo.sdkplugin:id/account_num_input").click()
            driver.clear_text()
            print "请输入账号密码:"
            account = raw_input()
            driver.type(account)
            sleep(2)
            driver.prepare_ime()
            driver(className="android.widget.EditText",resourceId="com.vivo.sdkplugin:id/account_password_input").click()
            driver.clear_text()
            print "请输入账号密码:"
            password = raw_input()
            driver.type(password)
            sleep(2)
            driver(resourceId='com.vivo.sdkplugin:id/account_login',className='android.widget.Button',text='登  录').click()
            sleep(2)
            '''
            拖动的实名认证
            '''
            if driver(resourceId='com.vivo.sdkplugin:id/user_info_commit_btn',className='android.widget.Button',text='确认').exists:
                driver(resourceId='com.vivo.sdkplugin:id/titleLeftBtn', className='android.widget.TextView').click()#关闭实名认证
                sleep(2)
            if driver(resourceId='com.vivo.sdkplugin:id/vivo_acts_singletxt_dialog_check_btn',className='android.widget.TextView',text='查看详情').exists:
                driver(resourceId='com.vivo.sdkplugin:id/vivo_acts_singletxt_dialog_close', className='android.widget.RelativeLayout').child(className='android.widget.ImageView',index=0).click()  # 关闭渠道弹窗界面
                sleep(2)
            loginLogo = driver(resourceId='com.vivo.sdkplugin:id/email_reg_title', className='android.widget.TextView',
                      text='帐号登录').wait.gone(timeout=3000)
            if loginLogo:
                log.info('登录成功')
                return 'ok'
            else:
                log.info('登录失败')
                return None
        else:
            if driver(className='android.widget.TextView',text='实名制信息登记').exists:
                driver.click(self.info1(driver) * 1365, self.info2(driver) * 145)  # 关闭实名认证
            if driver(resourceId='com.vivo.sdkplugin:id/vivo_acts_singletxt_dialog_check_btn',className='android.widget.TextView',text='查看详情').exists:
                driver.click(self.info1(driver) * 1378, self.info2(driver) * 282)  # 关闭渠道弹窗界面
            loginLogo = driver(resourceId='com.vivo.sdkplugin:id/email_reg_title', className='android.widget.TextView',
                               text='帐号登录').wait.gone(timeout=3000)
            if loginLogo:
                log.info('自动登录成功')
                return 'ok'
            else:
                log.info('自动登录失败')
                return None
    
    def fubiao(self,driver):
        u"浮标检查"
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_02.1920x1080.png",way_name='channel')
        driver(index=1, resourceId="com.vivo.sdkplugin:id/vivo_title_close_btn").click()
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_03.1920x1080.png",way_name='channel')
        sleep(1)
        driver(index=3, resourceId="com.vivo.sdkplugin:id/vivo_title_close_btn").click()
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_04.1920x1080.png",way_name='channel')
        sleep(1)
        driver(index=3, resourceId="com.vivo.sdkplugin:id/vivo_title_close_btn").click()
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_05.1920x1080.png",way_name='channel')
        sleep(1)
        driver(index=1, resourceId="com.vivo.sdkplugin:id/vivo_title_close_btn").click()
        self.click_images(driver,"fubiao_01.1920x1080.png",way_name='channel')
        self.click_images(driver,"fubiao_06.1920x1080.png",way_name='channel')
        sleep(1)
        driver(index=1, resourceId="com.vivo.sdkplugin:id/vivo_title_close_btn").click()
        if self.wait_gone_images(driver, 'fubiao_06.1920x1080.png',way_name='channel'):
            log.info('浮标检查成功')
            return "OK"
        else:
            log.info('浮标检查失败')
            return None
        
    def ali(self,driver):
        u'''支付宝支付'''
        sleep(1)
        driver(className='android.widget.ListView',index=0).child(className='android.widget.RelativeLayout',index=1,clickable='true').click()
        driver(resourceId='com.vivo.sdkplugin:id/vivo_payment_btn_submit',index=3).click() #立即支付
        if self.images_or_none(driver, 'ali_pay_back.1920x1080.png',way_name='channel'):
            self.click_images(driver,"ali_pay_back.1920x1080.png",way_name='channel')
            self.click_images(driver,"ali_pay_back_yes.1920x1080.png",way_name='channel')
        else:
            driver.press.back()
        driver(resourceId='com.vivo.sdkplugin:id/vivo_payment_recharge_back',index=0).click()
        if self.wait_gone_images(driver, 'ali_pay_back.1920x1080.png',way_name='channel'):
            log.info('支付宝支付成功')
            return "OK"
        else:
            log.info('支付宝支付失败')
            return None
        
    def wechat(self,driver):
        u'''微信支付'''
        sleep(1)
        driver(className='android.widget.ListView',index=0).child(className='android.widget.RelativeLayout',index=0,clickable='true').click() #微信支付
        driver(resourceId='com.vivo.sdkplugin:id/vivo_payment_btn_submit',index=3).click()  #立即支付
        sleep(3)
        driver(className='android.widget.LinearLayout',index=0).child(className="android.widget.ImageView",index=0).click() #退出微信
        #driver(className='android.widget.RelativeLayout',index=0).child(className="android.widget.ImageView",index=0).click() #支付退出确定
        driver(resourceId='com.vivo.sdkplugin:id/vivo_payment_recharge_back',index=0).click()
        sleep(2)
        driver.press.back()
        driver(resourceId='com.vivo.sdkplugin:id/vivo_common_dlg_btn_positive',index=0).click()
        if self.wait_gone_images(driver, 'ali_pay_back.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
        
    def exitGame(self,driver):
        sleep(2)
        driver(resourceId='com.vivo.sdkplugin:id/vivo_app_exit_dialog_confirm_btn',index=0).click()
        if self.wait_gone_images(driver, 'ali_pay_back.1920x1080.png',way_name='channel'):
            log.info('微信支付成功')
            return "OK"
        else:
            log.info('微信支付失败')
            return None
       

