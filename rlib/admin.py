from django.contrib import admin

from rlib import models


class BookAdmin(admin.ModelAdmin):
    search_fields = ['BookTitle', 'Author']


# Register your models here.
admin.site.register(models.Book, BookAdmin)
