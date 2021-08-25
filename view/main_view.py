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
        click.left_click(int(WINDOW_WIDTH_PX / 31), int(WINDOW_HEIGHT_PX / 1.05))

    def click_add_speed(self):
        click.left_click(int(WINDOW_WIDTH_PX / 1.14), WINDOW_HEIGHT_PX / 10)
        time.sleep(1)

    def click_back(self):
        click.left_click(WINDOW_WIDTH_PX / 31, WINDOW_HEIGHT_PX / 20)
        time.sleep(1)

    def click_sale(self):
        click.left_click(int(WINDOW_WIDTH_PX / 1.03), int(WINDOW_HEIGHT_PX / 1.7))
        time.sleep(1)

