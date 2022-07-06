from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# HTTP REQUEST


def home(request):
    return render(request, 'global/home.html', context={"name": 'Hermógenes Júnior'}, status=201)
    # HTTP RESPONSE


def home2(request):
    return render(request, 'recipes/home.html')
    # HTTP RESPONSE


def home3(request):
    return render(request, 'temp/temp.html')
    # HTTP RESPONSE


def page_sobre(request):
    return HttpResponse('PÁGINA SOBRE 2')
    # HTTP RESPONSE


def page_contato(request):
    return HttpResponse('PÁGINA CONTATO')
    # HTTP RESPONSE
