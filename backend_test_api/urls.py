from django.urls import path, include
from backend_test_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('teachers-manage-site/', views.CreateClassView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
