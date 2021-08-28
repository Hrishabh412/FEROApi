from rest_framework import serializers
from .models import Survey,User,Question,Answer


#serializers are just like Forms
class SurveySerializer(serializers.ModelSerializer):
    class Meta():
        model = Survey
        fields='__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields='__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Question
        fields='__all__'
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields='__all__'
