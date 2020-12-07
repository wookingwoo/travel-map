from django.contrib import admin

# Register your models here.
from .models import Group,MemberList,Profile

admin.site.register(Group)
admin.site.register(MemberList)
admin.site.register(Profile)