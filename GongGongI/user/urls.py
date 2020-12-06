from django.urls import path

from .views import GroupView, GroupCreateView

app_name = "user"

urlpatterns = [
    path('grouplist/',GroupView.as_view(), name='grouplist'),
    path('create/',GroupCreateView.as_view(),name='create'),
]