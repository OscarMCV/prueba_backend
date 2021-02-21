#Djanco core imports
from django.db import models
#Rest framework imports
from rest_framework import serializers
#Internal apps imports
from teachers_site_api import models
from students_site_api import models as student_models

#https://www.django-rest-framework.org/api-guide/serializers/#baseserializer


class ShowAnswersForStudents(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        exclude = ['kind_answer', 'upload']


class ShowQuestionForStudentsSerializer(serializers.ModelSerializer):
    answers = ShowAnswersForStudents(many=True, read_only=True)
    #The question model has answers, that answers are serialized
    # exluding the kind_answer field and added to the serialized data

    class Meta:
        model = models.Question
        fields = ['the_question_is', 'answers']


class LessonAchivmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_models.LessonAchivments
        fields = '__all__'


class RelateAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_models.RelateAnswers
        fields = '__all__'
