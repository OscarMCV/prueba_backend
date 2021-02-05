from django.urls import path
from teachers_site_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('teachers-site/classes/', views.ClassView.as_view()),
    path('teacher-site/classes/<str:class_id>/', views.ClassDetail.as_view()),
    path('teacher-site/classes/<str:class_id>/courses/', views.CourseView.as_view()),
    path('teacher-site/classes/<str:class_id>/courses/<str:course_id>', views.CourseDetail.as_view()),
    path('teacher-site/classes/<str:class_id>/courses/<str:course_id>/lessons/', views.LessonView.as_view()),
    path('teacher-site/classes/<str:class_id>/courses/<str:course_id>/lessons/<str: lesson_id>', views.LessonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
