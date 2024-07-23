from .models import Post, Comment, User, Mark
from django.forms import ModelForm, forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'date', 'author']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'text', 'date']


class RegForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','telegram_chat_id','email','password']
