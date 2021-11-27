from django.shortcuts import render


# path('', 'views.home', name='home'),
def home(request):
    return render(request, 'pages/home.html')


# path('about', views.about, name='about'),
def about(request):
    return render(request, 'pages/about.html')


# path('services', views.about, name='services'),
def services(request):
    return render(request, 'pages/services.html')


# path('contact', views.contact name='contact'),
def contact(request):
    return render(request, 'pages/contact.html')
