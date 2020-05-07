from django import forms
from .models import ArticleModel


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


class ArticleCreateForm(forms.ModelForm):
    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    content_short = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "short",
                "rows": 20,
                'cols': 120
            }
        )
    )
    content_full = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "full",
                "rows": 20,
                'cols': 120
            }
        )
    )

    image = forms.ImageField(label='Image', required=False, widget=forms.FileInput(
        attrs={
            # "class": "myButton"
        }))

    class Meta:
        model = ArticleModel
        fields = [
            'author',
            'title',
            'content_short',
            'content_full'
        ]
        # exclude = ('author',)
        # widgets = {'author': forms.HiddenInput()}


class CommentForm(forms.Form):
    author = forms.CharField(label='', required=True, max_length=60,
                             widget=forms.TextInput(attrs={
                                 "class": "form-control",
                                 "placeholder": "Your Name",
                                 "name": "author",
                             }))
    comment_text = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!",
            "name": "comment_text",
            "rows": 5,
        }))
