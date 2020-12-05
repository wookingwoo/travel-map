from django.shortcuts import render
from .models import Day, Place


def index(request):
    days = Day.objects.all()

    places = Place.objects.all()

    return render(request, 'map/index.html',
                  {
                      'wjh_test': 'wjh_test20201204',
                      'days': days,
                      'places': places,
                  })


def map(request):
    return render(
        request,
        'map/map.html',
        {
            'wjh_test': 'wjh_test20201204',
        }
    )


def navbar(request):
    return render(
        request,
        'map/navbar.html',
    )
