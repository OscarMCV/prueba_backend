#Django Core Imports
from django.urls import path
#Internal apps imports
from teachers_site_api import views

urlpatterns = [
    path('courses/<str:course_id>/', views.CourseDetail.as_view()),
    #Retrieve all the lessons (and their id's) of a given ID course, also is able to delete it
    path('lessons/<str:lesson_id>/', views.LessonDetail.as_view()),
    #Retrieve all the questions (and their id's) of a given ID lesson, also is able to delete it
    path('questions/<str:question_id>/', views.QuestionDetail.as_view()),
    #Retrieve all the answers of a question, and create new ones


    path('courses/', views.CourseView.as_view()),
    #Retrieve all the courses and make new ones
    path('lessons/', views.LessonView.as_view()),
    #Retrieve all the lessons in the database, it can also create a lesson for a given course
    path('questions/', views.QuestionView.as_view()),
    #Retrieve the information of all the questions in the database. Create a new question with the given characteristics
]
"""
The first paths, are the logic paths to manage the data
in an very detailed way.

The second paths, are the non detailed objects, they
could manage some nested relations but always undetailed
"""

