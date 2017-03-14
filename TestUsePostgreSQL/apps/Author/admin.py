from django.contrib import admin

from TestUsePostgreSQL.libs.admin.links import AdminSpecialLinks
from TestUsePostgreSQL.apps.Author.models import Author, AuthorAddress


class AuthorAdmin(admin.ModelAdmin):
    # OR you can set list_display = ('get_full_name',) to display author's full name.
    list_display = ('__str__', 'show_author_full_name', 'email', 'format_phone', 'status', 'added_date', 'edit_link')
    list_display_links = ('edit_link',)

    list_filter = ('status', 'added_date')

    search_fields = ('firstname', 'lastname', 'email')

    def show_author_full_name(self, author):
        return '{0} {1}' . format(author.firstname, author.lastname)

    show_author_full_name.short_description = 'Full Name'

    def format_phone(self, author):
        return '({0}){1}-{2}' . format(author.phone[:3], author.phone[3:6], author.phone[6:])

    format_phone.short_description = 'Phone'

    # Show 'edit' link
    def edit_link(self, author):
        return AdminSpecialLinks().edit_link

    edit_link.short_description = 'Action'

    pass

# Register your models here.
admin.site.register(Author, AuthorAdmin)


class AuthorAddressAdmin(admin.ModelAdmin):

    list_display = ('show_author_full_name', 'show_full_address', 'edit_link')
    list_display_links = ('edit_link', )

    search_fields = ('author__firstname', 'author__lastname', 'address_1', 'address_2', 'city')

    def show_author_full_name(self, address):
        return "{0} {1}" . format(address.author.firstname, address.author.lastname)
    show_author_full_name.short_description = 'Author Name'

    def show_full_address(self, address):
        return address.get_address()
    show_full_address.short_description = 'Full Address'

    # Show 'edit' link
    def edit_link(self, author):
        return AdminSpecialLinks().edit_link

    edit_link.short_description = 'Action'

    pass

admin.site.register(AuthorAddress, AuthorAddressAdmin)

