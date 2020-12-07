from django.urls import path, include
from . import views
from django.conf.urls import url

app_name = 'route_app'

urlpatterns = [

    path('', views.index, name='routeurl'),
    path('map/', views.map),
    path('navbar/', views.navbar),
    path('addPlace/', views.addPlace, name='placesave'),

    # path('comment/new/', views.comment_new, name='comment_new'),

    url(r'^(?P<post_pk>\d+)/comment/new$', views.comment_new, name='comment_new'),
    url(r'^(?P<post_pk>\d+)/comment/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),

]
