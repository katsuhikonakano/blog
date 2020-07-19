from django import forms
from .models import Post
from django.forms import TextInput, Textarea, FileInput, Select, SelectMultiple
from django.contrib.auth.forms import AuthenticationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "thumnail", "image", "category", "tag"]
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'タイトル'}),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': '本文',
                'cols': 80, 'rows': 15}),
            'thumnail': FileInput(attrs={
                'class': 'form-control-file'}),
            'image': FileInput(attrs={
                'class': 'form-control-file'}),
            'category': Select(attrs={
                'class': 'form-control'}),
            'tag': SelectMultiple(attrs={
                'class': 'form-control'
            })
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields.values():
            fields.widget.attrs['class'] = 'form-control'
            fields.widget.attrs['placeholder']= fields.label