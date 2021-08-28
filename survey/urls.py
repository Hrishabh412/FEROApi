from django.shortcuts import render
from django.urls import path

# Create your views here.
from .views import  UserGenericAPIView, QuestionGenericAPIView, AnswerGenericAPIView, SurveyGenericAPIView, Survey_report

urlpatterns = [
    #path('student_details/<int:pk>', student_detail),
    path('user/', UserGenericAPIView.as_view()),
    path('question/', QuestionGenericAPIView.as_view()),
    path('answer/', AnswerGenericAPIView.as_view()),
    path('survey/', SurveyGenericAPIView.as_view()),
    path('report/<str:pk>/', Survey_report),
    ]