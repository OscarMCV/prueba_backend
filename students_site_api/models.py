from django.db import models
import uuid


class StudenProgress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.EmailField()


class LessonAchivment(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    student = models.ForeignKey(StudenProgress, related_name='Lessons', on_delete=models.CASCADE)
    grade = models.FloatField()


class CourseAchivment(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    course =  models.ForeignKey(Course, on_delete=models.=ACCSCS)
    student = models.ForeignKey(StudenProgress, related_name='Courses', on_delete=models.CASCADE)
    grade = models.FloatField()

