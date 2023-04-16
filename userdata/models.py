from django.db import models
from django.contrib.auth.models import User

class userData(models.Model):
    name = models.CharField(max_length=50 (attrs=={'required': 'True'}))
    email = models.CharField(max_length=50 (attrs=={'required': 'True'}))
    password = models.CharField(max_length=50)

# Create your models here.
