#!/usr/bin/env python
# coding=utf-8



from time import sleep, strftime,time
import public.methods as public
from public import logutils
import os
import configure
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def info1(self, driver):
        cmd = "adb -s %s shell wm size" %configure.device_name
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[1]
        g = float(f)
        x = g/1920.0
        return x

    def info2(self, driver):
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
        '''渠道login'''
        if self.images_or_none(driver, 'login_01.1920x1080.png',way_name='channel'):
            driver.click(self.info1(driver)*920, self.info2(driver)*360)  # 点击帐号输入框
            driver.type('18200130399',next=True)
            sleep(1)
            driver.type('5668080')
            sleep(2)
            driver.click(self.info1(driver)*910, self.info2(driver)*710)  # 进入游戏按钮
        else:
            print '自动登录'
        if self.wait_gone_images(driver, 'login_02.1920x1080.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None