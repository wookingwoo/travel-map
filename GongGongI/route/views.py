from django.shortcuts import render
from .models import Day, Place
from user.models import Group, MemberList



def index(request):
    
    groups = Group.objects.all()
    groupsCount = Group.objects.count()
    
    days = Day.objects.all()
    daysCount = Day.objects.count()

    places = Place.objects.all()
    placesCount = Place.objects.count()
    
    

    return render(request, 'map/index.html',
                  {
                      
                      "groups":groups,
                      "groupsCount":groupsCount, 
                      'wjh_test': 'wjh_test20201204',
                      'days': days,
                      'daysCount': daysCount,
                      'places': places,
                      'placesCount': placesCount,

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





from django.shortcuts import render, get_object_or_404, redirect
def addPlace(request):
    place = Place()
    place.name = request.GET['name']
    place.description = request.GET['description']
    
    place.latitude = request.GET['latitude']
    place.longitude = request.GET['longitude']
    
#     day 추가하기
    # day = models.ForeignKey(Day, on_delete=models.CASCADE)

    # place.order = request.GET['order']
    place.order = 1


        
    place.save()
    

    return redirect('/route/')


