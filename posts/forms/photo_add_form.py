from django import forms
from posts.models import Post


class AddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
