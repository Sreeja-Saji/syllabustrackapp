# Generated by Django 4.2.1 on 2023-07-03 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0005_coursesyllabus'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coursesyllabus',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='syllabus',
        ),
    ]