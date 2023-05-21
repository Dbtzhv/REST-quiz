from questions.models import Question

import requests

def questions_add(data):
        for i in range(len(data)):
            question_text = data[i]['question']

            while Question.objects.filter(question_text=question_text).exists():
                response = requests.get("https://jservice.io/api/random?count=1")
                new_data = response.json()
                question_text = new_data[0]['question']

            Question.objects.create(question_text=question_text, answer_text=data[i]['answer'],
                                    creation_date=data[i]['created_at'])



def make_response(previous_question):
    if previous_question:
        response_data = {
            "id": previous_question.id,
            "question_text": previous_question.question_text,
            "answer_text": previous_question.answer_text,
            "creation_date": previous_question.creation_date
        }
    else:
        response_data = {}

    return response_data
