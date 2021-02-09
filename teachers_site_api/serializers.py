from rest_framework import serializers

from teachers_site_api import models


class HelloSerializer(serializers.Serializer):
    """Create a serializer for a request in my HelloApiView"""
    name = serializers.CharField(max_length=10)


class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'

    def get_lessons(self, course):
        try:
            course_lessons = models.CreateLesson.objects.filter(lesson__id=course.id)
            return CreateLessonSerializer(course_lessons)
        except models.CreateLesson.DoesNotExist:
            return None


class CreateLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ['name', 'questions']


class CreateQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'
