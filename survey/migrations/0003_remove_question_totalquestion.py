# Generated by Django 3.1.7 on 2021-08-27 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_question_totalquestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='totalquestion',
        ),
    ]
