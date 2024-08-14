from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Registration(models.Model):
    first_name=models.CharField(max_length=50 )
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    # User.email = models.EmailField(_("email address"), blank=True, null=True, unique=True)
    # User._meta.get_field('email')._unique = True
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


