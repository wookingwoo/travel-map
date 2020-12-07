from django.db import models
from django.core.validators import MaxValueValidator
from user.models import Group, MemberList
from django.contrib.auth.models import User
from django.urls import reverse


class Day(models.Model):
    name = models.CharField(max_length=15, unique=True)
    description = models.TextField(blank=True)

    # group = models.ForeignKey(Group, on_delete=models.CASCADE) #효원님이 개발한 그룹모델과 연결할 계획입니다.

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=15, unique=True)
    description = models.TextField(blank=True)

    latitude = models.FloatField()
    longitude = models.FloatField()

    day = models.ForeignKey(Day, on_delete=models.CASCADE, blank=True, null=True)

    # order = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(30)])

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Group, on_delete=models.CASCADE)  # Post : Comment = 1 : N
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자 탈퇴시 삭제함.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']  # 역순 정렬

    def get_edit_url(self):
        return reverse('route_app:comment_edit', args=[self.post.pk, self.pk])
        # return reverse('route_app:comment_edit', args=[1, self.pk])


