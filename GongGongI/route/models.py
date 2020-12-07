from django.db import models
from django.core.validators import MaxValueValidator
from user.models import Group, MemberList
from django.contrib.auth.models import User


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
    #     Post : Comment = 1 : N
    post = models.ForeignKey(Group, on_delete=models.CASCADE)  # ForeignKey: 다대 일 구조, Group 한개에 여러개의 댓글이 가능
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # on_delete=models.CASCADE: 사용자가 탈퇴했을때 삭제함.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 작성한 시간 추가
    updated_at = models.DateTimeField(auto_now=True)
