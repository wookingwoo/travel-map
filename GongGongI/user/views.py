from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView
from django.views.generic import ListView
from .models import Group, MemberList, Profile, FriendRequest
from .forms import GroupForm, ProfileForm
from .decorators import profile_ownership_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

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


def searchResult(request):
	users = None
	query = None
	button_status = 'none'

	if 'q' in request.GET:
		query = request.GET.get('q')
		result = User.objects.filter(email=query)
		users = result.exclude(id=request.user.id)

		if users.exists():
			p=users[0].profile
			friends=p.friends.all()
	
			#친구아님
			if p not in request.user.profile.friends.all():
				button_status = 'not_friend'
				#만약에 이 친구한테 요청을 보냈으면
				#버튼 상태 친구요청중
				if len(FriendRequest.objects.filter(from_user=request.user).filter(to_user=p.user)) == 1:
					button_status = 'friend_request_sent'


	context = {
		'query':query,
		'users':users,
		'button_status': button_status,
	}
		
	return render(request, 'user/friend.html', context)


def send_friend_request(request, id):
	if request.user.is_authenticated:
		user = get_object_or_404(User, pk=id)
		frequest, created = FriendRequest.objects.get_or_create(
			from_user=request.user,
			to_user=user)
		return HttpResponseRedirect('/user')

def cancel_friend_request(request, id):
	if request.user.is_authenticated:
		user = get_object_or_404(User, id=id)
		frequest = FriendRequest.objects.filter(
			from_user=request.user,
			to_user=user).first()
		frequest.delete()
		return HttpResponseRedirect('/user')
