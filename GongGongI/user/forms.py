from django.forms import ModelForm
from .models import Group,Profile

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields=['image','title','introduction']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields=['image','message']

