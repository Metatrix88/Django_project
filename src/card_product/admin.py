from django.contrib import admin
from . import models


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('data_register', 'data_changes')

admin.site.register(models.Book, BookAdmin)
