#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import configure
import public.methods as public
from public import logutils
import os
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

    def game_update(self,driver):
        driver.prepare_ime()
        ##########热更渠道才会用的##########
        # while ( 0<1 ):
        #     if self.images_or_none(driver,"exit@auto.png"):
        #         self.click_images(driver,"exit@auto.png")
        #         break
        # sleep(2)
        # driver.start_app(configure.package_name,configure.activity_name)
        sleep(30)
        self.images_or_none(driver, 'game_update_01@auto.png')
        sleep(1)
        driver.click(self.info1(driver)*1262, self.info2(driver)*419)  # 选择服务器
        sleep(2)
        driver.click(self.info1(driver)*955, self.info2(driver)*895)  # 进入游戏
        if self.wait_gone_images(driver, 'game_update_01@auto.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None

    def enter_game(self, driver):
        self.click_images(driver, "enter_game1@auto.png")
        # self.click_images(driver,"server_HuaNan@auto.png")
        if self.wait_gone_images(driver,'enter_game1@auto.png'):
            return 'ok'
        else:
            return None

        # if self.guide_exist(driver,'guide_001'):  #判断是否需要过指引
        #     result = self.game_click(driver, 'guide')  #过指引
        #     return result
        # else:
        #     result = self.game_click2(driver, 'enter_game')      #不需要过指引的操作
        #     return result

    
    def game_pre(self,driver):
        if self.images_or_none(driver, 'suiJiRename@auto.png'):#判断是否存在随机
            self.click_images(driver, 'suiJiRename@auto.png')
        if self.images_or_none(driver, 'enter_game@auto.png'):
            self.click_images(driver, 'enter_game@auto.png')
        log.info('枪战没有游戏前准备')
        if self.wait_gone_images(driver,'enter_game@auto.png'):
            return 'ok'
        else:
            return None 

       
    def guide(self,driver):
        '''引导第一次战斗'''
        # if self.images_or_none(driver,'guide_001@auto.png'):
        sleep(1)
        driver.click(self.info1(driver)*1366, self.info2(driver)*778)  # 扔骰子
        sleep(2)
        driver.click(self.info1(driver)*965, self.info2(driver)*945)  # 进入游戏
        sleep(10)
        self.images_or_none(driver, 'guide_002@auto.png')  # 跳过
        sleep(1)
        driver.click(self.info1(driver)*900, self.info2(driver)*750)  # 跳过
        sleep(1)
        driver.click(self.info1(driver)*900, self.info2(driver)*500)  # 关闭弹出框
        sleep(1)
        driver.click(self.info1(driver)*780, self.info2(driver)*1024)  # 战斗
        sleep(1)
        driver.click(self.info1(driver)*1168, self.info2(driver)*210)  # 单人模式
        sleep(1)
        driver.click(self.info1(driver)*610, self.info2(driver)*480)  # 机器人关卡
        sleep(5)
        driver.click(self.info1(driver)*398, self.info2(driver)*500)  # 第一个机器人关卡
        sleep(1)
        driver.click(self.info1(driver)*1385, self.info2(driver)*850)  # 开始
        sleep(1)
        self.images_or_none(driver, 'guide_003@auto.png')  # 确认开始战斗
        driver.click(self.info1(driver)*380, self.info2(driver)*930)  # 确定
        sleep(2)
        driver.click(120, 30)  # 小米mix2设置
        sleep(1)
        driver.click(self.info1(driver)*50, self.info2(driver)*39)  # 设置
        sleep(1)
        driver.click(self.info1(driver)*1366, self.info2(driver)*863)  # 退出战斗
        sleep(1)
        driver.click(self.info1(driver)*810, self.info2(driver)*650)  # 确定退出战斗
        sleep(5)
        '''商城'''
        self.images_or_none(driver, 'guide_004@auto.png')  # 等待商城
        sleep(1)
        driver.long_click(self.info1(driver)*1814, self.info2(driver)*969)  # 点击商城
        sleep(1)
        driver.click(self.info1(driver)*900, self.info2(driver)*500)  # 关闭弹出框
        sleep(1)
        driver.click(self.info1(driver)*669, self.info2(driver)*1024)  # 超级装备
        sleep(1)
        driver.click(self.info1(driver)*1160, self.info2(driver)*738)  # 购买一次
        sleep(5)
        driver.click(self.info1(driver)*900, self.info2(driver)*500)  # 任意键
        sleep(1)
        driver.click(self.info1(driver)*1180, self.info2(driver)*925)  # 确定
        sleep(1)
        driver.click(self.info1(driver)*1180, self.info2(driver)*925)  # 关闭弹出框
        '''装备'''
        sleep(1)
        driver.long_click(2020,30)  # 小米mix2返回
        sleep(1)
        driver.long_click(self.info1(driver)*1869, self.info2(driver)*45)  # 返回
        # driver.long_click(1243,30)
        sleep(1)
        driver.click(self.info1(driver)*1190, self.info2(driver)*418)  # 装备
        sleep(1)
        driver.click(self.info1(driver)*380, self.info2(driver)*400)  # 主武器
        sleep(1)
        driver.click(self.info1(driver)*315, self.info2(driver)*850)  # 装备
        sleep(1)
        '''主页'''
        driver.click(self.info1(driver)*520, self.info2(driver)*1010)  # 主页
        sleep(1)
        driver.click(self.info1(driver)*1180, self.info2(driver)*925)  # 关闭弹出框
        sleep(1)
        '''生存'''
        driver.click(self.info1(driver)*1600, self.info2(driver)*230)  # 生存
        log.info('游戏引导完成')
        # else:
        #     log.info('没有游戏引导')
        if self.wait_gone_images(driver, 'guide_004@auto.png'):
            log.info('引导成功')
            return 'ok'
        else:
            log.info('引导失败')
            return None
            
    def game_pay_pre(self, driver):  # 调起游戏充值界面
        if self.images_or_none(driver, 'game_pay_pre01@auto.png'):
            self.click_images(driver, 'game_pay_pre01@auto.png')
        sleep(2)
        if self.images_or_none(driver, 'exists_03@auto.png'):
            return 'ok'
        else:
            return None 

    def game_pay1(self, driver):  # 调起6元档位
        self.click_images(driver, "game_pay01@auto.png")
        sleep(1)
        if self.wait_gone_images(driver, 'game_pay01@auto.png'):
            return 'ok'
        else:
            return None

    def game_back_homePage(self, driver):
        if self.images_or_none(driver, 'game_pay_show@auto.png'):
            self.click_images(driver, 'game_home_page@auto.png')
        if self.wait_gone_images(driver, 'game_pay_show@auto.png'):
            return 'ok'
        else:
            return None


    def basicFunction(self,driver):
        '''逐步遍历基本功能'''
        driver.click(200,335)  # 推荐
        sleep(2)
        driver.click(1579,120)  # 关闭
        sleep(2)
        driver.click(200,800)  # 邮件
        sleep(2)
        driver.long_click(1860,36)  # 返回
        sleep(2)
        driver.click(1200,250)  # 角色
        sleep(2)
        driver.long_click(1860,36)  # 返回
        sleep(2)
        driver.click(1200,450)  # 装备
        sleep(2)
        driver.long_click(1860,36)  # 返回
        sleep(2)
        driver.click(1200,650)  # 任务
        sleep(2)
        driver.long_click(1860,36)  # 返回
        sleep(2)
        driver.click(1600,250)  # 机甲
        sleep(2)
        driver.click(720,880)  # 暂不教学
        sleep(2)
        driver.click(1560,450)  # 天赋
        sleep(2)
        driver.click(1560,660)  # 排行
        sleep(2)
        driver.long_click(1860,36)  # 返回
        sleep(2)
        driver.click(789,1020)  # 战斗
        sleep(2)
        driver.click(1060,1015)  # 创造
        sleep(2)
        driver.click(1723,92)  # 返回
        sleep(2)
        driver.click(1300,1020)  # 强化
        sleep(2)
        driver.click(1560,1020)  # 社交
        sleep(2)
        driver.click(530,1020)  # 主页
        sleep(2)
        if self.images_or_none(driver, 'basic_03@auto.png'):
            return 'ok'
        else:
            return None
    
    '''枪战直播'''   
    def live(self,driver):
        driver.click(200,650)  # 直播
        sleep(6)
        driver.click(130,785)  # 直播间
        sleep(2)
        driver.long_click(1860,60)  # 关闭
        sleep(2)
        if self.images_or_none(driver, 'basic_07@auto.png'):
            return 'ok'
        else:
            return None
    
    '''枪战攻略'''   
    def gonglue(self,driver):
        sleep(1)
        driver.click(369,829)  # 攻略
        sleep(6)
        driver.click(90,330)  # 红人
        sleep(2)
        driver.click(90,580)  # 攻略
        sleep(2)
        driver.click(90,820)  # 个人
        sleep(2)
        driver.click(1696,1024)  # 关闭
        if self.images_or_none(driver, 'basic_11@auto.png'):
            return 'ok'
        else:
            return None
        
    
    '''枪战赛事'''    
    def saishi(self,driver):
        sleep(1)
        driver.click(520,829)  # 赛事
        sleep(6)
        driver.click(68,350)  # 英雄榜
        sleep(2)
        driver.click(68,580)  # 小队
        sleep(2)
        driver.click(68,829)  # 我的
        sleep(2)
        driver.click(1696,1024)  # 关闭
        if self.images_or_none(driver, 'basic_13@auto.png'):
            return 'ok'
        else:
            return None
       
    '''枪战领钻'''   
    def lingzuan(self,driver):
        # self.click_images(driver,"basic_15@auto.png")
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # #self.click_images(driver,"choujiang@auto.png")
        # #self.click_images(driver,"lingzuian_04@auto.png")
        # sleep(2)
        # driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=0).click()
        # #sleep(3)
        # #driver(className="android.widget.LinearLayout",resourceId="com.tencent.mm:id/hf").click()
        # self.click_images(driver,"lingzuan_02@auto.png")
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # #self.click_images(driver,"choujiang@auto.png")
        # #self.click_images(driver,"lingzuian_05@auto.png")
        # sleep(2)
        # driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=1).click()
        # self.click_images(driver,"lingzuan_02@auto.png")
        # #sleep(2)
        # #driver(className="android.widget.LinearLayout",resourceId="com.tencent.mm:id/hf").click()
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # #self.click_images(driver,"choujiang@auto.png")
        # #self.click_images(driver,"lingzuian_06@auto.png")
        # sleep(2)
        # driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=2).click()
        # sleep(2)
        # driver.press.back()
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # self.click_images(driver,"lingzuan_01@auto.png")
        # #sleep(2)
        # #driver(className="android.widget.GridViewt",index=0).child(className="android.widget.LinearLayout",index=3).click()
        # sleep(3)
        # driver.press.back()
        # sleep(2)
        # driver(className="android.view.View",description='每日成功分享（0/1）').click()
        # #self.click_images(driver,"choujiang@auto.png")
        # #self.click_images(driver,"lingzuian_07@auto.png")
        # sleep(2)
        # driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=4).click()
        # sleep(2)
        # driver.press.back()
        # driver.press.back()
        # sleep(1)
        # driver(className="android.widget.TextView",text="不保存").click()
        # driver(className="android.widget.ImageView", resourceId="com.crisisfire.android.nearme.gamecenter:id/uc_sdk_webviewtool_close_deufalt").click()
        # self.click_images(driver,"lingzuan_03@auto.png")
        # #self.click_images(driver,"basic_16@auto.png")
        sleep(1)
        driver.click(669,829)  # 领钻
        sleep(6)
        driver.click(1136,565)  # 立即抽奖
        sleep(2)
        driver.click(960,1000)  # 取消
        sleep(2)
        driver.click(1689,1020)  # 关闭
        sleep(2)
        if self.images_or_none(driver,'basic_15@auto.png'):
            return 'ok'
        else:
            return None
    
    def store(self,driver):
        # self.click_images(driver,"basic_17@auto.png")
        # sleep(5)
        # driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=1).click()
        # sleep(2)
        # driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=2).click()
        # sleep(2)
        # driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=3).click()
        # sleep(2)
        # driver(className="android.widget.ImageView", resourceId="com.crisisfire.android.nearme.gamecenter:id/uc_sdk_webviewtool_close_deufalt").click()
        # self.click_images(driver,"basic_18@auto.png")
        sleep(1)
        driver.click(800,836)  # 神秘商店
        sleep(6)
        driver.click(80,350)  # 推荐
        sleep(2)
        driver.click(80,590)  # 积分商城
        sleep(2)
        driver.click(80,850)  # 订单
        sleep(2)
        driver.click(1690,1020)  # 关闭
        sleep(2)
        if self.images_or_none(driver, 'basic_15@auto.png'):
            return 'ok'
        else:
            return None
        

    def talking(self,driver):
        # self.click_images(driver,"talking_01@auto.png")
        # self.click_images(driver,"talking_02@auto.png")
        sleep(1)
        driver.click(50,1015)  # 谈话
        sleep(2)
        driver.click(950,929)  # 点击对话框
        sleep(2)
        # driver(className='android.widget.EditText',index=0).click()
        driver.type("毛泽东法轮功江泽民")
        sleep(2)
        driver(className='android.widget.Button',index=1).click()
        sleep(2)
        driver.click(1600,929)  # 发送
        sleep(2)
        driver.click(1685,185)  # 关闭
        # self.click_images(driver,"talking_03@auto.png")
        # self.click_images(driver,"talking_04@auto.png")
        if self.wait_gone_images(driver, 'talking_exist@auto.png'):
            return 'ok'
        else:
            return None
        
    def setting(self,driver):
        # self.click_images(driver,"setting@auto.png")
        if self.images_or_none(driver,'setting@auto.png'):
            self.click_images(driver, "setting@auto.png") # 设置
        # driver.long_click(1250,27)
        if self.wait_gone_images(driver, 'exists_01@auto.png'):
            log.info('进入设置界面')
            return 'ok'
        else:
            return None
        
    def exitGame(self,driver):
        if self.images_or_none(driver,'exit_game@auto.png'):
            self.click_images(driver,'exit_game@auto.png')  # 退出游戏
        return 'ok'
        
        
        
        
        
    
        
        


