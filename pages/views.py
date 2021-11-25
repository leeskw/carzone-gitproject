from django.shortcuts import render
from django.http import HttpResponse


# path('', 'views.home', name='home'),
def home(request):
    return render(request, 'pages/home.html')
