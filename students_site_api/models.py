from django.db import models
import uuid

#For more information about the logic of this database:
#https://docs.djangoproject.com/en/2.2/topics/db/models/#intermediary-manytomany


class StudentProgress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.EmailField()
    
    def __str__(self):
        return self.name


class Related_Course(models.Model):
    id = models.CharField(primary_key=True, unique=True)
    #It is a CahrField because the plan is will be equal to an existing lesson ID
    course_name = models.CharField(unique=True)
    student = models.ManyToManyField(StudentProgress, through='CourseAchivments')

    def __str__(self):
        return self.id


class Related_lesson(models.Model):
    id = models.CharField(primary_key=True, unique=True)
    #It is a CahrField because the plan is will be equal to an existing lesson ID
    Lesson_name = models.CharField(unique=True)
    student = models.ManyToManyField(StudentProgress, through='LessonAchivments')

    def __str__(self):
        return self.Lesson_name


class CourseAchivments(models.Model):
    student = models.ForeignKey(StudentProgress, on_delete=models.CASCADE)
    curse = models.ForeignKey(Related_Course, on_delete=models.CASCADE)
    achivment_date = models.DateTimeField(auto_now=True)


class LessonAchivments(models.Model):
    student = models.ForeignKey(StudentProgress, on_delete=models.CASCADE)
    lessons = models.ForeignKey(StudentProgress, on_delete=models.CASCADE)
    grade = models.FloatField()
