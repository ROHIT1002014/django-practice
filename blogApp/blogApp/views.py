from django.shortcuts import render
from .forms import ContactForm


def contact_page(request):
  # print(request.POST)

  form = ContactForm(request.POST or None)
  if form.is_valid():
    print(form.cleaned_data)

    form = ContactForm() # this code is re-initialize the form
  context = {
    "title" : "Contect Us",
    "form" : form
  }
  return render(request, "form.html", context)