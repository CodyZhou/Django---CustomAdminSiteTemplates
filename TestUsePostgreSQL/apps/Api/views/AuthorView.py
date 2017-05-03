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

from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)

from TestUsePostgreSQL.apps.Author.models import Author, AuthorAddress

from TestUsePostgreSQL.apps.Api.serializers.AuthorSerializer import (
    AuthorSerializer,
    AuthorAddSerializer,
    AuthorAddressSerializer,
)


class APIAuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()

        # Use Paginator
        paginator = Paginator(authors, 2)

        # Get the page
        page = self.request.GET.get('page', 1)

        try:
            if int(page) > paginator.num_pages:
                page = paginator.num_pages
        except ValueError:
            page = 1

        print("--------------- Page -----------")
        print(page)
        print("--------------- Page -----------")

        results = paginator.page(page)

        serializer = AuthorSerializer(results, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class APIAuthorAdd(APIView):
    def post(self, request):
        serializer = AuthorAddSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
# Test data for Author Add and Author Edit
{
    "firstname": "API-01",
    "lastname": "Test",
    "email": "cody@jiusite-2234.com",
    "phone": "11223344345",
    "status": 10
}
"""


class APIAuthor(APIView):
    def get(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
        except:
            raise Http404

        serializer = AuthorSerializer(author)

        return Response(serializer.data)

    def put(self, request, pk):
        author = Author.objects.get(pk=pk)
        serializer = AuthorAddSerializer(author, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = Author.objects.get(pk=pk)
        author.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class APIAuthorAddress(APIView):
    def get(self, request, *args, **kwargs):
        author_id = kwargs.get('author_id')
        address = AuthorAddress.objects.filter(author_id=author_id)
        # print(list(address))
        # try:
        #     author_id = kwargs.get('author_id')
        #     print("--------------")
        #     print(author_id)
        #     print("--------------")
        #     address = AuthorAddress.objects.filter(Author__id=author_id)
        #     print(address)
        # except:
        #     raise Http404

        serializer = AuthorAddressSerializer(address, many=True)

        return Response(serializer.data)


