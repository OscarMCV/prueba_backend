from django.db import models

import uuid


class CreateClass(models.Model):
    """Create a scholar Class which contain the courses"""
    id = id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")

    def __str__(self):
        """Return string representation for the school Class"""
        return self.name


class CreateCourse(models.Model):
    """Create a course which cointain the lessons"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_class = models.ForeignKey(CreateClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True,)
    level = models.IntegerField()

    def __str__(self):
        """Return string representation for the Course"""
        return self.name


class CreateLesson(models.Model):
    """Create a lesson which contain the questions"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(CreateCourse, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True,)
    level = models.IntegerField()

    def __str__(self):
        """Return string representation for a Lesson"""
        return self.name


class CreateQuestion(models.Model):
    """Create a question which contains the kind of question and the answers"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uploaded = models.DateTimeField(auto_now_add=True)
    lesson = models.ForeignKey(CreateLesson, on_delete=models.CASCADE)
    question = models.CharField(max_length=300, unique=True,)
    level = models.IntegerField()
    number_correct_answers = models.IntegerField()
    number_bad_answers = models.IntegerField()
    all_correctanswers = models.CharField(max_length=300, unique=True)
    all_badanswers = models.CharField(max_length=300, unique=True)
    list_of_choices = models.CharField(max_length=300, unique=True)
    KIND_OF_QUESTION = [('BOOLEAN', 'Boolean'),
                        ('MULTIPLECHOICE1', 'Multiple choice where only one answer is correct'),
                        ('MULTIPLECHOICE2', 'Multiple choice where more than one answer is correct'),
                        ('MULTIPLECHOICE3', 'Multiple choice where more than one answer is correct and all of them must be answered correctly'),
                        ]
    type_question = models.CharField(max_length=120, choices=KIND_OF_QUESTION, default='BOOLEAN')

    class Meta:
        ordering = ['uploaded']

    def __str__(self):
        """Return the question as string"""
        return self.question
