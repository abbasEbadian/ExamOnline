from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model, ModelStateFieldsCacheDescriptor
# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    question = models.ForeignKey("Qyestion")
    type = models.CharField(max_length=1, choices=[
        ("A", "Answer"),
        ("Q", "Question")
    ])

class Question(models.Model):
    Question_Type_Options = [
        ("M", 'تستی'),
        ("S", 'تشریحی'),
    ]
    text = models.TextField()
    type = models.CharField(
        max_length=1,
        choices=Question_Type_Options,
        default="multiple"
    )
    option1 = models.CharField(max_length=120)
    option2 = models.CharField(max_length=120)
    option3 = models.CharField(max_length=120)
    option4 = models.CharField(max_length=120)
    currect_answer = models.CharField(max_length=120)
    long_answer = models.TextField()
    exam = models.ForeignKey("Exam")
    
    def __str__(self):
        return self.question_text

class Exam(models.Model):
    title = models.CharField(max_length=120)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    duration = models.IntegerField()
    master = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    


