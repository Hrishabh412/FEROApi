# Generated by Django 3.1.7 on 2021-08-27 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('surveyid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('surveystart', models.DateTimeField()),
                ('surveyend', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questionid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('surveyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='survey.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answerid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('answer', models.TextField()),
                ('questionid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='survey.question')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='survey.user')),
            ],
        ),
    ]
