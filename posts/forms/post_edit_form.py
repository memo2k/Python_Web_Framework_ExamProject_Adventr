from django import forms
from posts.models import Post


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('location', 'description')

        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
