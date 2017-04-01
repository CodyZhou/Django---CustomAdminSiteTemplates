from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login


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
        next_url = request.GET['next']
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
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.POST['next']

        # Verify the data
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            print("We got next request is: {0}" . format(next_url))

            return HttpResponseRedirect(next_url)
        else:
            return render(request, 'admin/login.html', context={'errorMessages': ['Can not find this user!'] })


class AdminIndex(View):
    """
    Purpose:  This class is used to replace the index logic of django default admin site.
    Limit:  This class does not receive the POST request.
    """
    def get(self, request, *args, **kwargs):
        # check the user's permission

        # Follow the permission to go to the dashboard or go to the login template


        pass