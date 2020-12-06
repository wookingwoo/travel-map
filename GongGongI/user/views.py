from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import ListView
from .models import Group, MemberList
from .forms import GroupForm

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


class GroupView(ListView):
    model = Group
    context_object_name = "group_list"
    template_name = 'user/group.html'

    def get_queryset(self):
        group_list=MemberList.objects.filter(user=self.request.user)
        return group_list