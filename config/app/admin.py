from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.http import HttpRequest
from app.models import Item, Type, Season


@admin.register(Item)
class ItemAdmin(ModelAdmin):
    """The admin panel for Item model"""

    list_display = ("title", "type", "item_season")
    list_display_links = ("title",)
    search_fields = ("title", "type")
    
    def get_queryset(self, request: HttpRequest):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related("season")

    def item_season(self, object):
        return ", ".join([str(i) for i in object.season.all()])


@admin.register(Type)
class TypeAdmin(ModelAdmin):
    """The Admin panel for Type model"""

    list_display = ("title",)
    list_display_links = ("title",)
    search_fields = ("title",)


@admin.register(Season)
class SeasonAdmin(ModelAdmin):
    """The Admin panel for Season model"""

    list_display = ("title",)
    list_display_links = ("title",)
    search_fields = ("title",)
