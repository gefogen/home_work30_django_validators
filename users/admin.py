from django.contrib import admin

from users.models import User, Location


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role', 'age',)
    list_display_links = ('username',)
    search_fields = ('last_name',)


admin.site.register(User, UsersAdmin)
admin.site.register(Location)
