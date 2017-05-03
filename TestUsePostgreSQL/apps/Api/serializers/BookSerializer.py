#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 5/3/2017 1:44 PM
# @Author  : Cody Zhou
# @File    : BookSerializer.py
# @Software: PyCharm
# @Description:
#   
#   
from rest_framework import serializers

from TestUsePostgreSQL.apps.Book.models import Book
from TestUsePostgreSQL.apps.Api.serializers.AuthorSerializer import AuthorRelatedSerializer


class BookListSerializer(serializers.ModelSerializer):
    author = AuthorRelatedSerializer(many=True, read_only=True)
    book_url = serializers.HyperlinkedIdentityField(view_name='api:BookDetails')
    # choose this field will only show the id.
    # author = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    publisher = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            'id',
            'publisher',
            'author',
            'title',
            'book_url',
            'status',
            'publish_date',
            'added_date',
            'updated_date',
        )

    def get_publisher(self, obj):
        return obj.publisher.name


class BookDetailsSerializer(serializers.ModelSerializer):
    author = AuthorRelatedSerializer(many=True, read_only=True)
    publisher = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            'id',
            'publisher',
            'author',
            'title',
            'summary',
            'status',
            'publish_date',
            'added_date',
            'updated_date',

        )

    def get_publisher(self, obj):
        return obj.publisher.name


class BookAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'publisher',
            'author',
            'title',
            'summary',
            'status',
            'publish_date',
        )


class BookDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
        )

