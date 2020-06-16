from django.shortcuts import render
from .models import Profile


def index(request):
    return render(request, 'app/index.html', {})


def about(request):
    return render(request, 'app/about.html', {})
