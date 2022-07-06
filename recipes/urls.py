from django.urls import path
from recipes.views import home, home2, home3, page_contato, page_sobre

urlpatterns = [
    path('', home2),
    path('base/', home),
    path('temp/', home3),
    path('sobre/', page_sobre),
    path('contato/', page_contato),
]
