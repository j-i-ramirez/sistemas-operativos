from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True)
    
    class Meta:
        db_table = 'auth_user'