# Generated by Django 2.2 on 2021-02-21 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students_site_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelateAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('question_grade', models.FloatField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='students_site_api.StudentProgress')),
            ],
        ),
    ]
