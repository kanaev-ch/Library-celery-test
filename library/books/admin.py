from django.contrib import admin


from .models import Books


class BooksAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'pub_date')
    search_fields = ('title',)
    list_filter = ('title', 'author')
    list_editable = ('title',)
    empty_value_display = '-пусто-'


admin.site.register(Books, BooksAdmin)
