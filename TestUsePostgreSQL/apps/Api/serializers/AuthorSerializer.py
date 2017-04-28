#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : AuthorSerializer.py
# @Time    : 2017/4/27 21:32
# @Author  : Cody Zhou
# @Software: PyCharm
# @Description: 
#
#
from rest_framework import serializers

from TestUsePostgreSQL.apps.Author.models import Author, AuthorAddress


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'firstname', 'lastname', 'email', 'phone', 'status', 'added_date', 'updated_date')


class AuthorAddressSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer
    class Meta:
        model = AuthorAddress
        fields = ('id', '__str__')

