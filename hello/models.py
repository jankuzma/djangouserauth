from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    year = models.IntegerField()

class Genre(models.Model):
    name = models.CharField(max_length=64)

class Producer(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    year = models.IntegerField()
