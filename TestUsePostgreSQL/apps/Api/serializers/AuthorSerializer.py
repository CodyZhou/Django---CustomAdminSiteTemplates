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
from TestUsePostgreSQL.apps.Localisation.models import Country, Zone


class AuthorRelatedSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:AuthorDetails',
    )

    class Meta:
        model = Author
        fields = ('id', 'firstname', 'lastname', 'url')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'firstname', 'lastname', 'email', 'phone', 'status', 'added_date', 'updated_date')


class AuthorAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'firstname',
            'lastname',
            'email',
            'phone',
            'status'
        )


class AuthorAddressSerializer(serializers.ModelSerializer):
    # author_id = serializers.SerializerMethodField()
    fulladdress = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    zone = serializers.SerializerMethodField()

    class Meta:
        model = AuthorAddress
        fields = ('id', 'author_id', 'author_name', 'address_1', 'address_2', 'city', 'zip', 'zone', 'country', 'fulladdress')

    def get_author_name(self, obj):
        return obj.author.firstname + ' ' + obj.author.lastname

    def get_country(self, obj):
        return obj.country.name

    def get_zone(self, obj):
        return obj.zone.name

    def get_fulladdress(self, obj):
        return obj.get_address()



