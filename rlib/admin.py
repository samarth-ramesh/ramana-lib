from django.contrib import admin

from rlib import models


class BookAdmin(admin.ModelAdmin):
    search_fields = ['BookId','BookTitle', 'Author']
    list_display = ['BookId','BookTitle', 'Author', 'Category', 'NewShelfCode', 'Description']


# Register your models here.
admin.site.register(models.Book, BookAdmin)
