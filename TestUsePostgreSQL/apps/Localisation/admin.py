from django.contrib import admin

from TestUsePostgreSQL.libs.admin.links import AdminSpecialLinks
from TestUsePostgreSQL.apps.Localisation.models import Country, Zone


# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso_code_3', 'status', 'edit_link')
    list_display_links = ('edit_link',)
    list_filter = ('status',)

    search_fields = ('name', 'iso_code_3')

    def edit_link(self, country):
        return AdminSpecialLinks().edit_link
    edit_link.short_description = 'Action'


admin.site.register(Country, CountryAdmin)


class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'show_country_name', 'status', 'edit_link')
    list_display_links = ('edit_link',)
    list_filter = ('status',)

    search_fields = ('name', 'country__name')

    def show_country_name(self, zone):
        return zone.country.name
    show_country_name.short_description = "Country Name"

    def edit_link(self, zone):
        return AdminSpecialLinks().edit_link
    edit_link.short_description = 'Action'


admin.site.register(Zone, ZoneAdmin)

