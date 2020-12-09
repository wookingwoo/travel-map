from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save

User._meta.get_field('email')._unique = True

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


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/',null=True,default="profile/user.png")
    message=models.CharField(max_length=100,null=True,default="프로필을 입력해주세요")
    friends = models.ManyToManyField("Profile", blank=True)

    def __str__(self):
        return str(self.user.username)



def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=User)



class FriendRequest(models.Model):
	to_user = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='to_user')
	from_user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='from_user')
	timestamp = models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return "From {}, to {}".format(self.from_user.username, self.to_user.username)
