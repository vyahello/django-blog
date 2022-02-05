from blog.models import Comment, Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'authors', 'title', 'text'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(
                attrs={'class': 'editable medium-editor-textarea postcontent'}
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'author', 'text'
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(
                attrs={'class': 'editable medium-editor-textarea'}
            ),
        }
