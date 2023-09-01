from django.db import models

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    company_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    is_administrator = models.BooleanField(default=False) 

    def __str__(self):
        return self.username
