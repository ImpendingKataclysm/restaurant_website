from django.contrib import admin

from .models import Item, Location


class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "status")
    list_filter = ("status",)
    search_fields = ("name", "description")


class LocationAdmin(admin.ModelAdmin):
    list_display = ("city", "postal")
    list_filter = ("city", )
    search_fields = ("city", "postal")


admin.site.register(Item, MenuAdmin)
admin.site.register(Location, LocationAdmin)
