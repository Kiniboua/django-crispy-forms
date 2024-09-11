from django.shortcuts import render

from .forms import CustomUserCreationForm

def home(request):
    context = {'form': CustomUserCreationForm()}
    return render(request, 'index.html', context)
