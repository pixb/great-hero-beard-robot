# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 4:23
# @Author  : pixb
# @Email   : tpxsky@163.com
# @File    : main_controller.py.py
# @Software: PyCharm
# @Description:
import sys
import time

import keyboard

from model.main_model import main_model
from view.main_view import main_view


class main_controller(object):

    def __init__(self):
        self._view = main_view()
        self._model = main_model()
        self._game_count = 0
        self._looping = True

    def run(self):
        print("main_controller, run...")
        keyboard.add_hotkey("ctrl+q", self.system_exit)
        self._game_count = 0
        while self._looping:
            self._view.click_enter()
            time.sleep(2)
            self._view.select_level()
            time.sleep(2)
            self._view.click_add_speed()
            time.sleep(60)
            self._view.click_back()
            self._view.click_sale()
            time.sleep(2)
            self._game_count += 1

    def system_exit(self):
        self._looping = False
        print("============退出==============")
        print("共进行了\t{}\t场游戏".format(self._game_count))
        sys.exit(0)
