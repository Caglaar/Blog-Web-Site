from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50,null =True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastsurname = models.CharField(max_length=50)

    def __str__(self):
        return self.username