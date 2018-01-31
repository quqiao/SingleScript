#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
import os
import configure
log = logutils.getLogger(__name__)

class Game(public.Methods):

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

    def guide(self, driver):
        # if self.images_or_none(driver, 'guide_01@auto.png'):
        for i in range(15):
            driver.click(self.info1(driver)*600, self.info2(driver)*600)  # 跳过
        sleep(1)
        driver.long_click(self.info1(driver)*480, self.info2(driver)*730)  # 长按前进
        self.images_or_none(driver, 'guide_02@auto.png')  # 对话
        driver.click(self.info1(driver)*1400, self.info2(driver)*870)  # 对话跳过
        sleep(1)
        driver.long_click(self.info1(driver)*480, self.info2(driver)*730)  # 长按前进
        self.images_or_none(driver, 'guide_02@auto.png')  # 对话
        driver.click(self.info1(driver)*1400, self.info2(driver)*870)  # 对话跳过
        sleep(1)
        driver.long_click(self.info1(driver)*480, self.info2(driver)*730)  # 长按前进
        self.images_or_none(driver, 'guide_02@auto.png')  # 对话
        driver.click(self.info1(driver)*1400, self.info2(driver)*870)  # 对话跳过
        sleep(1)
        driver.long_click(self.info1(driver)*480, self.info2(driver)*730)  # 长按前进
        self.images_or_none(driver, 'guide_02@auto.png')  # 对话
        driver.click(self.info1(driver)*1400, self.info2(driver)*870)  # 对话跳过
        sleep(2)
        driver.click(self.info1(driver)*1400, self.info2(driver)*870)  # 对话跳过
        sleep(1)
        driver.long_click(self.info1(driver)*160, self.info2(driver)*720)  # 长按后退
        self.images_or_none(driver, 'guide_02@auto.png')  # 对话
        driver.click(self.info1(driver)*1400, self.info2(driver)*870)  # 对话跳过
        sleep(1)
        driver.click(self.info1(driver)*1640, self.info2(driver)*800)  # 火箭
        self.images_or_none(driver, 'guide_02@auto.png')  # 对话
        driver.click(self.info1(driver)*1400, self.info2(driver)*870)  # 对话跳过
        sleep(1)
        driver.click(self.info1(driver)*1400, self.info2(driver)*870)  # 对话跳过
        sleep(1)
        driver.click(self.info1(driver)*1400, self.info2(driver)*870)  # 对话跳过
        sleep(3)
        driver.swipe(self.info1(driver)*1850, self.info2(driver)*30, self.info1(driver)*1850, self.info2(driver)*30, 10)  # 设置
        sleep(1)
        driver.click(2000, 30)  # 小米mix2设置
        sleep(1)
        driver.click(self.info1(driver)*760, self.info2(driver)*950)  # 返回大厅
        # else:
        #     log.info('没有引导')
        if self.wait_gone_images(driver, 'guide_02@auto.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None



