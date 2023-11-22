from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'username', 'pub_date')
    search_fields = ('username',)
    list_filter = ('username', 'email')
    list_editable = ('username',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
