from rest_framework import serializers


class QuestionRequestSerializer(serializers.Serializer):
    questions_num = serializers.IntegerField()
