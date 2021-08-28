from rest_framework import serializers
from django.utils import timezone

from .models import Survey, User, Question, Answer


# serializers are just like Forms
class SurveySerializer(serializers.ModelSerializer):
    class Meta():
        model = Survey
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        surveyid = validated_data.get('surveyid')
        survey = Survey.objects.filter(surveyid=surveyid).last()
        if survey and survey.question.count() > 10:
            raise serializers.ValidationError('only 10 questions allowed')

        return super().create(validated_data)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

    def create(self, validated_data):
        questionid = validated_data.get('questionid')
        question = Question.objects.filter(questionid=questionid).last()
        if question:
            survey = Survey.objects.filter(surveyid=question.surveyid).last()
            if survey and survey.surveyend < timezone.now():
                raise serializers.ValidationError('Survey expired!')

        return super().create(validated_data)


class SurveyOpenSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Survey
        fields = '__all__'

    def get_questions(self, obj):
        return list(QuestionSerializer(obj.question.all(), many=True).data)


class QuestionAnswerSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    def get_answers(self, obj):
        return list(AnswerSerializer(obj.answer.all(), many=True).data)


class SurveyReportSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Survey
        fields = '__all__'

    def get_questions(self, obj):
        return QuestionAnswerSerializer(obj.question.all(), many=True).data
