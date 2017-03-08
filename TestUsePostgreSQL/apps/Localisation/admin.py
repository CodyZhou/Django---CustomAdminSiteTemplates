from django.contrib import admin

from TestUsePostgreSQL.apps.Localisation.models import Country, Zone


# Register your models here.
admin.site.register(Country)
admin.site.register(Zone)

