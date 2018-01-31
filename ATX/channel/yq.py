# coding=utf-8
#朋友玩渠道SDK测试用例
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

    # def register(self,driver):#手机号注册
    def login(self,driver):
        if self.images_or_none(driver, 'login_logo.1920x1080.png', way_name='channel'):
            if self.images_or_none(driver, 'login_user_null.1920x1080.png', way_name='channel')!=True:
                self.click_images(driver, 'login_user_list.1920x1080.png', way_name='channel')
                sleep(1)
                self.click_images(driver, 'login_clear.1920x1080.png', way_name='channel')
            sleep(2)
            driver.click(self.info1(driver)*841, self.info2(driver)*418)  # 点击账号输入框
            sleep(2)
            driver.type('15883980943', next=True)
            sleep(2)
            driver.type('123456')
            sleep(2)
            driver.click(self.info1(driver)*977, self.info2(driver)*701)  # 点击进入游戏
            driver.click(self.info1(driver)*977, self.info2(driver)*701)  # 点击进入游戏
            if self.wait_gone_images(driver,'login_logo.1920x1080.png',way_name='channel'):
                log.info('输入账号登录成功')
                return 'ok'
            else:
                log.info('输入账号登录失败')
                return None
        else:
            log.info('自动登录成功')
            return 'ok'
        if self.wait_gone_images(driver, 'login_logo.1920x1080.png', way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    # def exitGame(self, driver):
    #     if self.images_or_none(driver, 'ucSDK_exitGame.1920x1080.png', way_name='channel'):
    #         self.click_images(driver, "ucSDK_exitGame.1920x1080.png", way_name='channel')
    #     if self.wait_gone_images(driver, 'ucSDK_exitGame.1920x1080.png', way_name='channel'):
    #         log.info('退出游戏成功')
    #         return 'ok'
    #     else:
    #         return None

