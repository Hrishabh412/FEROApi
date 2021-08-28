from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    UserGenericAPIView, QuestionGenericAPIView, AnswerGenericAPIView,
    SurveyGenericAPIView
)

router = SimpleRouter()
router.register('user', UserGenericAPIView, 'user')
router.register('question', QuestionGenericAPIView, 'question')
router.register('answer', AnswerGenericAPIView, 'answer')
router.register('survey', SurveyGenericAPIView, 'survey')

urlpatterns = [
    path('', include(router.urls))
]
