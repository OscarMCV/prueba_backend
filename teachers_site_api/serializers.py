from rest_framework import serializers

from teachers_site_api import models


class HelloSerializer(serializers.Serializer):
    """Create a serializer for a request in my HelloApiView"""
    name = serializers.CharField(max_length=10)


class CreateClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreateClass
        fields = '__all__'


class CreateCourserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreateCourse
        fields = '__all__'


class CreateLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreateLesson
        fields = '__all__'


class CreateQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreateQuestion
        fields = '__all__'
