#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 5/3/2017 1:44 PM
# @Author  : Cody Zhou
# @File    : Book.py
# @Software: PyCharm
# @Description:
#   
#   

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)

from TestUsePostgreSQL.apps.Book.models import Book
from TestUsePostgreSQL.apps.Api.serializers.BookSerializer import (
    BookListSerializer,
    BookDetailsSerializer,
    BookDeleteSerializer,
    BookAddSerializer,
)
from TestUsePostgreSQL.apps.pagination import TPSPagination


class APIBookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    pagination_class = TPSPagination


class APIBookDetailsView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailsSerializer


class APIBookAddView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookAddSerializer


class APIBookEditView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookAddSerializer


class APIBookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDeleteSerializer

