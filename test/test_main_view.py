# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 8:15
# @Author  : pixb
# @Email   : tpxsky@163.com
# @File    : test_main_view.py
# @Software: PyCharm
# @Description:
from view.main_view import main_view


def test_main_back():
    main_view().click_back()

def test_click_enter():
    main_view().click_enter()

def test_add_speed():
    main_view().click_add_speed()


def test_select_level():
    main_view().select_level()

def test_click_sale():
    main_view().click_sale()
