from django.shortcuts import render


# path('', views.cars, name='cars'),
def cars(request):
    return render(request, 'cars/cars.html')
