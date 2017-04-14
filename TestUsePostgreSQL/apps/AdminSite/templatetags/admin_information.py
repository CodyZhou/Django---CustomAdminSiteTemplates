#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 3/24/2017 4:16 PM
# @Author  : Cody Zhou
# @File    : admin_information.py
# @Software: PyCharm
# @Description:
#   
#
from django.contrib import admin

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


# The app_list structure!

# [
# 	{
# 		'has_module_perms': True,
# 		'app_url': '/admin/auth/',
# 		'name': <django.utils.functional.lazy.<locals>.__proxy__ object at 0x0000000004C30E80>,
# 		'models': [
# 							{
# 								'perms': {'change': True, 'add': True, 'delete': True},
# 								'name': <django.utils.functional.lazy.<locals>.__proxy__ object at 0x000000000588F518>,
# 								'add_url': '/admin/auth/group/add/',
# 								'object_name': 'Group',
# 								'admin_url': '/admin/auth/group/'
# 							},
# 							{
# 								'perms': {'change': True, 'add': True, 'delete': True},
# 								'name': <django.utils.functional.lazy.<locals>.__proxy__ object at 0x000000000588FCC0>,
# 								'add_url': '/admin/auth/user/add/',
# 								'object_name': 'User',
# 								'admin_url': '/admin/auth/user/'
# 							}
# 					],
# 		'app_label': 'auth'
# 	},
# 	{
# 		'has_module_perms': True,
# 		'app_url': '/admin/Author/',
# 		'name': 'Author',
# 		'models': [
# 							{
# 								'perms': {'change': True, 'add': True, 'delete': True},
# 								'name': 'Author',
# 								'add_url': '/admin/Author/author/add/',
# 								'object_name': 'Author',
# 								'admin_url': '/admin/Author/author/'
# 							},
# 							{
# 								'perms': {'change': True, 'add': True, 'delete': True},
# 								'name': 'Author Address',
# 								'add_url': '/admin/Author/authoraddress/add/',
# 								'object_name': 'AuthorAddress',
# 								'admin_url': '/admin/Author/authoraddress/'
# 							}
# 					],
# 		'app_label': 'Author'
# 	},
# 	{
# 		'has_module_perms': True,
# 		'app_url': '/admin/Book/',
# 		'name': 'Book',
# 		'models': [
# 							{
# 								'perms': {'change': True, 'add': True, 'delete': True},
# 								'name': 'Book',
# 								'add_url': '/admin/Book/book/add/',
# 								'object_name': 'Book',
# 								'admin_url': '/admin/Book/book/'
# 							}
# 					],
# 		'app_label': 'Book'
# 	},
# 	{
# 		'has_module_perms': True,
# 		'app_url': '/admin/Localisation/',
# 		'name': 'Localisation',
# 		'models': [
# 							{
# 								'perms': {'change': True, 'add': True, 'delete': True},
# 								'name': 'Country',
# 								'add_url': '/admin/Localisation/country/add/',
# 								'object_name': 'Country',
# 								'admin_url': '/admin/Localisation/country/'
# 							},
# 							{
# 								'perms': {'change': True, 'add': True, 'delete': True},
# 								'name': 'Zone',
# 								'add_url': '/admin/Localisation/zone/add/',
# 								'object_name': 'Zone',
# 								'admin_url': '/admin/Localisation/zone/'
# 							}
# 					],
# 		'app_label': 'Localisation'
# 	},
# 	{
# 		'has_module_perms': True,
# 		'app_url': '/admin/Publisher/',
# 		'name': 'Publisher',
# 		'models': [
# 							{
# 								'perms': {'change': True, 'add': True, 'delete': True},
# 								'name': 'Publisher',
# 								'add_url': '/admin/Publisher/publisher/add/',
# 								'object_name': 'Publisher',
# 								'admin_url': '/admin/Publisher/publisher/'
# 							}
# 					],
# 		'app_label': 'Publisher'
# 	}
# ]

@register.inclusion_tag('admin/common/_sidemenu.html')
def get_side_menu(request):
    """
    This method is used to set up the side menu for admin site.
    :param cl:
    :param request: The current request with user
    :return: side menu html
    """
    return {'app_list': admin.site.get_app_list(request)}



