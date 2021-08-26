from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """Use to call the form for the comments"""
    class Meta:
        model = Comment
        fields = ('content',)