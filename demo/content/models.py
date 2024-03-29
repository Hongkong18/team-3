from django.db import models
from polymorphic.models import PolymorphicModel


# Create your models here.
class User(models.Model):
   username = models.CharField(max_length=200)  # given name
   email = models.EmailField(max_length=254, unique=True)
   password = models.CharField(max_length=200)
   contact = models.CharField(max_length=20, blank=True)
   is_admin = models.BooleanField(default=False)


class Volunteer(PolymorphicModel):
   user = models.OneToOneField(User, on_delete=models.CASCADE,)
   skills = models.CharField(max_length=500)  # comeback to it
   hours_available_per_week = models.PositiveIntegerField()


class Donor(PolymorphicModel):
   user = models.OneToOneField(User, on_delete=models.CASCADE,)
   donated_amount = models.PositiveIntegerField()


class Event(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=200)
   in_charge = models.OneToOneField(User, on_delete=models.CASCADE,)
   venue = models.CharField(max_length=200)
   skills_needed = models.CharField(max_length=500)
   date = models.DateField()
   time_start = models.TimeField()
   time_end = models.TimeField()

