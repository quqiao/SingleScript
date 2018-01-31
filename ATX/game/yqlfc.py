#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)
import os
import configure
import threading

class Game(public.Methods):
    def __init__(self):
        pass

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

    def game_triggered(self, driver):
        driver.watcher(u"oppoR7安全警告").when(text = u"允许")\
                                         .click(text = u"允许")
        print driver.watcher(u"oppoR7安全警告").triggered

    def safeWarn(device):
        if device(text='Force Close').exists:
            device(text='Force Close').click()
        return True

    def game_update(self, driver):
        driver.prepare_ime()
        while ( 0<1 ):
            if self.images_or_none(driver, "game_update_01@auto.png"):
                self.click_images(driver, "game_update_01@auto.png")
                break

        if self.wait_gone_images(driver,'game_update_01@auto.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
    def game_pre(self, driver):
        self.images_or_none(driver,"game_pre_01@auto.png")
        sleep(1)
        driver.click(self.info1(driver)*955, self.info2(driver)*858)  # 确定
        sleep(2)
        driver.click(self.info1(driver)*1240, self.info2(driver)*690)  # 选区
        sleep(1)
        driver.click(self.info1(driver)*150, self.info2(driver)*400)  # 1区-12区
        sleep(1)
        driver.click(self.info1(driver)*150, self.info2(driver)*400)  # 1区-12区
        sleep(1)
        driver.click(self.info1(driver)*700, self.info2(driver)*310)  # 秋名山
        # driver.click(self.info1(driver)*1550, self.info2(driver)*310)  # 盐湖城
        # driver.click(self.info1(driver)*700, self.info2(driver)*420)  # 巴塞罗那
        # driver.click(self.info1(driver)*1550, self.info2(driver)*420)  # 九州岛
        sleep(1)
        driver.click(self.info1(driver)*900, self.info2(driver)*900)  # 开始
        if self.wait_gone_images(driver, 'game_pre_01@auto.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
        
    def guide(self, driver):
        if self.images_or_none(driver, 'guide_01@auto.png'):  # 头像
            sleep(1)
            driver.click(self.info1(driver)*1200, self.info2(driver)*930)  # 随机
            sleep(1)
            driver.click(self.info1(driver)*1650, self.info2(driver)*923)  # 开始
            sleep(8)
            self.images_or_none(driver, 'guide_02@auto.png')  # 对话出现
            sleep(1)
            driver.click(500, 500)  # 随机点击屏幕
            sleep(2)
            self.images_or_none(driver, 'guide_02@auto.png')  # 对话出现
            sleep(1)
            driver.click(500, 500)  # 随机点击屏幕
            '''右转'''
            sleep(1)
            driver.swipe(self.info1(driver)*1000, self.info2(driver)*500, self.info1(driver)*1000, self.info2(driver)*500, 50)  # 右转
            sleep(3)
            '''左转'''
            driver.swipe(self.info1(driver)*400, self.info2(driver)*500, self.info1(driver)*400, self.info1(driver)*500, 40)  # 左转
            self.images_or_none(driver, 'guide_02@auto.png')  # 对话出现
            sleep(1)
            driver.click(500, 500)  # 随机点击屏幕
            sleep(3)
            self.images_or_none(driver, 'guide_02@auto.png')  # 对话出现
            sleep(1)
            driver.click(500, 500)  # 随机点击屏幕
            sleep(3)
            '''左漂移'''
            def long1():
                driver.swipe(400, 500, 400, 500, 10)
                # driver.click(400, 500)

            def long2():
                driver.swipe(1200, 500, 1200, 500, 10)
                # driver.click(1200, 500)

            threads1 = []
            t1 = threading.Thread(target=long1)
            threads1.append(t1)
            t2 = threading.Thread(target=long2)
            threads1.append(t2)
            for t in threads1:
                t.start()
            sleep(1)

            threads2 = []
            t1 = threading.Thread(target=long1)
            threads2.append(t1)
            t2 = threading.Thread(target=long2)
            threads2.append(t2)
            for t in threads2:
                t.start()
            sleep(1)

            threads3 = []
            t1 = threading.Thread(target=long1)
            threads3.append(t1)
            t2 = threading.Thread(target=long2)
            threads3.append(t2)
            for t in threads3:
                t.start()
            sleep(1)

            threads4 = []
            t1 = threading.Thread(target=long1)
            threads4.append(t1)
            t2 = threading.Thread(target=long2)
            threads4.append(t2)
            for t in threads4:
                t.start()
            sleep(1)

            threads5 = []
            t1 = threading.Thread(target=long1)
            threads5.append(t1)
            t2 = threading.Thread(target=long2)
            threads5.append(t2)
            for t in threads5:
                t.start()
            sleep(1)

            driver.long_click(400, 500)  # 长按左漂移
            sleep(6)
            '''右漂移'''
            # for i in range(2):
            #     self.images_or_none(driver,'guide_003@auto.png')
            #     driver.click(0.5,0.5)

            threads6 = []
            t1 = threading.Thread(target=long2)
            threads6.append(t1)
            t2 = threading.Thread(target=long1)
            threads6.append(t2)
            for t in threads6:
                t.start()
            sleep(1)

            threads7 = []
            t1 = threading.Thread(target=long2)
            threads7.append(t1)
            t2 = threading.Thread(target=long1)
            threads7.append(t2)
            for t in threads7:
                t.start()
            sleep(1)

            threads8 = []
            t3 = threading.Thread(target=long2)
            threads8.append(t3)
            t4 = threading.Thread(target=long1)
            threads8.append(t4)
            for t in threads8:
                t.start()
            sleep(1)

            threads9 = []
            t3 = threading.Thread(target=long2)
            threads9.append(t3)
            t4 = threading.Thread(target=long1)
            threads9.append(t4)
            for t in threads9:
                t.start()
            sleep(1)

            threads10 = []
            t3 = threading.Thread(target=long2)
            threads10.append(t3)
            t4 = threading.Thread(target=long1)
            threads10.append(t4)
            for t in threads10:
                t.start()
            sleep(1)

            driver.long_click(1200, 500)  # 长按右漂移
            sleep(2)
            '''氮气'''
            self.images_or_none(driver, "guide_03@auto.png")  # 氮气
            driver.click(self.info1(driver)*130, self.info2(driver)*500)  # 氮气
            self.images_or_none(driver, 'guide_02@auto.png')  # 对话出现
            driver.click(500, 500)  # 随机点击屏幕
            '''设置'''
            self.images_or_none(driver, "guide_04@auto.png")
            driver.click(self.info1(driver)*70, self.info2(driver)*40)  # 设置
            sleep(1)
            driver.click(self.info1(driver)*1516, self.info2(driver)*895)  # 确定
            sleep(1)
            driver.click(self.info1(driver)*955, self.info2(driver)*815)  # 确定2
            sleep(3)
            driver.click(500, 500)  # 随机点击屏幕
            '''任务'''
            self.images_or_none(driver, 'guide_05@auto.png')  # 任务
            driver.swipe(self.info1(driver)*1850, self.info2(driver)*590, self.info1(driver)*1850, self.info2(driver)*590, 10)  # 任务
            sleep(2)
            driver.click(self.info1(driver)*1690, self.info2(driver)*260)  # 领取
            sleep(2)
            driver.click(self.info1(driver)*960, self.info2(driver)*890)  # 确认
            sleep(2)
            driver.click(self.info1(driver)*960, self.info2(driver)*955)  # 任意
            sleep(2)
            driver.click(self.info1(driver)*960, self.info2(driver)*960)  # 领取2
            sleep(1)
            driver.click(self.info1(driver)*60, self.info2(driver)*40)  # 任务
            sleep(4)
            driver.click(self.info1(driver)*960, self.info2(driver)*890)  # 确定
            # sleep(2)
            # driver.click(self.info1(driver)*1710, self.info2(driver)*130)  # 关闭
            self.click_images(driver, 'guide_06@auto.png')  # 关闭
            sleep(3)
            driver.click(960, 500)  # 任意
            '''开始游戏'''
            sleep(2)
            driver.click(self.info1(driver)*1660, self.info2(driver)*960)  # 开始游戏
            sleep(2)
            driver.click(self.info1(driver)*760, self.info2(driver)*970)  # 剧情模式
            sleep(2)
            driver.click(self.info1(driver)*50, self.info2(driver)*40)  # 返回
            sleep(2)
            driver.click(self.info1(driver)*50, self.info2(driver)*40)  # 返回
            sleep(2)
            log.info('游戏引导结束')

        else:
            # while ( 0<1 ):
            #     driver.click(self.info1(driver)*960, self.info2(driver)*890)  # 确定1
            #     driver.click(self.info1(driver)*1700, self.info2(driver)*130)  # 关闭1
            #     driver.click(self.info1(driver)*965, self.info2(driver)*700)  # 确定2
            #     if self.exist(driver, "guide_07@auto.png"):
            #         break
            # sleep(1)
            # driver.click(self.info1(driver)*1660, self.info2(driver)*960)  # 开始游戏
            # sleep(1)
            # driver.click(self.info1(driver)*760, self.info2(driver)*990)  # 剧情模式
            # sleep(1)
            # driver.click(self.info1(driver)*500, self.info2(driver)*500)  # 任意键继续
            # sleep(1)
            # driver.click(self.info1(driver)*50, self.info2(driver)*40)  # 返回
            # sleep(1)
            # driver.click(self.info1(driver)*50, self.info2(driver)*40)  # 返回
            # sleep(1)
            log.info('不用过游戏引导')
        if self.wait_gone_images(driver, 'guide_05@auto.png'):
            log.info('游戏引导成功')
            return 'ok'
        else:
            log.info('游戏引导失败')
            return None

    def basicFunction(self,driver):
        driver.click(1300,1030)  # 商城
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        driver.click(1058,1030)  # 宠物
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        driver.click(830,1030)  # 车库
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        driver.click(580,1030)  # 赛事
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        # driver.click(350,1030)  # 车队
        # sleep(2)
        driver.click(100,1030)  # 社交
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        driver.click(65,400)  # 转盘
        sleep(3)
        driver.click(50,40)  # 返回
        sleep(2)
        driver.click(65,250)  # 活动
        sleep(2)
        driver.click(1700,150)  # 关闭
        sleep(2)
        driver.click(580,60)  # 充值
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        driver.click(700,60)  # 首充
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        driver.click(1688,45)  # 邮件
        sleep(2)
        driver.click(1700,100)  # 关闭
        sleep(2)
        driver.click(1780,45)  # 设置
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        driver.click(1750,500)  # 背包
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        driver.click(1750,688)  # 成长
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        driver.swipe(1850,400,1850,400,10)  # 排行
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        driver.swipe(1850,600,1850,600,10)  # 任务
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        # self.click_images(driver,"basic_001@auto.png")
        # self.click_images(driver,"basic_002@auto.png")
        # self.click_images(driver,"basic_003@auto.png")
        # self.click_images(driver,"basic_004@auto.png")
        # self.click_images(driver,"basic_005@auto.png")
        # self.click_images(driver,"basic_004@auto.png")
        # self.click_images(driver,"basic_006@auto.png")
        # self.click_images(driver,"basic_007@auto.png")
        # self.click_images(driver,"basic_004@auto.png")
        # self.click_images(driver,"basic_008@auto.png")
        # self.click_images(driver,"basic_009@auto.png")
        # self.click_images(driver,"basic_010@auto.png")
        # self.click_images(driver,"basic_011@auto.png")
        # self.click_images(driver,"basic_012@auto.png")
        # self.click_images(driver,"basic_004@auto.png")
        # self.click_images(driver,"basic_013@auto.png")
        # self.click_images(driver,"basic_004@auto.png")
        # self.click_images(driver,"basic_014@auto.png")
        # self.click_images(driver,"basic_002@auto.png")
        if self.wait_gone_images(driver, 'basic_002@auto.png'):
            log.info('基本功能检查成功')
            return 'ok'
        else:
            log.info('基本功能检查失败')
            return None
        
    '''飞车祈愿'''
    def live(self,driver):
        sleep(2)
        driver.click(60,550)  # 祈愿
        sleep(9)
        driver.click(1669,1018)  # 关闭有虚拟硬件
        driver.click(1791,1022)  # 关闭没有虚拟硬件
        sleep(2)
        # self.click_images(driver,"live_001@auto.png")
        # self.click_images(driver,"live_002@auto.png")
        if self.wait_gone_images(driver, 'live_002@auto.png'):
            return 'ok'
            log.info('飞车祈愿检查成功')
        else:
            return None
            log.info('飞车祈愿检查失败')
        
    '''飞车社区'''
    def gonglue(self,driver):
        sleep(2)
        driver.click(1755,300)  # 社区
        sleep(5)
        driver.click(85,335)  # 红人
        sleep(2)
        driver.click(85,580)  # 攻略
        sleep(2)
        driver.click(85,820)  # 个人
        sleep(2)
        driver.click(1669,1018)  # 关闭有虚拟硬件
        driver.click(1791,1022)  # 关闭没有虚拟硬件
        sleep(2)
        # self.click_images(driver,"gonglue_01@auto.png")
        # self.click_images(driver,"gonglue_02@auto.png")
        # self.click_images(driver,"gonglue_03@auto.png")
        # self.click_images(driver,"gonglue_04@auto.png")
        # self.click_images(driver,"gonglue_05@auto.png")
        if self.wait_gone_images(driver, 'gonglue_02@auto.png'):
            return 'ok'
            log.info('飞车社区检查成功')
        else:
            return None
            log.info('飞车社区检查失败')
        
    '''飞车特惠 '''
    def store(self,driver):
        sleep(2)
        driver.swipe(1846,785,1846,785,10)  # 特惠1920*1080
        # driver.swipe(1230,520,1230,520,10)  # 特惠1280*720
        sleep(5)
        driver.click(1669,1018)  # 关闭有虚拟硬件
        driver.click(1791,1022)  # 关闭没有虚拟硬件
        sleep(2)
        # self.click_images(driver,"store_02@auto.png")
        if self.wait_gone_images(driver, 'store_02@auto.png'):
            return 'ok'
        else:
            return None
        
    '''飞车邀请'''   
    def lingzuan(self,driver):
        sleep(2)
        driver.swipe(1846,230,1846,230,10)  # 邀请1920*1080
        # driver.swipe(1230,150,1230,150,10)  # 邀请1280*720
        sleep(8)
        driver.click(1669,1018)  # 关闭有虚拟硬件
        driver.click(1791,1022)  # 关闭没有虚拟硬件
        sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # self.click_images(driver,"lingzuan_04@auto.png")
        # sleep(2)
        # driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=0).click()
        # self.click_images(driver,"lingzuan_02@auto.png")
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # self.click_images(driver,"lingzuan_04@auto.png")
        # sleep(2)
        # driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=1).click()
        # self.click_images(driver,"lingzuan_02@auto.png")
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # self.click_images(driver,"lingzuan_04@auto.png")
        # sleep(2)
        # driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=2).click()
        # sleep(2)
        # driver.press.back()
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # self.click_images(driver,"lingzuan_04@auto.png")
        # self.click_images(driver,"lingzuan_01@auto.png")
        # sleep(3)
        # driver.press.back()
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # self.click_images(driver,"lingzuan_04@auto.png")
        # sleep(2)
        # driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=4).click()
        # sleep(2)
        # driver.press.back()
        # driver.press.back()
        # sleep(1)
        # driver(className="android.widget.TextView",text="不保存").click()
        # self.click_images(driver,"lingzuan_03@auto.png")
        if self.wait_gone_images(driver, 'lingzuan_04@auto.png'):
            return 'ok'
            log.info('飞车邀请成功')
        else:
            return None
            log.info('飞车邀请失败')

    '''飞车任务'''    
    def saishi(self,driver):
        sleep(2)
        driver.swipe(1846,597,1846,597,10)  # 任务1920*1080
        # driver.swipe(1230,393,1230,393,10)  # 任务1280*760
        sleep(2)
        driver.click(150,350)  # 成就任务
        sleep(2)
        driver.click(150,350)  # 日常任务
        sleep(2)
        driver.click(150,510)  # 车队任务
        sleep(2)
        driver.click(150,820)  # 情侣任务
        sleep(2)
        driver.click(150,960)  # 王爵任务
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        # self.click_images(driver,"saishi_02@auto.png")
        # self.click_images(driver,"saishi_03@auto.png")
        # self.click_images(driver,"saishi_04@auto.png")
        # self.click_images(driver,"saishi_05@auto.png")
        # self.click_images(driver,"saishi_06@auto.png")
        # self.click_images(driver,"saishi_07@auto.png")
        if self.wait_gone_images(driver, 'saishi_07@auto.png'):
            return 'ok'
            log.info('飞车任务检查成功')
        else:
            return None
            log.info('飞车任务检查失败')

    def talking(self,driver):
        # self.click_images(driver,"talking_01@auto.png")
        # self.click_images(driver,"talking_02@auto.png")
        sleep(2)
        driver.click(138,858)  # 对话
        sleep(2)
        driver.click(330,1000)  # 对话框
        sleep(2)
        driver(className='android.widget.EditText',index=0).click()
        driver.type(u"毛泽东法轮功江泽民")
        sleep(2)
        driver.click(1700,912)  # 输入框确定 有底部虚拟
        sleep(1)
        driver.click(1840,932)  # 输入框确定 无底部虚拟
        # driver(className='android.widget.Button',index=1).click()
        sleep(2)
        driver.click(750,1000)  # 发送
        sleep(5)
        driver.click(930,530)  # 关闭对话框
        sleep(2)
        # self.click_images(driver,"talking_03@auto.png")
        # self.click_images(driver,"talking_04@auto.png")
        if self.wait_gone_images(driver, 'talking_04@auto.png'):
            return 'ok'
            log.info('对话检查成功')
        else:
            return None
            log.info('对话检查失败')
        
    def setting(self,driver):
        # self.click_images(driver,"setting_01@auto.png")
        sleep(2)
        driver.click(1776,49)  # 设置1920*1080
        # driver.click(1170,115)  # 设置1280*760
        sleep(2)
        driver.click(50,40)  # 返回
        sleep(2)
        # self.click_images(driver,"setting_02@auto.png")
        if self.wait_gone_images(driver, 'setting_02@auto.png'):
            log.info('游戏中设置检查成功')
            return 'ok'
        else:
            log.info('游戏中设置检查失败')
            return None

    def exitgame(self,driver):
        sleep(2)
        driver.press.back()  # 返回键
        # self.click_images(driver,"exitgame_01@auto.png")
        if self.wait_gone_images(driver, 'exitgame_01@auto.png'):
            log.info('游戏中退出按钮成功')
            return 'ok'
        else:
            log.info('游戏中退出按钮失败')
            return None



