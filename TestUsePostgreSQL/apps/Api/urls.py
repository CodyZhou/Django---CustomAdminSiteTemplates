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

from TestUsePostgreSQL.apps.Api.views.AuthorView import (
    APIAuthorList,
    APIAuthor,
    APIAuthorAdd,
    APIAuthorAddress
)
from TestUsePostgreSQL.apps.Api.views.BookView import (
    APIBookListView,
    APIBookDetailsView,
    APIBookAddView,
    APIBookEditView,
    APIBookDeleteView
)

urlpatterns = [
    # For Author
    url(r'author/list/$', APIAuthorList.as_view(), name="AuthorList"),
    url(r'author/add/$', APIAuthorAdd.as_view(), name="AuthorAdd"),
    url(r'author/(?P<pk>[0-9]+)/$', APIAuthor.as_view(), name="AuthorDetails"),
    # url(r'author/(?P<pk>[0-9]+)/edit/$', APIAuthor.as_view(), name="AuthorEdit"),

    # For Author Address
    url(r'address/(?P<author_id>[0-9]+)/$', APIAuthorAddress.as_view()),

    # For Book
    url(r'book/list/$', APIBookListView.as_view(), name="BookList"),
    url(r'book/add/$', APIBookAddView.as_view(), name="BookAdd"),
    url(r'book/(?P<pk>[0-9]+)/$', APIBookDetailsView.as_view(), name="BookDetails"),
    url(r'book/(?P<pk>[0-9]+)/edit$', APIBookEditView.as_view(), name="BookEdit"),
    url(r'book/(?P<pk>[0-9]+)/delete$', APIBookDeleteView.as_view(), name="BookDelete"),

]


