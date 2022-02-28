from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        fields = ['username', 'email', 'password1', 'password2']
        model = User

class PostForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'code', 'programming_language']
        model = Post

class CommentForm(forms.ModelForm):
    class Meta:
        fields = ['comment']
        model = Comment
