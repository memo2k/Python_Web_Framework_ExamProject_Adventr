from django import forms

from posts.models import Comment


class CommentForm(forms.Form):

    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':
                    'form-control rounded-2',
            }
        )
    )

