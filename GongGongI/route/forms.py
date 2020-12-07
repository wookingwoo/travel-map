from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message'] # models.py에서 post, text, author 3가지가 있지만 post는 글을 가져오고, author은 로그인 계정 가져오면 되니까 text만 가져옴. text가 댓글 내용.