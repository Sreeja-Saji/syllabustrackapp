# Generated by Django 4.2.1 on 2023-07-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0007_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]