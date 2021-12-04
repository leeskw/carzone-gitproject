from django.shortcuts import render
from .models import Team
from cars.models import Car


# path('', 'views.home', name='home'),
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
    }
    return render(request, 'pages/home.html', context)


# path('about', views.about, name='about'),
def about(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', context)


# path('services', views.about, name='services'),
def services(request):
    return render(request, 'pages/services.html')


# path('contact', views.contact name='contact'),
def contact(request):
    return render(request, 'pages/contact.html')
