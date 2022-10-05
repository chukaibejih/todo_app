from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from todo.models import TodoItem

UserModel = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField() # modified the default sign up page and added an email field
    username = forms.CharField()

    class Meta:
        model = UserModel
        fields = ["email", "username", "password1", "password2"]


class TodoForm(forms.ModelForm):
    
    class Meta:
        fields = "__all__"