from django.contrib import admin
from django.contrib.admin import site

from ads.models import Ad, Category


class AdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ("is_published",)
    list_filter = ('is_published',)


admin.site.register(Ad, AdsAdmin)
admin.site.register(Category)