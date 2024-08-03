from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email