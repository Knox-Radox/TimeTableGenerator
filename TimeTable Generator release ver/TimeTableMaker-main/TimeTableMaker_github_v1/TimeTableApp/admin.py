from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Subjects)
admin.site.register(models.Teachers)
admin.site.register(models.TimeTable)
