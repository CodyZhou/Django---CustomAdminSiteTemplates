#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 3/10/2017 10:48 AM
# @Author  : Cody Zhou
# @File    : links.py
# @Software: PyCharm
# @Description:
#   Used to save the special links for admin site.
#   

from django.utils.html import format_html


class AdminSpecialLinks(object):

    @property
    def edit_link(self):
        # print('-------------> edit_link --------->')
        # print(format_html('<img src="/static/admin/img/icon-changelink.svg" />'
        #                               '<span style="color: red;">Edit</span>'))
        return format_html('<img src="/static/admin/img/icon-changelink.svg" />'
                                      '<span style="color: red;">Edit</span>')

