#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 3/23/2017 5:54 PM
# @Author  : Cody Zhou
# @File    : adminviews.py
# @Software: PyCharm
# @Description:
#   
#   

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login


class AdminLogin(View):
    def get(self, request, *args, **kwargs):
        next = request.GET['next']
        return render(request, 'admin/login.html', context={'next': next})

    def post(self, request, *args, **kwargs):

        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            print("We got next request is: {0}" . format(next))

            return HttpResponseRedirect(next)
        else:
            return render(request, 'admin/login.html', context={'errorMessages': ['Can not find this user!'] })


