from django.contrib import admin

# Register your models here.
from teachers_site_api.models import Answer, Course, Lesson

admin.site.register(Answer)
admin.site.register(Course)
admin.site.register(Lesson)