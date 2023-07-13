from django.db import models

class User(models.Model):
    id = models.CharField(max_length=255)
    username = models.CharField(primary_key=True,max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()

