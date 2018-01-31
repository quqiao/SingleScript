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
        cmd = "adb -s %s shell wm size" % configure.device_name
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[1]
        g = float(f)
        x = g/1920.0
        return x

    def info2(self, driver):
        cmd = "adb -s %s shell wm size" % configure.device_name
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[0]
        g = float(f)
        y = g/1080.0
        return y

    def guide(self, driver):
        while ( 0<1 ):
            if self.images_or_none(driver, "guide_01@auto.png"):
                break  # 等待进入游戏引导
        sleep(2)
        driver.click(self.info1(driver)*1750, self.info1(driver)*270)  # 跳过
        while ( 0<1 ):
            if self.images_or_none(driver, "guide_02@auto.png"):
                break  # 等待加载完成
        # driver.click(self.info1(driver)*340, self.info1(driver)*280)  # 对战模式
        # sleep(1)
        # driver.click(self.info1(driver)*300, self.info1(driver)*580)  # 指挥学院
        # sleep(2)
        # '''进化力量'''
        # driver.click(self.info1(driver)*1550, self.info1(driver)*980)  # 开始
        # sleep(1)
        # while ( 0<1 ):
        #     if self.images_or_none(driver, "guide_03@auto.png"):
        #         break  # 等待加载完成
        # driver.click(self.info1(driver)*380, self.info1(driver)*990)  # 部署1
        # sleep(1)
        # driver.click(self.info1(driver)*150, self.info1(driver)*800)  # 选择兵种1
        # sleep(5)
        # driver.click(500,500)  # 点击任意
        # sleep(2)
        # driver.click(self.info1(driver)*380, self.info1(driver)*990)  # 部署1
        # sleep(1)
        # driver.click(self.info1(driver)*900, self.info1(driver)*500)  # 升级兵种
        # sleep(1)
        # driver.click(self.info1(driver)*1120, self.info1(driver)*720)  # 确定升级
        # sleep(1)
        # driver.click(self.info1(driver)*1380, self.info1(driver)*980)  # 开始战斗
        # while ( 0<1 ):
        #     if self.images_or_none(driver, "guide_04@auto.png"):
        #         break  # 等待战斗完成
        # sleep(1)
        # driver.click(self.info1(driver)*960, self.info1(driver)*780)  # 确定
        # sleep(1)
        # driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 离开训练
        # while ( 0<1 ):
        #     if self.images_or_none(driver, "guide_05@auto.png"):
        #         break  # 等待退出完成
        # '''暗影突袭'''
        # sleep(2)
        # driver.click(self.info1(driver)*1550, self.info1(driver)*980)  # 开始
        # sleep(15)
        # driver.click(500,500)  # 点击任意键
        # sleep(1)
        # driver.click(self.info1(driver)*380, self.info1(driver)*990)  # 部署1
        # sleep(2)
        # driver.click(self.info1(driver)*150, self.info1(driver)*800)  # 选择兵种1
        # sleep(5)
        # driver.click(self.info1(driver)*520, self.info1(driver)*990)  # 部署2
        # sleep(2)
        # driver.click(self.info1(driver)*220, self.info1(driver)*780)  # 选择兵种2
        # sleep(2)
        # driver.click(self.info1(driver)*1380, self.info1(driver)*980)  # 开始战斗
        # while ( 0<1 ):
        #     if self.images_or_none(driver, "guide_04@auto.png"):
        #         break  # 等待战斗完成
        # sleep(1)
        # driver.click(self.info1(driver)*960, self.info1(driver)*780)  # 确定
        # sleep(1)
        # driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 离开训练
        # while ( 0<1 ):
        #     if self.images_or_none(driver, "guide_05@auto.png"):
        #         break  # 等待退出完成
        # '''全数击落'''
        # sleep(1)
        # driver.click(self.info1(driver)*1550, self.info1(driver)*980)  # 开始
        # sleep(15)
        # driver.click(500, 500)  # 任意键继续
        # sleep(2)
        # driver.click(self.info1(driver)*380, self.info1(driver)*990)  # 部署1
        # sleep(1)
        # driver.click(self.info1(driver)*150, self.info1(driver)*800)  # 选择兵种1
        # sleep(5)
        # driver.click(self.info1(driver)*380, self.info1(driver)*990)  # 部署1
        # sleep(2)
        # driver.click(self.info1(driver)*1260, self.info1(driver)*700)  # 确定升级
        # sleep(3)
        # driver.click(self.info1(driver)*1380, self.info1(driver)*980)  # 开始战斗
        # while ( 0<1 ):
        #     if self.images_or_none(driver, "guide_04@auto.png"):
        #         break  # 等待战斗完成
        # sleep(1)
        # driver.click(self.info1(driver)*960, self.info1(driver)*780)  # 确定
        # sleep(1)
        # driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 离开训练
        # '''事半功倍'''
        # sleep(9)
        # driver.click(self.info1(driver)*1550, self.info1(driver)*980)  # 开始
        # sleep(15)
        # driver.click(500, 500)  # 点击任意键继续
        # sleep(2)
        # driver.click(self.info1(driver)*380, self.info1(driver)*990)  # 部署1
        # sleep(1)
        # driver.click(self.info1(driver)*150, self.info1(driver)*800)  # 选择兵种1
        # sleep(5)
        # driver.click(500, 500)  # 点击任意键
        # sleep(2)
        # driver.click(self.info1(driver)*380, self.info1(driver)*990)  # 部署1
        # sleep(2)
        # driver.click(self.info1(driver)*1290, self.info1(driver)*510)  # 增加数量
        # sleep(1)
        # driver.click(self.info1(driver)*1260, self.info1(driver)*700)  # 确定升级
        # sleep(1)
        # driver.click(self.info1(driver)*1380, self.info1(driver)*980)  # 开始战斗
        # while ( 0<1 ):
        #     if self.images_or_none(driver, "guide_04@auto.png"):
        #         break  # 等待战斗完成
        # sleep(1)
        # driver.click(self.info1(driver)*960, self.info1(driver)*780)  # 确定
        # sleep(1)
        # driver.click(self.info1(driver)*960, self.info1(driver)*900)  # 离开训练
        # sleep(3)
        # '''对战模式'''
        # driver.click(self.info1(driver)*80, self.info1(driver)*50)  # 返回
        # sleep(1)
        # driver.click(self.info1(driver)*360, self.info1(driver)*280)  # 对战模式
        # sleep(1)
        # driver.click(self.info1(driver)*400, self.info1(driver)*400)  # 匹配对战
        # sleep(1)
        # driver.click(self.info1(driver)*625, self.info1(driver)*260)  # 1v1
        # sleep(1)
        # driver.click(self.info1(driver)*900, self.info1(driver)*920)  # 开始游戏

        if self.wait_gone_images(driver, 'guide_01@auto.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
