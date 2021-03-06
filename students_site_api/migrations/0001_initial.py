# Generated by Django 2.2 on 2021-02-17 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseAchivments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achivment_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LessonAchivments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProgress',
            fields=[
                ('name', models.EmailField(max_length=254, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Related_Lesson',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('lesson_name', models.CharField(max_length=100, unique=True)),
                ('student', models.ManyToManyField(through='students_site_api.LessonAchivments', to='students_site_api.StudentProgress')),
            ],
        ),
        migrations.CreateModel(
            name='Related_Course',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(max_length=100, unique=True)),
                ('student', models.ManyToManyField(through='students_site_api.CourseAchivments', to='students_site_api.StudentProgress')),
            ],
        ),
        migrations.AddField(
            model_name='lessonachivments',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students_site_api.Related_Lesson'),
        ),
        migrations.AddField(
            model_name='lessonachivments',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_achivments', to='students_site_api.StudentProgress'),
        ),
        migrations.AddField(
            model_name='courseachivments',
            name='curse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students_site_api.Related_Course'),
        ),
        migrations.AddField(
            model_name='courseachivments',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_achivments', to='students_site_api.StudentProgress'),
        ),
    ]
