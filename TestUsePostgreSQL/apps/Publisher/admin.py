from django.contrib import admin

from TestUsePostgreSQL.libs.admin.links import AdminSpecialLinks
from TestUsePostgreSQL.apps.Publisher.models import Publisher


# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'added_date', 'edit_link')
    list_display_links = ('edit_link',)
    search_fields = ('name',)

    def edit_link(self, publisher):
        return AdminSpecialLinks().edit_link
    edit_link.short_description = 'Action'

admin.site.register(Publisher, PublisherAdmin)

