from django.urls import path

from .views import GroupView, GroupCreateView, ProfileCreateView, ProfileUpdateView

from django.views.generic import TemplateView

app_name = "user"

urlpatterns = [   
    path('',TemplateView.as_view(template_name="user/friend.html")),
    path('grouplist/',GroupView.as_view(), name='grouplist'),
    path('create/',GroupCreateView.as_view(),name='create'),
    path('profile_create/',ProfileCreateView.as_view(),name='profile_create'),
    path('profile_update/<int:pk>',ProfileUpdateView.as_view(),name='profile_update')
]