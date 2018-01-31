#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep,time
import public.methods as public
from public import logutils
import os
log = logutils.getLogger(__name__)


class Game(public.Methods):
    def game_update(self,driver):
        for i in range(8):
            sleep(30)
            driver.click(500,500)
        if self.wait_gone_images(driver,'game_pre_01@auto.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
    def game_pre(self,driver):
        self.click_images(driver,"game_pre_01@auto.png")
        self.click_images(driver,"game_pre_02@auto.png")
        self.click_images(driver,"game_pre_03@auto.png")
        if self.wait_gone_images(driver,'game_pre_03@auto.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
        
    def guide(self,driver):
        ###########################################################
        cmd = "adb shell wm size"
        a = os.popen(cmd).read()
        c = a.split()
        d = c[2]
        e = d.split('x')
        f = e[1]
        g = float(f)
        f1 = e[0]
        g1 = float(f1)
        x = g/1920.0
        y = g1/1080.0
        ############################################################
        '''开始引导'''
        ###########################################################
        # if self.images_or_none(driver,"guide_001@auto.png"):
        ###########################################################
        self.images_or_none(driver,"guide_001@auto.png")  # 等待输入名字
        driver.click((x*780), (y*930))  # 点击输入框
        sleep(2)
        driver.type('12')
        sleep(2)
        driver.click((x*1430), (y*930))  # 创建角色
        sleep(2)
        driver.click((x*560), (y*280))  # 选择类型
        sleep(2)
        driver.click((x*1720), (y*950))  # 进入游戏
        sleep(5)
        driver.click(500, 500)  # 点击任意键
        sleep(1)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.click((x*1410), (y*320))  # 签到
        sleep(1)
        driver.click((x*928), (y*720))  # 确定
        sleep(1)
        driver.click(x*928, y*720)  # 确定
        sleep(1)
        driver.click(500, 500)  # 点击任意键
        '''舞创商城'''
        sleep(3)
        driver.click((x*950), (y*650))  # 舞创商城
        self.images_or_none(driver,"guide_002@auto.png")
        driver.click((x*920), (y*570))  # 普通商城
        self.images_or_none(driver,"guide_003@auto.png")
        driver.click((x*900), (y*350))  # 表情
        sleep(1)
        driver.click((x*900), (y*350))  # 表情
        sleep(1)
        driver.click((x*900), (y*350))  # 表情
        sleep(1)
        driver.long_click((x*1820), (y*50))   # 返回
        self.images_or_none(driver, "guide_002@auto.png")
        driver.long_click((x*1820), (y*50))   # 返回
        '''活跃'''
        self.images_or_none(driver,"guide_004@auto.png")
        driver.click((x*1720), (y*60))   # 活跃
        sleep(2)
        driver.click((x*890), (y*150))   # 常规任务
        sleep(2)
        driver.click((x*1288), (y*900))  # 领取奖励
        sleep(2)
        driver.click((x*1288), (y*900))  # 接受任务
        sleep(2)
        driver.click((x*1668), (y*90))  # 关闭
        '''游戏大厅'''
        sleep(2)
        driver.click((x*930), (y*400))  # 游戏大厅
        self.images_or_none(driver, "guide_005@auto.png")
        driver.click((x*65), (y*364))  # 设置
        sleep(2)
        driver.click((x*330), (y*265))  # 背包
        sleep(2)
        driver.click((x*1827), (y*200))  # 配饰
        sleep(2)
        driver.click((x*1248), (y*286))  # 头像
        sleep(2)
        driver.click((x*1823), (y*50))   # 返回
        '''活跃'''
        sleep(2)
        driver.click((x*1352), (y*43))   # 活跃
        sleep(2)
        driver.click((x*856), (y*150))   # 常规任务
        sleep(2)
        driver.click((x*1288), (y*900))  # 领取奖励
        sleep(2)
        driver.click((x*1288), (y*900))  # 接受任务
        sleep(2)
        driver.click((x*1668), (y*90))  # 关闭
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        '''创建房间'''
        sleep(2)
        driver.click((x*1027), (y*983))  # 创建房间
        sleep(2)
        driver.click((x*1150), (y*850))  # 确定
        self.images_or_none(driver, "guide_006@auto.png")
        sleep(2)
        driver.click((x*1560), (y*980))  # 随机场景
        sleep(2)
        driver.click((x*1150), (y*310))  # 随机歌曲
        sleep(2)
        driver.click((x*939), (y*985))  # 确定
        sleep(2)
        driver.long_click((x*1800), (y*964))  # 开始
        '''第一次跳舞'''
        self.images_or_none(driver, "guide_007@auto.png")
        driver.click((x*1710), (y*860))  # 下
        driver.click((x*1530), (y*730))  # 左
        driver.click((x*1710), (y*530))  # 上
        sleep(2)
        driver.click((x*190), (y*766))  # beat
        sleep(2)
        driver.click((x*190), (y*766))  # beat
        sleep(2)
        driver.click((x*1710), (y*860))  # 下
        driver.click((x*1530), (y*730))  # 左
        driver.click((x*1710), (y*530))  # 上
        sleep(10)
        driver.click((x*190), (y*766))  # beat
        sleep(2)
        driver.click((x*190), (y*766))  # beat
        sleep(3)
        driver.click(500, 500)  # 任意键
        sleep(3)
        driver.click((x*1710), (y*860))  # 下
        driver.click((x*1530), (y*730))  # 左
        driver.click((x*1710), (y*530))  # 上
        sleep(10)
        driver.click((x*190), (y*766))  # beat
        sleep(2)
        '''大厅'''
        self.images_or_none(driver, "guide_006@auto.png")
        driver.click((x*1818), (y*50))  # 大厅
        self.images_or_none(driver, "guide_005@auto.png")
        driver.click((x*1866), (y*50))  # 社区
        self.images_or_none(driver, "guide_004@auto.png")
        driver.click((x*1735), (y*36))  # 活跃
        sleep(2)
        driver.click((x*856), (y*150))   # 常规任务
        sleep(2)
        driver.click((x*1288), (y*900))  # 领取奖励
        sleep(2)
        driver.click((x*1288), (y*900))  # 接受任务
        sleep(2)
        driver.click((x*1668), (y*90))  # 关闭
        '''魔法屋'''
        self.images_or_none(driver, "guide_004@auto.png")
        driver.click((x*1620), (y*55))  # 魔法屋
        sleep(2)
        driver.click((x*969), (y*600))  # 碎片工坊
        sleep(2)
        driver.click(500, 500)  # 任意键
        sleep(2)
        driver.click(500, 500)  # 任意键
        sleep(2)
        driver.click((x*789), (y*750))  # 合成
        sleep(2)
        driver.click((x*1168), (y*731))  # 确定
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        sleep(2)
        driver.click((x*1710), (y*145))  # 关闭
        sleep(2)
        driver.click(500, 500)  # 点击任意键
        '''活跃'''
        sleep(2)
        driver.click((x*1735), (y*36))  # 活跃
        sleep(2)
        driver.click((x*856), (y*150))   # 常规任务
        sleep(2)
        driver.click((x*1288), (y*900))  # 领取奖励
        sleep(2)
        driver.click((x*1288), (y*900))  # 接受任务
        sleep(2)
        driver.click((x*1668), (y*90))  # 关闭
        #################################################
        # else:
        #     print '引导已完成'
        ################################################
        if self.wait_gone_images(driver, 'guide_001@auto.png'):
            log.info('游戏引导结束')
            return 'ok'
        
        else:
            log.info('游戏更新失败')
            return None

