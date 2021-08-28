from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

class Survey(models.Model):
    surveyid = models.CharField(primary_key=True, max_length=5)
    surveystart = models.DateTimeField()
    surveyend = models.DateTimeField()

    def __str__(self):
        return self.surveyid


class Question(models.Model):
    questionid = models.CharField(primary_key=True, max_length=5)
    surveyid = models.ForeignKey(Survey, related_name='question',
                                 on_delete=CASCADE)
    question = models.TextField()

    def __str__(self):
        return self.questionid


class User(models.Model):
    userid = models.CharField(primary_key=True, max_length=5)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.userid


class Answer(models.Model):
    answerid = models.CharField(primary_key=True, max_length=5)
    userid = models.ForeignKey(User, related_name='answer', on_delete=CASCADE)
    questionid = models.ForeignKey(Question, related_name='answer',
                                   on_delete=CASCADE)
    answer = models.TextField()

    class Meta:
        unique_together = ('userid', 'questionid')

    def __str__(self):
        return self.answerid
