from django.contrib import admin

# Register your models here.
from students_site_api.models import Related_Course, Related_Lesson, StudentProgress, RelateAnswers

admin.site.register(Related_Lesson)
admin.site.register(Related_Course)
admin.site.register(StudentProgress)
admin.site.register(RelateAnswers)
