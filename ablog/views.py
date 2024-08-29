from django.shortcuts import render

from .forms import UniversityForm

def home(request):
    context = {'form': UniversityForm}
    return render(request, 'index.html', context)
