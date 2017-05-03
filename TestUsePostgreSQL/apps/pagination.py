#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 5/3/2017 11:49 AM
# @Author  : Cody Zhou
# @File    : pagination.py
# @Software: PyCharm
# @Description:
#   
#   
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class TPSPagination(PageNumberPagination):
    page_size = 2

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'result': data
        })

