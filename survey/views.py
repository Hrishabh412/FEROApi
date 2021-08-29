from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Survey, User, Question, Answer
from .serializers import (
    SurveySerializer, QuestionSerializer, AnswerSerializer,
    UserSerializer, SurveyOpenSerializer, SurveyReportSerializer
)


class SurveyGenericAPIView(ModelViewSet):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(methods=['GET'], detail=True, url_path='open')
    def open_survey_view(self, request, *args, **kwargs):
        survey_obj = self.get_object()
        return Response(SurveyOpenSerializer(instance=survey_obj).data)

    @action(methods=['GET'], detail=True, url_path='show-report')
    def show_survey_report_view(self, request, *args, **kwargs):
        survey_obj = self.get_object()
        return Response(SurveyReportSerializer(instance=survey_obj).data)


class QuestionGenericAPIView(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class UserGenericAPIView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class AnswerGenericAPIView(ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(methods=['POST'], detail=False, url_path='submit')
    def open_survey_view(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
