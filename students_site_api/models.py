from django.db import models
import uuid

#For more information about the logic of this database:
#https://docs.djangoproject.com/en/2.2/topics/db/models/#intermediary-manytomany


class StudentProgress(models.Model):
    name = models.EmailField(primary_key=True)

    def __str__(self):
        return self.name


class Related_Course(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=100)
    #It is a CharField because the plan is will be equal to an existing lesson ID
    course_name = models.CharField(unique=True, max_length=100)
    student = models.ManyToManyField(StudentProgress, through='CourseAchivments')

    def __str__(self):
        return self.course_name


class Related_Lesson(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=100)
    #It is a CharField because the plan is will be equal to an existing lesson ID
    lesson_name = models.CharField(unique=True, max_length=100)
    student = models.ManyToManyField(StudentProgress, through='LessonAchivments')

    def __str__(self):
        return self.lesson_name


class CourseAchivments(models.Model):
    #Will handle a register when a course is finished
    student = models.ForeignKey(StudentProgress, related_name='course_achivments', on_delete=models.CASCADE)
    curse = models.ForeignKey(Related_Course, on_delete=models.CASCADE)
    achivment_date = models.DateTimeField(auto_now=True)


class LessonAchivments(models.Model):
    #will handle a register when a Lesson is finished
    student = models.ForeignKey(StudentProgress, related_name='lesson_achivments', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Related_Lesson, on_delete=models.CASCADE)
    grade = models.FloatField()
    status = models.BooleanField(default=False)


class RelateAnswers(models.Model):
    #Create answers to storage
    student = models.ForeignKey(StudentProgress, related_name="answers", on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    question_grade = models.FloatField(max_length=100)
    #this model object is deleted when a lesson y finishedrs", o