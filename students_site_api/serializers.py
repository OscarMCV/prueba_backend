#Djanco core imports
from django.db import models
#Rest framework imports
from rest_framework import serializers
#Internal apps imports
from teachers_site_api import models

#https://www.django-rest-framework.org/api-guide/serializers/#baseserializer


class ShowAnswersForStudents(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = '__all__'
        exclude = {'kind_answer'}


class LessonSerializer(serializers.Serializer):
    class Meta:
        models = models.Lesson
        fields = ['name']


class ShowQuestionForStudentsSerializer(serializers.ModelSerializer):
    answers = ShowAnswersForStudents

    class Meta:
        model = models.Question
        fields = ['the_question_is', 'score', 'GoodAnswers', 'BadAnswers', 'answers']
