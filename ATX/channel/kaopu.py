#!/usr/bin/env python
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

    def login(self, driver):
        sleep(20)
        if self.images_or_none(driver, 'login_01.1920x1080.png', way_name='channel'):
            driver.click(self.info1(driver)*650, self.info2(driver)*910)  # 立即注册
            sleep(1)
            driver.click(self.info1(driver)*1160, self.info2(driver)*660)  # 没有手机号
            sleep(1)
            driver.click(self.info1(driver)*1200, self.info2(driver)*880)  # 一键注册
            sleep(1)
            driver.click(self.info1(driver)*800, self.info2(driver)*360)  # 点击密码框
            sleep(1)
            driver.type('123456')
            sleep(1)
            driver.click(self.info1(driver)*900, self.info2(driver)*550)  # 注册
            sleep(1)
            driver.click(self.info1(driver)*680, self.info2(driver)*820)  # 截屏保存
            sleep(2)
            driver.click(self.info1(driver)*1130, self.info2(driver)*820)  # 登录
            self.images_or_none(driver, 'login_01.1920x1080.png', way_name='channel')
            driver.click(self.info1(driver)*1160, self.info2(driver)*900)  # 下次再说
            sleep(1)
            log.info('一键注册')
        else:
            sleep(1)
            driver.click(self.info1(driver)*900, self.info2(driver)*700)  # 登录
            sleep(1)
            driver.click(self.info1(driver)*1160, self.info2(driver)*900)  # 下次再说
            log.info('自动登录')
        if self.wait_gone_images(driver, 'login_01.1920x1080.png', way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None
            # self.click_images(driver, "register_rightNow.1920x1080.png", way_name='channel')
            # sleep(1)
            # self.click_images(driver, "noPhoneRegister.1920x1080.png", way_name='channel')
            # sleep(1)
            # self.click_images(driver, "fastRegister.1920x1080.png", way_name='channel')
            # sleep(1)
            # driver.click(self.info1(driver)*825, self.info2(driver)*373)
            # sleep(2)
            # driver.type('123456')
            # sleep(2)
            # driver.click(self.info1(driver)*961, self.info2(driver)*562)
            # if self.images_or_none(driver, 'screenShout.1920x1080.png', way_name='channel'):
            #     self.click_images(driver, "register_login.1920x1080.png", way_name='channel')
            # if self.images_or_none(driver, 'bindPhoneOrEmail.1920x1080.png', way_name='channel'):
            #     driver.click(self.info1(driver)*1219, self.info2(driver)*880)  # 点击下次再说
            # if self.wait_gone_images(driver, 'login_01.1920x1080.png', way_name='channel'):
            #     log.info('一键注册成功')
            #     return 'ok'
            # else:
            #     log.info('一键注册失败')
            #     if self.images_or_none(driver, 'login_01.1920x1080.png', way_name='channel'):
            #         driver.click(self.info1(driver)*950, self.info2(driver)*420)  # 账号
            #         sleep(1)
            #         driver.clear_text()
            #         sleep(1)
            #         driver.type("13488958799", next=True)
            #         sleep(1)
            #         driver.type("luo118413")
            #         sleep(1)
            #         driver.click(self.info1(driver)*900, self.info2(driver)*700)  # 登录
            #         sleep(2)
            #         # self.click_images(driver,"idInput.1920x1080.png",way_name='channel')
            #         # sleep(1)
            #         # driver.type("15198139230")
            #         # self.click_images(driver,"pswInput.1920x1080.png",way_name='channel')
            #         # sleep(1)
            #         # driver.type("a123123")
            #         # self.click_images(driver,"login.1920x1080.png",way_name='channel')
            #         # self.click_images(driver,"login_shiming_returnGame.1920x1080.png",way_name='channel')
            #     else:
            #         # self.click_images(driver,"login_shiming_returnGame.1920x1080.png",way_name='channel')
            #         log.info('自动登录成功')
            #     if self.wait_gone_images(driver, 'login_01.1920x1080.png', way_name='channel'):
            #         log.info('登录成功')
            #         return 'ok'
            #     else:
            #         log.info('登录失败')
            #         return None



    def exitGame(self,driver):
        sleep(1)
        driver.click(self.info1(driver)*659, self.info2(driver)*731)  # 退出游戏
        if self.wait_gone_images(driver, 'login_01.1920x1080.png',way_name='channel'):
            log.info('退出成功')
            return 'ok'
        else:
            log.info('退出失败')
            return None