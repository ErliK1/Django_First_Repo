# Generated by Django 4.2.3 on 2023-07-13 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_alter_student_student_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentTakesCourse',
        ),
    ]
