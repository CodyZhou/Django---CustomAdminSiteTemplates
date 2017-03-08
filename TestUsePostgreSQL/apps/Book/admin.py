from django.contrib import admin

from TestUsePostgreSQL.apps.Book.models import Book


# Register your models here.
admin.site.register(Book)