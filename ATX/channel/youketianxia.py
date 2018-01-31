#!/usr/bin/env python
# coding=utf-8


from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        driver(className="android.widget.TextView", resourceId="com.ttxw.yktx:id/register_goLogin").click()#点击已有账号
        sleep(1)
        driver(className="android.widget.EditText", resourceId="com.ttxw.yktx:id/login_username").click()#用户名
        sleep(1)
        driver.type("15528377554",next=True) #输入账号
        driver.type("123456") #输入密码
        sleep(1)
        driver(className="android.widget.TextView", resourceId="com.ttxw.yktx:id/login_loginBtn").click()#立即登录
        sleep(2)
        driver(className="android.widget.TextView", resourceId="com.ttxw.yktx:id/usercenter_enter").click()#进入游戏
        if self.wait_gone_images(driver, 'login@auto.png',timeout=40,way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
        
