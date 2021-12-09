from django.shortcuts import render
from .models import Team
from cars.models import Car


# path('', 'views.home', name='home'),
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        # 'search_fields': search_fibody_style
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
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
