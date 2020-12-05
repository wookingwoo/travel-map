from django.db import models
from django.core.validators import MaxValueValidator


class Day(models.Model):
    name = models.CharField(max_length=15, unique=True)
    description = models.TextField(blank=True)
    # group = models.ForeignKey(Group, on_delete=models.CASCADE) #효원님이 개발한 그룹모델과 연결할 계획입니다.


class Place(models.Model):
    name = models.CharField(max_length=15, unique=True)
    description = models.TextField(blank=True)

    latitude = models.FloatField()
    longitude = models.FloatField()

    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    # order = models.IntegerField(max_length=2, unique=True)
    order = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(30)])
