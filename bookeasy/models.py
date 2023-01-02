from email.policy import default
from re import U
from statistics import mode
from unittest.util import _MAX_LENGTH
from django import forms
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class movie_User(models.Model):
    django_user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.IntegerField(default=0)

class movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    duration = models.IntegerField()
    is_movie = models.BooleanField()
    amount = models.IntegerField()

class locations(models.Model):
    city = models.CharField(max_length=100)

class cinema_hall(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class seats(models.Model):
    seat_number = models.CharField(max_length=100)
    cinema_hall_id = models.ForeignKey(cinema_hall, on_delete=models.CASCADE)

# class movie_seat_mapping(models.Model):
#     start_time = models.IntegerField()
#     amount = models.IntegerField()
#     seat_id = models.ForeignKey(seats, on_delete=models.CASCADE)
#     movie_id = models.ForeignKey(movie, on_delete=models.CASCADE)

class reservation(models.Model):
    email = models.CharField(max_length=100)
    employee_id = models.ForeignKey(movie_User, on_delete=models.CASCADE)
    movie_seat_id = models.ForeignKey(movie_seat_mapping, on_delete=models.CASCADE)

class order(models.Model):
    quantity = models.IntegerField()
    total_amount = models.IntegerField()
    discount = models.IntegerField()
    movies = models.ForeignKey(movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(movie_User, on_delete=models.CASCADE)

class transactions(models.Model):
    card_number = models.IntegerField()
    name_on_card = models.CharField(max_length=100)
    order = models.ForeignKey(order, on_delete=models.CASCADE)





