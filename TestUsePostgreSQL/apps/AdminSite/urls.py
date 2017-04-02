#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 3/24/2017 3:59 PM
# @Author  : Cody Zhou
# @File    : urls.py
# @Software: PyCharm
# @Description:
#   
#   
from django.conf.urls import url
#from django.contrib import admin

from TestUsePostgreSQL.apps.AdminSite.views import (
    AdminLogin,
    AdminLogout,
)

app_name = "admin_site"

urlpatterns = [
    # My admin site
    #url(r'^$', admin.site.urls),
    url(r'^login/$', AdminLogin.as_view(), name="login"),
    url(r'^logout/$', AdminLogout.as_view(), name="logout"),

]