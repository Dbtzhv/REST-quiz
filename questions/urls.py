from django.urls import path
from .views import QuestionView

app_name = 'questions'

urlpatterns = [
    path('questions/', QuestionView.as_view()),
]
