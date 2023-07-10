from django import forms
from .models import Post, Comment


class PostUpdateCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)


class CommentCreatForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReplyCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)





