from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from teachers_site_api import serializers
from teachers_site_api import models


class ClassView(APIView):
    """Serializer to get the fields"""
    def get(self, request):
        """Method to get the classes"""
        classes = models.CreateClass.objects.all()
        serializer = serializers.CreateClassSerializer(classes, many=True)
        """The parameter "many=True" tell drf that queryset contains mutiple 
        items (a list of items) so drf needs to serialize each item with serializer 
        class (and serializer.data will be a list)"""
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CreateClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassDetail(APIView):
    def get(self, request, class_id):
        try:
            name_class = models.CreateClass.objects.get(pk=class_id)
        except models.CreateClass.DoesNotExist:
            raise Http404
        serializer = serializers.CreateClassSerializer(name_class)
        return Response(serializer.data)

    def delete(self, request, class_id):
        try:
            name_class = models.CreateClass.objects.get(pk=class_id)
        except models.CreateClass.DoesNotExist:
            raise Http404
        name_class.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseView(APIView):
    def get(self, request, format=None):
        courses = models.CreateCourse.objects.all()
        serializer = serializers.CreateCourserSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.CreateCourseSerializer(data=request.data)
        if serializers.is_valid:
            serializers.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    def get(self, request, course_id):
        try:
            course = models.CreateCourse.objects.get(pk=course_id)
        except models.CreateCourse.DoesNotExist:
            raise Http404
        serializer = serializers.CreateCourseSerializer(course)
        return Response(serializer.data)

    def delete(self, request, course_id):
        try:
            course = models.CreateCourse.objects.get(pk=course_id)
        except models.CreateCourse.DoesNotExist:
            raise Http404
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LessonView(APIView):
    def get(self, request, format=None):
        lessons = models.CreateLesson.objects.all()
        serializer = serializers.CreateLessonSerializer(lessons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.CreateLessonsSerializer(data=request.data)
        if serializers.is_valid:
            serializers.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonDetail(APIView):
    def get(self, request, lesson_id):
        try:
            lesson = models.CreateLesson.objects.get(pk=lesson_id)
        except models.CreateLesson.DoesNotExist:
            raise Http404
        serializer = serializers.CreateLessonSerializer(lesson)
        return Response(serializer.data)

    def delete(self, request, lesson_id):
        try:
            lesson = models.CreateCourse.objects.get(pk=lesson_id)
        except models.CreateCourse.DoesNotExist:
            raise Http404
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionView(APIView):
    def get(self, request):
        questions = models.CreateQuestion.objects.all()
        serializer = serializers.CreateQuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = models.CreateQuestion(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
