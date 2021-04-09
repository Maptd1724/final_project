from django.contrib import admin

from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('price',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'price')
    list_per_page = 25

admin.site.register(Menu, MenuAdmin)
