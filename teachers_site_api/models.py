from django.db import models

import uuid

from django.db.models.fields import BooleanField


KIND_OF_QUESTION = [('BOOLEAN', 'Boolean'),
                    ('MULTIPLECHOICE1', 'Multiple choice where only one answer is correct'),
                    ('MULTIPLECHOICE2', 'Multiple choice where more than one answer is correct'),
                    ('MULTIPLECHOICE3', 'Multiple choice where more than one answer is correct and all of them must be answered correctly'),
                    ]


class Course(models.Model):
    """Create a course which cointain the lessons"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    #Id is a uudid field which is the primary key for every Course
    name = models.CharField(max_length=120, unique=True,)

    def __str__(self):
        """Return string representation for the Course"""
        return self.name


class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    """Create a lesson which contain the questions"""
    #Id is a uudid field which is the primary key for every Lesson
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(null=False)
    the_lesson_is = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        unique_together = ['course', 'order']
        ordering = ['order']

    def __str__(self):
        """Return string representation for a Lesson"""
        return '%d: %s' % (self.order, self.name)


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    """Create a question which contains the kind of question and the answers"""
    lesson = models.ForeignKey(Lesson, related_name='questions', on_delete=models.CASCADE)
    #The related name will be handle has a field in the model seralizer of the lesson
    order = models.IntegerField()
    GoodAnswers = models.IntegerField(null=False, blank=False)
    BadAnswers = models.IntegerField(null=False, blank=False)
    #Could be "all answers are correct", this are the unique with capital letters
    the_question_is = models.CharField(max_length=200)
    score = models.IntegerField(default=1)
    type_question = models.CharField(max_length=120, choices=KIND_OF_QUESTION, default='BOOLEAN')

    class Meta:
        unique_together = ['lesson', 'order', ]
        #Cannot have a question two lessons or two  similar number of order
        ordering = ['order']
        #When is required, the questions order by the nomber of order

    def __str__(self):
        """Return the question as string"""
        return (self.the_question_is)
        #Return in a python form the data. %d is for decimal and %s is for a string


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=70)
    upload = models.DateField(auto_now=True)
    kind_answer = BooleanField()

    class Meta:
        ordering = ['upload']
        """Display answers by date"""

    def __str__(self):
        """Return the answer as string"""
        return (self.answer)
