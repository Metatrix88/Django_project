from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Genre)
admin.site.register(models.Series)
admin.site.register(models.The_authors)
admin.site.register(models.Publishing_house)
