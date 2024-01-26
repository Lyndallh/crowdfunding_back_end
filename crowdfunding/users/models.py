from django.db import models
from django.contrib.auth.models import AbstractUser
user = AbstractUser
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField( max_length=150, blank=True)
    email = models.EmailField( blank=True)
    pass

    def __str__(self):
        return self.username