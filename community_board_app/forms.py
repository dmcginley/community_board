from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category','status']
        

        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your post...'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
        labels = {
            'content': 'Comment'
        }

        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your comment...'})
        }
