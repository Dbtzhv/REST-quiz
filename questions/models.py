from django.db import models


class Question(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField()
    creation_date = models.DateTimeField()

    def __str__(self):
        return self.question_text
