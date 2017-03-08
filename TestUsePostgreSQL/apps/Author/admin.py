from django.contrib import admin

from TestUsePostgreSQL.apps.Author.models import Author, AuthorAddress


class AuthorAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(AuthorAddress)