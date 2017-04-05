from django.apps import apps
from django.contrib import admin

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth import (
    authenticate,
    login,
    logout
)


class AdminLogin(View):
    """
    Purpose: This class is used to replace the login logic of the django default admin site.
    """
    def get(self, request, *args, **kwargs):
        """
        This method is used to catch the GET request, show the login page.
        :param request: GET request.
        :param args:
        :param kwargs:
        :return: admin/login.html
        """
        # Get the next url, it is used to define the next location after the login successful.
        next_url = request.GET.get('next', '/admin/')
        return render(request, 'admin/login.html', context={'next': next_url})

    def post(self, request, *args, **kwargs):
        """
        This method is used to get the data from page, verify the user's data.
        :param request: POST requst
        :param args:
        :param kwargs:
        :return:
                If the user exist, go to the previous url, otherwise, go back to login page.
        """
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        next_url = request.POST.get('next', '/admin/login')

        # Verify the data
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                print(user.get_group_permissions())
                print(user.get_all_permissions())
                print(dir(user))
                print('------ APPS -------')
                print(apps.get_app_configs())
                print('------- APPS  ----------')
                print(admin.site.get_app_list(request))


                print("We got next request is: {0}" . format(next_url))

                return HttpResponseRedirect(next_url)

            else:
                return render(request, 'admin/login.html',
                              context={'errorMessages': ['This user is not active, please contact administrator'],
                                       'next': next_url}
                              )
        else:
            return render(request, 'admin/login.html',
                          context={'errorMessages': ['Can not find this user!'], 'next': next_url })


class AdminLogout(View):
    """
    Purpose:  This class is used to replace the logout logic of django default admin site.
    Limit:  This class does not support the POST request.
    """

    def get(self, request, *args, **kwargs):
        """
        This method is used to do the logout logic, release all data from the user session.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # Logout the user
        logout(request=request)

        # redirect to the admin/
        # return HttpResponseRedirect('/admin/')

        # using logout template
        return render(request, 'admin/logout.html')


class AdminIndex(View):
    """
    Purpose:  This class is used to replace the index logic of django default admin site.
    Limit:  This class does not support the POST request.
    """
    def get(self, request, *args, **kwargs):
        # check the user's permission, get all app_list.

        # Follow the permission to go to the dashboard or go to the login template


        pass