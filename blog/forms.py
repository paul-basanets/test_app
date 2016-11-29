from django import forms

from blog.models import Post


class PostForm(forms.Form):
    title = forms.CharField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
