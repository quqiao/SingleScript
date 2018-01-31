# coding=utf-8

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

    def login(self,driver):
        if self.images_or_none(driver, 'login_returnRegister.1920x1080.png', way_name='channel'):
            self.click_images(driver, "login_returnRegister.1920x1080.png", way_name='channel')
        self.click_images(driver, "login_oneButtonReg.1920x1080.png", way_name='channel')
        sleep(1)
        driver.click(self.info1(driver)*523, self.info2(driver)*548)
        sleep(1)
        driver.type('123456')
        sleep(2)
        self.click_images(driver, "login_sureRegister.1920x1080.png", way_name='channel')
        sleep(2)
        driver.click(self.info1(driver)*945, self.info2(driver)*755)
        sleep(2)
        self.click_images(driver, "login_registerEnterGame.1920x1080.png", way_name='channel')
        if self.wait_gone_images(driver, 'login_registerEnterGame.1920x1080.png', way_name='channel'):
            log.info('游戏注册成功')
            return 'ok'
        else:
            log.info('游戏注册失败')
            return None

    # def exitGame(self, driver):
    #     if self.images_or_none(driver, 'ucSDK_exitGame.1920x1080.png', way_name='channel'):
    #         self.click_images(driver, "ucSDK_exitGame.1920x1080.png", way_name='channel')
    #     if self.wait_gone_images(driver, 'ucSDK_exitGame.1920x1080.png', way_name='channel'):
    #         log.info('退出游戏成功')
    #         return 'ok'
    #     else:
    #         return None
