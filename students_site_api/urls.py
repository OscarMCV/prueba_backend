from django.urls import path
from students_site_api import views
#from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('courses/<str:course_id>/', views.CourseDetail.as_view()),
    #Retrieve all the lessons (and their id's) of a given ID course, also is able to delete it
    path('lessons/<str:lesson_id>/', views.SolveLesson.as_view()),
    #Retrieve all the questions and the answers to ve solved    
    path('courses/', views.CourseView.as_view()),
    #Retrieve all the courses and make new ones
    path('lessons/', views.LessonView.as_view()),
    #Retrieve all the lessons in the database, it can also create a lesson for a given course
    #path('lessons/<str:lesson_id>', views.SolveLesson.as_view()),
    #Retrieve the information of all the questions in the database. Create a new question with the given characteristics
]
