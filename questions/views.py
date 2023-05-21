from questions.serializers import QuestionRequestSerializer
from questions.models import Question
from questions.services import questions_add, make_response

from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class QuestionView(APIView):
    def post(self, request):
        serializer = QuestionRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        questions_num = serializer.validated_data['questions_num']

        response = requests.get(f"https://jservice.io/api/random?count={questions_num}")
        data = response.json()

        previous_question = Question.objects.last()


        questions_add(data)


        return Response(make_response(previous_question))
