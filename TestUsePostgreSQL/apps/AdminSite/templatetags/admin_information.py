#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 3/24/2017 4:16 PM
# @Author  : Cody Zhou
# @File    : admin_information.py
# @Software: PyCharm
# @Description:
#   
#   
from django.template import Library
from django.utils.html import format_html

register = Library()


@register.simple_tag
def get_admin_site_main_title():
    return format_html('<span class="glyphicon glyphicon-tree-deciduous green"></span>'
                       ' <span class="orange">Admin</span> Management System')


@register.simple_tag
def get_admin_site_copyright():
    return format_html('<div class="copyright">'
                       '    <span class="orange">&copy;2017 All Rights Reserved.</span>'
                       '</div>')