# Generated by Django 2.2 on 2021-02-15 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers_site_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='description',
            new_name='the_lesson_is',
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=70),
        ),
    ]
