from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Comment, Post


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
        widgets = {
            "body": forms.Textarea(attrs={"rows": 4, "placeholder": "Write your comment..."}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "summary", "content", "cover_image", "categories", "status")
        widgets = {
            "content": CKEditor5Widget(config_name="default"),
            "categories": forms.CheckboxSelectMultiple(),
        }
