from django.db import models

import uuid


KIND_OF_QUESTION = [('BOOLEAN', 'Boolean'),
                    ('MULTIPLECHOICE1', 'Multiple choice where only one answer is correct'),
                    ('MULTIPLECHOICE2', 'Multiple choice where more than one answer is correct'),
                    ('MULTIPLECHOICE3', 'Multiple choice where more than one answer is correct and all of them must be answered correctly'),
                    ]


class Course(models.Model):
    """Create a course which cointain the lessons"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #Id is a uudid field which is the primary key for every Course
    name = models.CharField(max_length=120, unique=True,)

    def __str__(self):
        """Return string representation for the Course"""
        return self.name


class Lesson(models.Model):
    """Create a lesson which contain the questions"""
    #Id is a uudid field which is the primary key for every Lesson
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True,)
    uploaded = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField()
    description = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        """Return string representation for a Lesson"""
        return self.name


class Question(models.Model):
    """Create a question which contains the kind of question and the answers"""
    lesson = models.ForeignKey(Lesson, related_name='questions', on_delete=models.CASCADE)
    #The related name will be handle has a field in the model seralizer of the lesson
    order = models.IntegerField()
    question = models.CharField(max_length=300, unique=True,)
    number_correct_answers = models.IntegerField()
    number_bad_answers = models.IntegerField()
    score = models.IntegerField(default=1)
    all_correctanswers = models.CharField(max_length=300, unique=True)
    all_badanswers = models.CharField(max_length=300, unique=True)
    list_of_choices = models.CharField(max_length=300, unique=True)
    type_question = models.CharField(max_length=120, choices=KIND_OF_QUESTION, default='BOOLEAN')

    class Meta:
        unique_together = ['order', 'lesson', ]
        #Cannot have a question two lessons or two  similar number of order
        ordering = ['order']
        #When is required, the questions order by the nomber of order

    def __str__(self):
        """Return the question as string"""
        return '%d: %s ' % (self.order, self.question)
        #Return in a python form the data. %d is for decimal and %s is for a string
