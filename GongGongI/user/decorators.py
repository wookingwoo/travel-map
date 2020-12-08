from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect

from .models import Profile


def profile_ownership_required(func):
    def decorated(request,*args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request,*args, **kwargs)
    return decorated


def profile_required(func):
    def decorated(request,*args, **kwargs):
        profile=Profile.objects.filter(user_id=request.user.id)
        if not profile.exists():
            return HttpResponseRedirect('/user/profile_create')
        return func(request,*args, **kwargs)
    return decorated