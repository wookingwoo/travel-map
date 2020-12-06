from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leader')
    image = models.ImageField(upload_to='groupimage/',null=True)
    title = models.CharField(max_length=200)
    introduction = models.TextField()
    member = models.ManyToManyField(User, through='MemberList')

    def __str__(self):
        return self.title


class MemberList(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['group','user']] 