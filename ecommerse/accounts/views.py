from django.shortcuts import render, redirect
from .form import RegistrationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def registration_from(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    print(form.errors)
    if form.is_valid():
      user = form.save()

      # email = form.cleaned_data.get('email')
      # password = form.cleaned_data.get('password')

      # You already have the user when you save the form, so you don't need to call authenticate since you already provide the backend when calling login()
      # user_authenticate = authenticate(email = email, password = password)

      login(request,user)
      return redirect('home')
    else:
      form = RegistrationForm()
      return render(request, 'accounts/regiter.html', {'form': form })
  else:
    form = RegistrationForm()
    return render(request, 'accounts/regiter.html', {'form': form })