# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 4:25
# @Author  : pixb
# @Email   : tpxsky@163.com
# @File    : main_view.py.py
# @Software: PyCharm
# @Description:
import time

from view import click
from constants.constants import *


class main_view(object):

    def click_enter(self):
        click.left_click(int(WINDOW_WIDTH_PX / 10), int(WINDOW_HEIGHT_PX / 3))

    def select_level(self):
        # click.left_click(int(WINDOW_WIDTH_PX / 31), int(WINDOW_HEIGHT_PX / 1.05))
        click.left_click(int(WINDOW_WIDTH_PX / 31), int(WINDOW_HEIGHT_PX / 1.75))

    def click_add_speed(self):
        click.left_click(int(WINDOW_WIDTH_PX / 1.14), WINDOW_HEIGHT_PX / 10)

    def click_back(self):
        click.left_click(WINDOW_WIDTH_PX / 31, WINDOW_HEIGHT_PX / 20)

    def click_sale(self):
        click.left_click(int(WINDOW_WIDTH_PX / 1.04), int(WINDOW_HEIGHT_PX / 1.65))

    def double_click(self):
        click.left_click(int(600), int(500))
        time.sleep(0.2)
        click.left_click(int(1100), int(500))

