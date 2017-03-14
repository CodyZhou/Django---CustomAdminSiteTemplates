from django.contrib import admin

from TestUsePostgreSQL.libs.admin.links import AdminSpecialLinks
from TestUsePostgreSQL.apps.Book.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_author_name_list', 'show_publisher_name', 'publish_date', 'status', 'added_date', 'edit_link')
    list_display_links = ('edit_link',)

    list_filter = ('status', 'added_date', 'publish_date',  'publisher__name')

    search_fields = ('title',  'publisher__name')

    # def show_author_full_name(self, author):
    #     return "{0} {1}" . format(author.firstname, author.lastname)
    # show_author_full_name.shor_description = "Author Name"

    def show_publisher_name(self, book):
        return book.publisher.name
    show_publisher_name.short_description = "Publisher"

    def edit_link(self, book):
        return AdminSpecialLinks().edit_link
    edit_link.short_description = "Action"

    def get_author_name_list(self, book):
        # print(book.author)
        return ', '.join(user.firstname + ' ' + user.lastname for user in book.author.all())

    get_author_name_list.short_description = "Author"

# Register your models here.
admin.site.register(Book, BookAdmin)

