from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView
from django.views.generic import ListView
from .models import Group, MemberList, Profile
from .forms import GroupForm, ProfileForm
from .decorators import profile_ownership_required

from django.urls import reverse_lazy

# Create your views here.

@method_decorator(login_required, name="dispatch")
class GroupCreateView(CreateView):
    model=Group
    context_object_name='target_group'
    form_class= GroupForm
    success_url = reverse_lazy('user:grouplist')
    template_name = 'user/create.html'

    def form_valid(self,form):
        temp_group=form.save(commit=False)
        temp_group.leader = self.request.user
        temp_group.save()
        temp_group.member.add(self.request.user)
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class ProfileCreateView(CreateView):
    model=Profile
    context_object_name='target_profile'
    form_class= ProfileForm
    success_url = reverse_lazy('user:grouplist')
    template_name = 'user/profile_create.html'

    def form_valid(self,form):
        temp_profile=form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model=Profile
    context_object_name='target_profile'
    form_class= ProfileForm
    success_url = reverse_lazy('user:grouplist')
    template_name = 'user/profile_update.html'



class GroupView(ListView):
    model = Group
    context_object_name = "group_list"
    template_name = 'user/group.html'

    def get_queryset(self):
        group_list=MemberList.objects.filter(user=self.request.user)
        return group_list