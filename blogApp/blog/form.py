from django import forms
from .models import BlogPost

# it was normal form
class BlogPostForm(forms.Form):
  title = forms.CharField()
  slug = forms.SlugField()
  content = forms.CharField(widget=forms.Textarea)

