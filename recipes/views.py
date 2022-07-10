from django.shortcuts import render

# Create your views here.

# HTTP REQUEST


def home(request):
    return render(request, 'recipes/pages/home.html', context={"name": 'Hermógenes Júnior'}, status=201)
    # HTTP RESPONSE
