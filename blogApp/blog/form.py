from django import forms
from .models import BlogPost

# it was normal form
class BlogPostForm(forms.Form):
  title = forms.CharField()
  slug = forms.SlugField()
  content = forms.CharField(widget=forms.Textarea)

  # write validation of fields in the form
  def clean_title(self, *args, **kwargs):
    title = self.cleaned_data.get('title')
    qs = BlogPost.objects.filter(title__iexact=title) # if this field is already contain unique key in models class then we don't need this field and _iexact is used for case sensitive of words
    print(qs.exists())
    if qs.exists():
      raise forms.ValidationError("This title is already exist. Please try again.")
    return title

# below is model form which is due to model in models
class BlogPostModelForm(forms.ModelForm):
  class Meta:
    model = BlogPost
    fields = ['title', 'slug', 'content']

  # commented below code bcs we have to make update form workable

  # write validation of fields in the form
  # def clean_title(self, *args, **kwargs):
  #   title = self.cleaned_data.get('title')
  #   qs = BlogPost.objects.filter(title=title)

    # if qs.exists():
    #   raise forms.ValidationError("This title is already exist. Please try again.")
    # return title