#Django
from django.urls import path

#Django rest framework
from rest_framework.urlpatterns import format_suffix_patterns

#Views
from users_manage_api import views as user_views
"""In order to handle urls management better, the "views" name has been changed"""
urlpatterns = [
    path('login/', user_views.UserAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
