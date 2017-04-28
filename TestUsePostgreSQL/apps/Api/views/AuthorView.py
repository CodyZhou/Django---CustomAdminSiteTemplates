#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : AuthorView.py
# @Time    : 2017/4/27 21:25
# @Author  : Cody Zhou
# @Software: PyCharm
# @Description: 
#
#
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from TestUsePostgreSQL.apps.Author.models import Author, AuthorAddress

from TestUsePostgreSQL.apps.Api.serializers.AuthorSerializer import AuthorSerializer, AuthorAddressSerializer


class APIAuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        print(serializer.data)
        return Response(serializer.data)

    # def post(self, request):
    #     pass


class APIAuthor(APIView):
    def get(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
        except:
            raise Http404

        serializer = AuthorSerializer(author)

        return Response(serializer.data)

    # def post(self, request, ):


class APIAuthorAddress(APIView):
    def get(self, request, *args, **kwargs):
        author_id = kwargs.get('author_id')
        address = AuthorAddress.objects.filter(author_id=author_id)
        print(list(address))
        # try:
        #     author_id = kwargs.get('author_id')
        #     print("--------------")
        #     print(author_id)
        #     print("--------------")
        #     address = AuthorAddress.objects.filter(Author__id=author_id)
        #     print(address)
        # except:
        #     raise Http404

        serializer = AuthorAddressSerializer(address)

        return Response(serializer.data)


