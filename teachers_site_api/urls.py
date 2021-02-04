from django.urls import path
from teachers_site_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('teachers-site/', views.CreateClassView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
