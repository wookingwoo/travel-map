from django.urls import path

from .views import (
    GroupView, 
    GroupCreateView, 
    ProfileCreateView, 
    ProfileUpdateView,
)

from .views import(
    searchResult, 
	send_friend_request, 
	cancel_friend_request,
    accept_friend_request,
    delete_friend_request,
    profile_view
)

from django.views.generic import TemplateView

app_name = "user"

urlpatterns = [   
    path('friendlist/', searchResult, name='search'),
    path('grouplist/',GroupView.as_view(), name='grouplist'),
    path('create/',GroupCreateView.as_view(),name='create'),

    path('profile_create/',ProfileCreateView.as_view(),name='profile_create'),
    path('profile_update/<int:pk>',ProfileUpdateView.as_view(),name='profile_update'),
    path('mypage/<int:pk>',profile_view,name='mypage'),
    
    path('friend-request/send/<int:id>/', send_friend_request, name='send_friend_request'),
    path('friend-request/cancel/<int:id>/', cancel_friend_request, name='cancel_friend_request'),
    path('friend-request/accept/<int:id>/', accept_friend_request, name='accept_friend_request'),
    path('friend-request/delete/<int:id>/', delete_friend_request, name='delete_friend_request'),


]