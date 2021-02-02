from django.contrib import admin

from backend_test_api import models

# Register your models here.
admin.site.register(models.CreateClass),
admin.site.register(models.CreateCourse),
admin.site.register(models.CreateLesson),
admin.site.register(models.CreateQuestion),