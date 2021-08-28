from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.views import APIView

import survey
from .models import Survey,User,Question,Answer
from .serializers import SurveySerializer,QuestionSerializer,AnswerSerializer,UserSerializer
from survey import serializers
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class SurveyGenericAPIView(mixins.ListModelMixin,generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= SurveySerializer
    queryset=Survey.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    def delete(self, request):
        return self.destroy(request)

class QuestionGenericAPIView(mixins.ListModelMixin,generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= QuestionSerializer
    queryset=Question.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        return self.list(request)

    def post(self, request):
        numPosts = Question.objects.filter(questionid=self.questionid).count()
        if numPosts > self.questionid.max_posts:
            raise ValidationError("one survey can have 10 qustions")
        return self.create(request)

class UserGenericAPIView(mixins.ListModelMixin,generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= UserSerializer
    queryset=User.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
class AnswerGenericAPIView(mixins.ListModelMixin,generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= AnswerSerializer
    queryset=Answer.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

@api_view(['GET','DELETE'])
def Survey_report(request,pk):
    try:
        survey=Survey.objects.get(pk=pk)
    except Survey.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method=="GET":
        serializer=SurveySerializer(survey)
        return Response(serializer.data)
    elif request.method=='DELETE':
        survey.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)