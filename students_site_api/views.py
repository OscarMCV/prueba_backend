from django.db.models.query import QuerySet
from django.http import Http404
#Core Django imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
#Rest_framework imports
from teachers_site_api import serializers
from teachers_site_api import models
from students_site_api import serializers as student_serializers
from students_site_api import models as student_models
from users_manage_api.permissions import IsStudent, IsTeacher
#Imports from internal apps


class CourseView(APIView):
    """
    Retrieve all the information of every course
    """
    permission_classes = [IsAuthenticated & IsStudent]
    serializer_class = serializers.CreateCourseSerializer

    def get(self, request, format=None):
        courses = models.Course.objects.all()
        serializer = serializers.CreateCourseSerializer(courses, many=True)
        return Response(serializer.data)


class LessonView(APIView):
    """
     Retrieve all the lessons in the system
     """
    permission_classes = [IsAuthenticated & IsStudent]
    serializer_class = serializers.CreateLessonSerializer
    queryset = models.Lesson.objects.all()

    def get(self, request, format=None):
        lessons = models.Lesson.objects.all()
        serializer = serializers.CreateLessonSerializer(lessons, many=True)
        return Response(serializer.data)


class QuestionView(APIView):
    """
    Retrieve all the questions in the
    system
    """
    permission_classes = [IsAuthenticated & IsStudent]
    serializer_class = serializers.CreateQuestionSerializer
    queryset = models.Question.objects.all()

    def get(self, request):
        questions = models.Question.objects.all()
        serializer = serializers.CreateQuestionSerializer(questions, many=True)
        return Response(serializer.data)


#The APIView's for the details
class CourseDetail(APIView):
    """
    Retrieve all the lessons (and their id's) of a given ID course
    Don't support post method for students
    """
    permission_classes = [IsAuthenticated & IsStudent]

    def get(self, request, course_id):
        try:
            course = models.Course.objects.get(pk=course_id)
            course_serialized = serializers.CreateCourseSerializer(course)
            ####NEED CONVERT INTO JSON FCKING STUPID################## don't forget
            lessons = models.Lesson.objects.filter(course=course_id)
            lessons_serialized = serializers.CreateLessonSerializer(lessons, many=True)
            data = {
                "The follow lessons came from": course_serialized.data['name'],
                "lessons of the course": lessons_serialized.data,
            }
            #It has to send the lessons ID
        except models.Course.DoesNotExist:
            raise Http404
        #serializer = serializers.CreateCourseSerializer(course)
        return Response(data)


class LessonDetail(APIView):
    """
    Retrieve detailed lessons
    Don't support post method
    """
    permission_classes = [IsAuthenticated & IsStudent]
    serializer_class = serializers.CreateLessonSerializer
    queryset = models.Lesson.objects.all()

    def get(self, request, lesson_id):
        try:
            course = models.Course.objects.get(lessons=lesson_id)
            course_serialized = serializers.CreateCourseSerializer(course)
            lesson = models.Lesson.objects.get(pk=lesson_id)
            #Retrieve an specific lesson
            lesson_serialized = serializers.CreateLessonSerializer(lesson)
            questions = models.Question.objects.filter(lesson=lesson_id,)
            #Questions which came from "D" lessons
            question_serialized = serializers.CreateQuestionSerializer(questions, many=True)
            data = {
                'This lesson came from': course_serialized.data['name'],
                'lesson': lesson_serialized.data['name'],
                'questions': question_serialized.data
            }
            #It has to send the question id
        except models.Lesson.DoesNotExist:
            raise Http404
        #serializer = serializers.CreateCourseSerializer(course)
        return Response(data)


class SolveLesson(APIView):
    """
    Retrieve all the questions of a lesson and their possible
    answers
    """
    permission_classes = [IsAuthenticated & IsStudent]
    serializer_class = student_serializers.ShowQuestionForStudentsSerializer

    def get(self, request, lesson_id):
        try:
            questions = models.Question.objects.filter(lesson=lesson_id)
            serialized_questions = student_serializers.ShowQuestionForStudentsSerializer(questions, many=True)
        except models.Question.DoesNotExist:
            raise Http404
        return Response(serialized_questions.data)
