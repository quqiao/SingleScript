# coding=utf-8
#!/usr/bin/env python

from time import sleep, strftime
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
        u'''渠道login'''
        if self.images_or_none(driver,"login_02@auto.png",way_name='channel'):
            sleep(1)
            driver.click(self.info1(driver)*860, self.info2(driver)*350)  # 点击账号
            sleep(1)
            driver.clear_text()
            sleep(1)
            driver.type("17713623912", next=True)
            sleep(1)
            driver.type("test123")
            sleep(1)
            driver.click(self.info1(driver)*927, self.info2(driver)*696)  # 登录
            sleep(2)
            driver.click(self.info1(driver)*1530, self.info2(driver)*530)  # 开始游戏
            sleep(2)
            log.info('输入账号登录')
        else:
            sleep(1)
            driver.click(self.info1(driver)*1530, self.info2(driver)*530)  # 开始游戏
            sleep(2)
            log.info('自动登录')
        sleep(2)
        driver.click(self.info1(driver)*1860, self.info2(driver)*600)  # 浮标
        sleep(1)
        driver.click(self.info1(driver)*1680, self.info2(driver)*600)  # 隐藏浮标
        if self.wait_gone_images(driver, 'login_02@auto.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def exitGame(self, driver):
        sleep(1)
        driver.click(655, 569)  # 退出游戏
        sleep(2)
        if self.wait_gone_images(driver, 'login_01@auto.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None