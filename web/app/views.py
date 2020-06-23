from django.shortcuts import render
from .models import Profile
from django.template import RequestContext


def custom_handler404(request, exception):
    print("404 error")
    context = {}
    response = render(request, 'app/404.html', context=context)
    response.status_code = 404
    return response


def custom_handler500(request):
    print("500 error")
    context = {}
    response = render(request, 'app/500.html', context=context)
    response.status_code = 500
    return response




def index(request):
    return render(request, 'app/index.html', {})


def about(request):
    return render(request, 'app/about.html', {})
