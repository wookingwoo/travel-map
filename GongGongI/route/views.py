from django.shortcuts import render
from .models import Day, Place, Comment

from user.models import Group, MemberList
from .forms import CommentForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    groups = Group.objects.all()
    groupsCount = Group.objects.count()

    days = Day.objects.all()
    daysCount = Day.objects.count()

    places = Place.objects.all()
    placesCount = Place.objects.count()
    
    comments = Comment.objects.all()


    return render(request, 'map/index.html',
                  {

                      "groups": groups,
                      "groupsCount": groupsCount,
                      'wjh_test': 'wjh_test20201204',
                      'days': days,
                      'daysCount': daysCount,
                      'places': places,
                      'placesCount': placesCount,
                      'comments':comments,

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


@login_required
def comment_new(request, post_pk):
    post = get_object_or_404(Group, pk=post_pk)
    # post = get_object_or_404(Group)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("/route/", post.pk)

    else:
        form = CommentForm()
    return render(request, 'map/comment_form.html', {
        'form': form,
    })
