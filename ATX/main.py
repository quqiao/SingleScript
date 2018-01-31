# coding=utf-8

import os
import unittest
import atx
from time import sleep, strftime
import configure
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)
class Test(unittest.TestCase,public.Methods):

    def setUp(self):
        if configure.device_name == '':
            self.driver = atx.connect()
        else:
            self.driver = atx.connect(configure.device_name)
        # self.driver.start_app(configure.package_name,configure.activity_name)  # 如果设备未连接，默认启动
        log.info('测试开始')


    def get_names(self,name):
        '''
                    动态import 游戏和渠道相应的测试类
        :param name: 动态import 游戏还是 渠道
        :return: 返回 游戏 或者 渠道 实例 的类
        '''
        import public.get_names as get_names
        get_names = get_names.Get_name()
        if name =='game':
            game = __import__(get_names.get_game())
            game_name = get_names.get_game().split('.')[1]
            game = getattr(game, game_name)
            game = game.Game()
            return game
        if name == 'channel':
            channel = __import__(get_names.get_channel())
            channel_name = get_names.get_channel().split('.')[1]
            channel = getattr(channel, channel_name)
            channel = channel.Channel()
            return channel

    def tearDown(self):
        pass
        # self.driver.stop_app(configure.package_name)
        log.info('测试结束')


    def test(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        # self.dy_IsNotNone(self.driver, game.game_update(self.driver), 'game_update')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'login')
        # self.dy_IsNotNone(self.driver, game.game_pre(self.driver), 'game_pre')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'guide')

    # 渠道360
    '''
    def test_360(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), '360_guide')
        # 新账号登录
        # self.dy_IsNotNone(self.driver,game.game_update(self.driver),'360_game_update')
        # self.dy_IsNotNone(self.driver,channel.login(self.driver), '360_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'360_game_pre')
        # self.dy_IsNotNone(self.driver,game.guide(self.driver),'360_guide')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'360_fubiao')
        # 老账号登录
        # self.dy_IsNotNone(self.driver, game.enter_game(self.driver), '360_game_pre')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), '360_login')
        # self.dy_IsNotNone(self.driver, channel.fubiao(self.driver), '360_fubiao')
        #支付宝支付跳转
        # self.dy_IsNotNone(self.driver,game.game_pay_pre(self.driver),'360_pay')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), '360_game_pay1')
        # self.dy_IsNotNone(self.driver, channel.ali(self.driver), '360_pay_ali')
        # #微信支付跳转
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), '360_game_pay1')
        # self.dy_IsNotNone(self.driver, channel.wechat(self.driver), '360_pay_wechat')
        # self.dy_IsNotNone(self.driver, game.game_back_homePage(self.driver), '360_gamePay_backHomePage')
        # #游戏基本功能模块
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'360_basicFunction')
        # self.dy_IsNotNone(self.driver,game.live(self.driver),'360_live')
        # self.dy_IsNotNone(self.driver,game.gonglue(self.driver),'360_gonglue')
        # self.dy_IsNotNone(self.driver,game.saishi(self.driver),'360_saishi')
        # self.dy_IsNotNone(self.driver,game.lingzuan(self.driver),'360_lingzuan')
        # self.dy_IsNotNone(self.driver,game.store(self.driver),'360_store')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'360_talking')
        # self.dy_IsNotNone(self.driver,game.setting(self.driver),'360_setting')
        # #360渠道退出框
        # self.dy_IsNotNone(self.driver,game.exitGame(self.driver),'360_exitgame')
        # self.dy_IsNotNone(self.driver,channel.exitSDK_activityInfo(self.driver),'360_exitGame')
        # self.dy_IsNotNone(self.driver, game.exitGame(self.driver), '360_exitgame')
        # self.dy_IsNotNone(self.driver, channel.exitSDK_exitGame(self.driver), '360_exitGame')
        '''

    # 渠道百度
    '''
    def test_baiDu(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        # 新账号登录
        # self.dy_IsNotNone(self.driver, game.game_update(self.driver), 'baidu_game_update')  # 游戏第一登录更新
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'baidu_login')
        # self.dy_IsNotNone(self.driver, game.game_pre(self.driver), 'baidu_game_pre')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'baidu_guide')
        # 二次登录（老账号）
        # self.dy_IsNotNone(self.driver, game.enter_game(self.driver), 'baidu_game_pre')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'baidu_login')
        # 支付
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'baidu_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'baidu_game_pay1')
        # self.dy_IsNotNone(self.driver, channel.ali(self.driver), 'baidu_ali')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'baidu_game_pay1')
        # self.dy_IsNotNone(self.driver, channel.wechat(self.driver), 'baidu_wechat')
        # self.dy_IsNotNone(self.driver, game.game_back_homePage(self.driver), 'baidu_gamePay_backHomePage')
        # 基本功能
        # self.dy_IsNotNone(self.driver, game.basicFunction(self.driver), 'baidu_basicFunction')
        # self.dy_IsNotNone(self.driver, game.live(self.driver), 'baidu_live')
        # self.dy_IsNotNone(self.driver, game.gonglue(self.driver), 'baidu_gonglue')
        # self.dy_IsNotNone(self.driver, game.saishi(self.driver), 'baidu_saishi')
        # self.dy_IsNotNone(self.driver, game.lingzuan(self.driver), 'baidu_lingzuan')
        # self.dy_IsNotNone(self.driver, game.store(self.driver), 'baidu_store')
        # self.dy_IsNotNone(self.driver, channel.fubiao(self.driver), 'baidu_fubiao')
        # self.dy_IsNotNone(self.driver, game.talking(self.driver), 'baidu_talking')
        # self.dy_IsNotNone(self.driver, game.setting(self.driver), 'baidu_setting')
        # self.dy_IsNotNone(self.driver, game.exitGame(self.driver), 'baidu_exitgame')
        # self.dy_IsNotNone(self.driver, channel.exit_HotGame(self.driver), 'baidu_exitgame')
        # self.dy_IsNotNone(self.driver, game.exitGame(self.driver), 'baidu_exitgame')
        # self.dy_IsNotNone(self.driver, channel.exitGame(self.driver), 'baidu_exitgame')
    '''

    # 渠道UC
    '''
    def test_uc(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        # self.dy_IsNotNone(self.driver, game.game_update(self.driver),'UC_game_update')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'UC_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'UC_game_pre')
        # self.dy_IsNotNone(self.driver,game.guide(self.driver),'UC_guide')
        # 老账号登录
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'UC_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'UC_login')
        #UC_支付宝支付
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'UC_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'UC_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.QQ_Pay(self.driver),'UC_QQPay')
        # UC_微信支付
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'UC_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'UC_wechat')
        # self.dy_IsNotNone(self.driver, game.game_back_homePage(self.driver), 'UC_gamePay_backHomePage')
        #基本功能
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'UC_basicFunction')
        # self.dy_IsNotNone(self.driver,game.live(self.driver),'UC_live')
        # self.dy_IsNotNone(self.driver,game.gonglue(self.driver),'UC_gonglue')
        # self.dy_IsNotNone(self.driver,game.saishi(self.driver),'UC_saishi')
        # self.dy_IsNotNone(self.driver,game.lingzuan(self.driver),'UC_lingzuan')
        # self.dy_IsNotNone(self.driver,game.store(self.driver),'UC_store')
        # # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'UC_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'UC_talking')
        # self.dy_IsNotNone(self.driver,game.setting(self.driver),'UC_setting')
        # self.dy_IsNotNone(self.driver,game.exitGame(self.driver),'UC_game_exitGame')
        # self.dy_IsNotNone(self.driver,channel.exitGame(self.driver),'UC_exitGame')
        '''

    # 渠道豌豆荚
    '''
    def test_wdj(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'wanDouJia_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'wandoujia_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'wandoujia_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'wandoujia_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'wandoujia_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'wandoujia_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'wandoujia_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'wandoujia_wechat')
        '''

    # 渠道4399
    '''
    def test_4399(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), '4399_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'4399_enter_game1')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), '4399_login1')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'4399_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), '4399_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), '4399_game_pay')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'4399_ali')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), '4399_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'4399_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'4399_basicFunction')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'4399_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'4399_talking')
        # self.dy_IsNotNone(self.driver,channel.exitGame(self.driver),'4399_exitGame')
        '''

    # 渠道应用宝
    '''
    def test_yyb(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver,game.guide(self.driver),'qmqzhero_guide')
        # self.dy_IsNotNone(self.driver,game.game_update(self.driver),'yingyongbao_game_update')
        #self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'yingyongbao_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'yingyongbao_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'yingyongbao_game_pre')
        # self.dy_IsNotNone(self.driver,game.guide(self.driver),'yingyongbao_guide')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'yingyongbao_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'yingyongbao_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.QQ(self.driver),'yingyongbao_QQ')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'yingyongbao_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'yingyongbao_basicFunction')
        # self.dy_IsNotNone(self.driver,game.live(self.driver),'yingyongbao_live')
        # self.dy_IsNotNone(self.driver,game.gonglue(self.driver),'yingyongbao_gonglue')
        # self.dy_IsNotNone(self.driver,game.saishi(self.driver),'yingyongbao_saishi')
        # self.dy_IsNotNone(self.driver,game.lingzuan(self.driver),'yingyongbao_lingzuan')
        # self.dy_IsNotNone(self.driver,game.store(self.driver),'yingyongbao_store')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'yingyongbao_talking')
        # self.dy_IsNotNone(self.driver,game.setting(self.driver),'yingyongbao_setting')
        # self.dy_IsNotNone(self.driver,game.exitgame(self.driver),'yingyongbao_exitgame')
        '''

    # 渠道拇指玩
    '''
    def test_mzw(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'mzw_guide')
        # self.dy_IsNotNone(self.driver, game.enter_game(self.driver), 'muzhiwan_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'muzhiwan_login')
        # self.dy_IsNotNone(self.drsiver, game.game_pre(self.driver), 'muzhiwan_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'muzhiwan_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'muzhiwan_game_pay1')
        # self.dy_IsNotNone(self.driver, channel.ali(self.driver), 'muzhiwan_ali')
        # self.dy_IsNotNone(self.driver, channel.wechat(self.driver), 'muzhiwan_wechat')
        # self.dy_IsNotNone(self.driver, game.basicFunction(self.driver), 'muzhiwan_basicFunction')
        # self.dy_IsNotNone(self.driver, channel.fubiao(self.driver), 'muzhiwan_fubiao')
        # self.dy_IsNotNone(self.driver, game.talking(self.driver), 'muzhiwan_talking')
        # self.dy_IsNotNone(self.driver, channel.exitGame(self.driver), 'muzhiwan_exitGame')
        '''

    #渠道当乐
    '''
    def test_DL(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'DL_guide')
        #self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'dangle_enter_game1')
        #self.dy_IsNotNone(self.driver, channel.login(self.driver), 'dangle_login1')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'dangle_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'dangle_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'dangle_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'dangle_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'dangle_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'dangle_basicFunction')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'dangle_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'dangle_talking')
        # self.dy_IsNotNone(self.driver,game.setting_exitgame(self.driver),'dangle_exitGame')
        '''

    # 渠道应用汇
    '''
    def test_yyh(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'yyh_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'yingyonghui_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'yingyonghui_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'yingyonghui_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'yingyonghui_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'yingyonghui_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'yingyonghui_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'yingyonghui_wechat')
        '''

    # 渠道PPS
    '''
    def test_pps(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'pps_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'PPS_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'PPS_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'PPS_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'PPS_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'PPS_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'PPS_wechat')
        # self.dy_IsNotNone(self.driver, game.game_pay(self.driver), 'PPS_game_pay')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'PPS_ali')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'PPS_basicFunction')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'PPS_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'PPS_talking')
        # self.dy_IsNotNone(self.driver,channel.exitGame(self.driver),'PPS_exitGame')
        '''

    # 渠道安智
    '''
    def test_anZhi(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'anzhi_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'anzhi_enter_game1')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'anzhi_login1')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'anzhi_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'anzhi_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'anzhi_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'anzhi_wechat')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'anzhi_ali')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'anzhi_basicFunction')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'anzhi_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'anzhi_talking')
        # self.dy_IsNotNone(self.driver,channel.exitGame(self.driver),'anzhi_exitGame')
        '''

    # 渠道联通
    '''
    def test_woStore(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver),'wolt_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'LianTong_enter_game')
        # self.dy_IsNotNone(self.driver,channel.login(self.driver), 'LianTong_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'LianTong_game_pre')
        # self.dy_IsNotNone(self.driver,game.game_pay_pre(self.driver), 'LianTong_game_pay_pre')
        # self.dy_IsNotNone(self.driver,game.game_pay1(self.driver), 'LianTong_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'LianTong_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'LianTong_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'LianTong_basicFunction')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'LianTong_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'LianTong_talking')
        # self.dy_IsNotNone(self.driver,game.setting_exitgame(self.driver),'LianTong_exitGame')
        '''

    # 渠道新浪
    '''
    def test_sina(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'sina_wyx_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'sina_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'sina_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'sina_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'sina_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'sina_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'sina_ali')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'sina_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.chongzhika(self.driver),'sina_chongzhika')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'sina_basicFunction')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'sina_talking')
        # self.dy_IsNotNone(self.driver,channel.exitGame(self.driver),'sina_exitGame')
        '''

    # 渠道益玩
    '''
    def test_ewan(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'ewan_guide')
        # self.dy_IsNotNone(self.driver,channel.ewanUpdate(self.driver),'ewan_ewanUpdate')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'ewan_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'ewan_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'ewan_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'ewan_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'ewan_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'ewan_ali')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'ewan_basicFunction')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'ewan_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'ewan_talking')
        # self.dy_IsNotNone(self.driver,channel.exitGame(self.driver),'ewan_exitGame')
        '''

    # 渠道搜狗
    '''
    def test_souGou(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'sougou_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'sougou_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'sougou_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'sougou_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'sougou_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'sougou_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'sougou_ali')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'sougou_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'sougou_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'sougou_basicFunction')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'sougou_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'sougou_talking')
        # self.dy_IsNotNone(self.driver,channel.exitGame(self.driver),'sougou_exitGame')
        '''

    # 渠道电信
    '''
    def test_dianXin(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'egame_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'dianxin_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'dianxin_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'dianxin_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'dianxin_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'dianxin_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'dianxin_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'dianxin_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'dianxin_basicFunction')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'dianxin_talking')
        # self.dy_IsNotNone(self.driver,channel.exitGame(self.driver),'dianxin_exitGame')
        '''

    # 渠道果盘
    '''
    def test_guoPan(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'guopan_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'guopan_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'guopan_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'guopan_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'guopan_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'guopan_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'guopan_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'guopan_wechat')
        # self.dy_IsNotNone(self.driver,channel.guopan(self.driver),'guopan_guopan')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'guopan_basicFunction')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'guopan_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'guopan_talking')
        # self.dy_IsNotNone(self.driver,channel.exitGame(self.driver),'guopan_exitGame')
        '''

    # 渠道触手
    '''
    def test_chuShou(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver),'cstv_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'chushou_enter_game1')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'chushou_login1')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'chushou_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'chushou_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'chushou_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'chushou_ali')
        # self.dy_IsNotNone(self.driver,channel.phonePay(self.driver),'chushou_phonePay')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'chushou_basicFunction')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'chushou_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'chushou_talking')
        # self.dy_IsNotNone(self.driver,game.setting_exitgame(self.driver),'chushou_exitGame')
        '''

    # 渠道酷狗
    '''
    def test_kuGou(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'kugou_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'kugou_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'kugou_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'kugou_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'kugou_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'kugou_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'kugou_ali')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'kugou_basicFunction')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'kugou_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'kugou_talking')
        # self.dy_IsNotNone(self.driver,game.channel.exitGame(self.driver),'kugou_exitGame')
        '''

    #啪啪渠道
    '''
    def test_papa(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'papa_guide')
    '''

    #TT语音渠道
    '''
    def test_TT(self):
        game=self.get_names('game')
        channel=self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'TT_guide')
    '''

    # 朋友玩
    '''
    def test_pengYouWan(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'yq_guide')
    '''

    # 美图
    '''
    def test_meiTu(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'meitu_guide')
    '''

    # 渠道37wan
    """
    def test_37wan(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'sy37_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'37wan_enter_game1')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), '37wan_login1')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'37wan_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), '37wan_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), '37wan_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'37wan_ali')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), '37wan_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.wangshangyinhang(self.driver),'37wan_wangshangyinhang')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'37wan_basicFunction')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'37wan_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'37wan_talking')
        # self.dy_IsNotNone(self.driver,game.setting_exitgame(self.driver),'37wan_exitGame')
    """

    # 官网安卓
    # """
    # def test_guanFang(self):
    #     game = self.get_names('game')
    #     channel = self.get_names('channel')
    #     self.dy_IsNotNone(self.driver, game.guide(self.driver), 'cmge_guide')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'guanfang_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'guanfang_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'guanfang_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'guanfang_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'guanfang_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'guanfang_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'guanfang_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'guanfang_basicFunction')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'guanfang_talking')
        # self.dy_IsNotNone(self.driver,game.setting_exitgame(self.driver),'37wan_exitGame')
    # """

    '''小米'''
    '''
    def test23(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'mi_guide')
        # self.dy_IsNotNone(self.driver, game.game_update(self.driver),'xiaomi_game_update')
        #self.dy_IsNotNone(self.driver, game.enter_game(self.driver),'xiaomi_enter_game')
        # self.dy_IsNotNone(self.driver,channel.login(self.driver), 'xiaomi_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'xiaomi_game_pre')
        # self.dy_IsNotNone(self.driver,game.guide(self.driver),'xiaomi_guide')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'xiaomi_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'xiaomi_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'xiaomi_ali')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'xiaomi_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'xiaomi_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'xiaomi_basicFunction')
        # self.dy_IsNotNone(self.driver,game.live(self.driver),'xiaomi_live')
        # self.dy_IsNotNone(self.driver,game.gonglue(self.driver),'xiaomi_gonglue')
        # self.dy_IsNotNone(self.driver,game.saishi(self.driver),'xiaomi_saishi')
        # self.dy_IsNotNone(self.driver,game.lingzuan(self.driver),'xiaomi_lingzuan')
        # self.dy_IsNotNone(self.driver,game.store(self.driver),'xiaomi_store')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'xiaomi_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'xiaomi_talking')
        # self.dy_IsNotNone(self.driver,game.setting(self.driver),'xiaomi_setting')
        # self.dy_IsNotNone(self.driver,game.exitgame(self.driver),'xiaomi_exitgame')
        # self.dy_IsNotNone(self.driver,channel.Exitgame(self.driver),'xiaomi_exitgame')
        '''

    '''华为'''
    '''
    def test_huaWei(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'huaWei_guide')
        # self.dy_IsNotNone(self.driver, game.game_update(self.driver),'huawei_game_update')
        # #self.dy_IsNotNone(self.driver, game.enter_game(self.driver),'huawei_enter_game')
        # self.dy_IsNotNone(self.driver,channel.login(self.driver), 'huawei_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'huawei_game_pre')
        # self.dy_IsNotNone(self.driver,game.guide(self.driver),'huawei_guide')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'huawei_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'huawei_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'huawei_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'huawei_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'huawei_basicFunction')
        # self.dy_IsNotNone(self.driver,game.live(self.driver),'huawei_live')
        # self.dy_IsNotNone(self.driver,game.gonglue(self.driver),'huawei_gonglue')
        # self.dy_IsNotNone(self.driver,game.saishi(self.driver),'huawei_saishi')
        # self.dy_IsNotNone(self.driver,game.lingzuan(self.driver),'huawei_lingzuan')
        # self.dy_IsNotNone(self.driver,game.store(self.driver),'huawei_store')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'huawei_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'huawei_talking')
        # self.dy_IsNotNone(self.driver,game.setting(self.driver),'huawei_setting')
        # self.dy_IsNotNone(self.driver,game.exitgame(self.driver),'huawei_exitgame')
    '''

    '''vivo'''
    '''
    def test_vivo(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver),'vivo_guide')
        # self.dy_IsNotNone(self.driver, game.game_update(self.driver),'vivo_game_update')
        # #self.dy_IsNotNone(self.driver, game.enter_game(self.driver),'vivo_enter_game')
        # self.dy_IsNotNone(self.driver,channel.login(self.driver), 'vivo_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'vivo_game_pre')
        # self.dy_IsNotNone(self.driver,game.guide(self.driver),'vivo_guide')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'vivo_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'vivo_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'vivo_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'vivo_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'vivo_basicFunction')
        # self.dy_IsNotNone(self.driver,game.live(self.driver),'vivo_live')
        # self.dy_IsNotNone(self.driver,game.gonglue(self.driver),'vivo_gonglue')
        # self.dy_IsNotNone(self.driver,game.saishi(self.driver),'vivo_saishi')
        # self.dy_IsNotNone(self.driver,game.lingzuan(self.driver),'vivo_lingzuan')
        # self.dy_IsNotNone(self.driver,game.store(self.driver),'vivo_store')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'vivo_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'vivo_talking')
        # self.dy_IsNotNone(self.driver,game.setting(self.driver),'vivo_setting')
        # self.dy_IsNotNone(self.driver,game.exitgame(self.driver),'vivo_exitgame')
        # self.dy_IsNotNone(self.driver,channel.exitGame(self.driver),'vivo_exitGame')
    '''

    '''三星手机'''
    '''
    def test_samSung(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'samSung_guide')
        # self.dy_IsNotNone(self.driver, game.game_update(self.driver),'Samsung_game_update')
        # self.dy_IsNotNone(self.driver, game.enter_game(self.driver),'Samsung_enter_game')
        # self.dy_IsNotNone(self.driver,channel.login(self.driver), 'Samsung_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'Samsung_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'Samsung_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'Samsung_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'Samsung_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'Samsung_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'Samsung_basicFunction')
        # self.dy_IsNotNone(self.driver,game.live(self.driver),'Samsung_live')
        # self.dy_IsNotNone(self.driver,game.gonglue(self.driver),'Samsung_gonglue')
        # self.dy_IsNotNone(self.driver,game.saishi(self.driver),'Samsung_saishi')
        # self.dy_IsNotNone(self.driver,channel.lingzuan(self.driver),'Samsung_lingzuan')
        # self.dy_IsNotNone(self.driver,game.store(self.driver),'Samsung_store')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'Samsung_talking')
        # self.dy_IsNotNone(self.driver,game.setting(self.driver),'Samsung_setting')
        # self.dy_IsNotNone(self.driver,game.exitgame(self.driver),'Samsung_exitgame')
    '''

    '''oppo手机'''
    '''
    def test_oppo(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'nearme_guide')
        # self.dy_IsNotNone(self.driver, game.game_update(self.driver),'oppo_game_update')
        # #self.dy_IsNotNone(self.driver, game.enter_game(self.driver),'oppo_enter_game')
        # self.dy_IsNotNone(self.driver,channel.login(self.driver), 'oppo_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'oppo_game_pre')
        # self.dy_IsNotNone(self.driver,game.guide(self.driver),'xiaomi_guide')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'oppo_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'oppo_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'oppo_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'oppo_wechat')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'oppo_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.fanhui(self.driver),'oppo_fanhui')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'oppo_basicFunction')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'oppo_fubiao')
        # self.dy_IsNotNone(self.driver,game.live(self.driver),'oppo_live')
        # self.dy_IsNotNone(self.driver,game.gonglue(self.driver),'oppo_gonglue')
        # self.dy_IsNotNone(self.driver,game.saishi(self.driver),'oppo_saishi')
        # self.dy_IsNotNone(self.driver,game.lingzuan(self.driver),'oppo_lingzuan')
        # self.dy_IsNotNone(self.driver,game.store(self.driver),'oppo_store')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'oppo_talking')
        # self.dy_IsNotNone(self.driver,game.setting(self.driver),'oppo_setting')
        # self.dy_IsNotNone(self.driver,game.exitgame(self.driver),'oppo_exitgame')
    '''

    '''魅族手机'''
    '''
    def test_mz(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'mz_guide')
        # self.dy_IsNotNone(self.driver, game.game_update(self.driver),'meizu_game_update')
        # #self.dy_IsNotNone(self.driver, game.enter_game(self.driver),'meizu_enter_game')
        # self.dy_IsNotNone(self.driver,channel.login(self.driver), 'meizu_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'meizu_game_pre')
        # self.dy_IsNotNone(self.driver,game.guide(self.driver),'meizu_guide')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'meizu_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'meizu_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'meizu_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'meizu_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'meizu_basicFunction')
        # self.dy_IsNotNone(self.driver,game.live(self.driver),'meizu_live')
        # self.dy_IsNotNone(self.driver,game.gonglue(self.driver),'meizu_gonglue')
        # self.dy_IsNotNone(self.driver,game.saishi(self.driver),'meizu_saishi')
        # self.dy_IsNotNone(self.driver,game.lingzuan(self.driver),'meizu_lingzuan')
        # self.dy_IsNotNone(self.driver,game.store(self.driver),'meizu_store')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'meizu_talking')
        # self.dy_IsNotNone(self.driver,game.setting(self.driver),'meizu_setting')
        # self.dy_IsNotNone(self.driver,game.exitgame(self.driver),'meizu_exitgame')
    '''

    '''联想手机'''
    '''
    def test_lenovo(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'lenovo_guide')
        # self.dy_IsNotNone(self.driver, game.game_update(self.driver),'Lenovo_game_update')
        # #self.dy_IsNotNone(self.driver, game.enter_game(self.driver),'Lenovo_enter_game')
        # self.dy_IsNotNone(self.driver,channel.login(self.driver), 'Lenovo_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'Lenovo_game_pre')
        # self.dy_IsNotNone(self.driver,game.guide(self.driver),'Lenovo_guide')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'Lenovo_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'Lenovo_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'Lenovo_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'Lenovo_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'Lenovo_basicFunction')
        # self.dy_IsNotNone(self.driver,game.live(self.driver),'Lenovo_live')
        # self.dy_IsNotNone(self.driver,game.gonglue(self.driver),'Lenovo_gonglue')
        # self.dy_IsNotNone(self.driver,game.saishi(self.driver),'Lenovo_saishi')
        # self.dy_IsNotNone(self.driver,game.lingzuan(self.driver),'Lenovo_lingzuan')
        # self.dy_IsNotNone(self.driver,game.store(self.driver),'Lenovo_store')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'Lenovo_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'Lenovo_talking')
        # self.dy_IsNotNone(self.driver,game.setting_exitgame(self.driver),'Lenovo_exitGame')
        # self.dy_IsNotNone(self.driver,channel.setting_exitgame(self.driver),'Lenovo_exitGame')
    '''

    '''金立手机'''
    '''
    def test_Gionee(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver),'am_guide')
        # self.dy_IsNotNone(self.driver, game.game_update(self.driver),'Gionee_game_update')
        # #self.dy_IsNotNone(self.driver, game.enter_game(self.driver),'Gionee_enter_game')
        # self.dy_IsNotNone(self.driver,channel.login(self.driver), 'Gionee_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'Gionee_game_pre')
        # self.dy_IsNotNone(self.driver,game.guide(self.driver),'Gionee_guide')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'Gionee_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'Gionee_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'Gionee_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'Gionee_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'Gionee_basicFunction')
        # self.dy_IsNotNone(self.driver,game.live(self.driver),'Gionee_live')
        # self.dy_IsNotNone(self.driver,game.gonglue(self.driver),'Gionee_gonglue')
        # self.dy_IsNotNone(self.driver,game.saishi(self.driver),'Gionee_saishi')
        # self.dy_IsNotNone(self.driver,game.lingzuan(self.driver),'Gionee_lingzuan')
        # self.dy_IsNotNone(self.driver,game.store(self.driver),'Gionee_store')
        # self.dy_IsNotNone(self.driver,channel.fubiao(self.driver),'Gionee_fubiao')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'Gionee_talking')
        # self.dy_IsNotNone(self.driver,game.setting(self.driver),'Gionee_setting')
        # self.dy_IsNotNone(self.driver,game.exitgame(self.driver),'Gionee_exitgame')
        # self.dy_IsNotNone(self.driver,channel.exitGame(self.driver),'Gionee_exitGame')
    '''

    '''乐视'''
    '''
    def test_leShi(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'leShi_guide')
    '''

    '''酷派手机'''
    '''
    def test_coolpad(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'kp_guide')
        # self.dy_IsNotNone(self.driver,game.game_update(self.driver),'coolpad_game_update')
        # #self.dy_IsNotNone(self.driver, game.enter_game(self.driver),'coolpad_enter_game')
        # self.dy_IsNotNone(self.driver,channel.login(self.driver), 'coolpad_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'coolpad_game_pre')
        # self.dy_IsNotNone(self.driver,game.guide(self.driver),'xiaomi_guide')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'coolpad_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'coolpad_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'coolpad_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'coolpad_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'coolpad_basicFunction')
        # self.dy_IsNotNone(self.driver,game.live(self.driver),'coolpad_live')
        # self.dy_IsNotNone(self.driver,game.gonglue(self.driver),'coolpad_gonglue')
        # self.dy_IsNotNone(self.driver,game.saishi(self.driver),'coolpad_saishi')
        # self.dy_IsNotNone(self.driver,game.lingzuan(self.driver),'coolpad_lingzuan')
        # self.dy_IsNotNone(self.driver,game.store(self.driver),'coolpad_store')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'coolpad_talking')
        # self.dy_IsNotNone(self.driver,channel.restart(self.driver),'coolpad_restart')
        # self.dy_IsNotNone(self.driver,game.setting(self.driver),'coolpad_setting')
        # self.dy_IsNotNone(self.driver,game.exitgame(self.driver),'coolpad_exitgame')
    '''

    '''HTC手机'''
    '''
    def test_HTC(self):
        game = self.get_names('game')
        channel = self.get_names('channel')
        self.dy_IsNotNone(self.driver, game.guide(self.driver), 'htc_guide')
        # self.dy_IsNotNone(self.driver,game.game_update(self.driver),'HTC_game_update')
        # self.dy_IsNotNone(self.driver,game.enter_game(self.driver),'HTC_enter_game')
        # self.dy_IsNotNone(self.driver, channel.login(self.driver), 'HTC_login')
        # self.dy_IsNotNone(self.driver,game.game_pre(self.driver),'HTC_game_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay_pre(self.driver), 'HTC_game_pay_pre')
        # self.dy_IsNotNone(self.driver, game.game_pay1(self.driver), 'HTC_game_pay1')
        # self.dy_IsNotNone(self.driver,channel.ali(self.driver),'HTC_ali')
        # self.dy_IsNotNone(self.driver,channel.wechat(self.driver),'HTC_wechat')
        # self.dy_IsNotNone(self.driver,game.basicFunction(self.driver),'HTC_basicFunction')
        # self.dy_IsNotNone(self.driver,game.live(self.driver),'HTC_live')
        # self.dy_IsNotNone(self.driver,game.gonglue(self.driver),'HTC_gonglue')
        # self.dy_IsNotNone(self.driver,game.saishi(self.driver),'HTC_saishi')
        # self.dy_IsNotNone(self.driver,game.lingzuan(self.driver),'HTC_lingzuan')
        # self.dy_IsNotNone(self.driver,game.store(self.driver),'HTC_store')
        # self.dy_IsNotNone(self.driver,game.talking(self.driver),'HTC_talking')
        # self.dy_IsNotNone(self.driver,game.setting(self.driver),'HTC_setting')
        # self.dy_IsNotNone(self.driver,game.exitgame(self.driver),'HTC_exitgame')
    '''

if __name__ == '__main__':
    unittest.main()

