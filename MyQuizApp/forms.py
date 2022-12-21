from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from MyQuizApp.models import *

class userform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']


class AddQuestionForm(ModelForm):
     class Meta:
         model=QuestionsModel
         fields="__all__"
