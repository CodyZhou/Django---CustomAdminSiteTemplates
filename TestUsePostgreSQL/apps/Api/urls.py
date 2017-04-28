#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : urls.py
# @Time    : 2017/4/27 20:32
# @Author  : Cody Zhou
# @Software: PyCharm
# @Description: 
#
#
from django.conf.urls import url

from TestUsePostgreSQL.apps.Api.views.AuthorView import APIAuthorList, APIAuthor, APIAuthorAddress

urlpatterns = [
    # For Author
    url(r'author/list/$', APIAuthorList.as_view()),
    url(r'author/(?P<pk>[0-9]+)/$', APIAuthor.as_view()),

    # For Author Address
    url(r'address/(?P<author_id>[0-9]+)/$', APIAuthorAddress.as_view()),

]


