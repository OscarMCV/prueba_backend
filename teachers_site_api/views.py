from django.db.models.query import QuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from teachers_site_api import serializers
from teachers_site_api import models
from users_manage_api.permissions import IsTeacher

"""
this is how the request works
https://docs.djangoproject.com/en/3.1/ref/request-response/#django.http.HttpRequest
"""


class CourseView(APIView):
    """
    Retrieve all the information of every course
    """
    permission_classes = [IsAuthenticated & IsTeacher]
    serializer_class = serializers.CreateCourseSerializer

    def get(self, request, format=None):
        courses = models.Course.objects.all()
        serializer = serializers.CreateCourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CreateCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonView(APIView):
    """
     Retrieve all the information of ev
     """
    serializer_class = serializers.CreateLessonSerializer
    queryset = models.Lesson.objects.all()

    def get(self, request, format=None):
        lessons = models.Lesson.objects.all()
        serializer = serializers.CreateLessonSerializer(lessons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.CreateLessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionView(APIView):
    serializer_class = serializers.CreateQuestionSerializer
    queryset = models.Question.objects.all()

    def get(self, request):
        questions = models.Question.objects.all()
        serializer = serializers.CreateQuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CreateQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#The APIView for the details
class CourseDetail(APIView):
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

    def delete(self, request, course_id):
        try:
            course = models.Course.objects.get(pk=course_id)
        except models.CreateCourse.DoesNotExist:
            raise Http404
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LessonDetail(APIView):
    serializer_class = serializers.CreateLessonSerializer
    queryset = models.Lesson.objects.all()

    def get(self, request, lesson_id, course_id):
        try:
            course = models.Course.objects.get(pk=course_id)
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
        except models.Course.DoesNotExist:
            raise Http404
        #serializer = serializers.CreateCourseSerializer(course)
        return Response(data)

    def delete(self, request, lesson_id):
        try:
            lesson = models.Lesson.objects.get(pk=lesson_id)
        except models.Lesson.DoesNotExist:
            raise Http404
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionDetail(APIView):
    """
    Gives details of a question, name, answers and kind of answers.
    also in this view is where the answers are created.
    """
    serializer_class = serializers.CreateAnswerSerializer

    def get(self, request, question_id, course_id, lesson_id):
        try:
            question = models.Question.objects.get(pk=question_id)
            #Retrieve an specific question object
            question_serialized = serializers.CreateQuestionSerializer(question)
            answers = models.Answer.objects.filter(question=question_id)
            #Retrieve all the answers of the question
            answers_serialized = serializers.CreateAnswerSerializer(answers, many=True)
            data = {
                'question': question_serialized.data['the_question_is'],
                'answers': answers_serialized.data
            }
        except models.Question.DoesNotExist:
            raise Http404
        return Response(data)

    def post(self, request, question_id, course_id, lesson_id):
        serializer = serializers.CreateAnswerSerializer(
            data=request.data,
            context={'question_id': question_id}
        )
        #The context should give the answer serializer, the question which they belong of the answers,
        #in order to get the data to keep safe the logic of the answers
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, question_id, course_id, lesson_id):
        try:
            question = models.Question.objects.get(pk=question_id)
        except models.Question.DoesNotExist:
            raise Http404
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
