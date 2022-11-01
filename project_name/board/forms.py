from django import forms
from .models import Post, Answer, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["category", "title", "content", "tags", "image"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
