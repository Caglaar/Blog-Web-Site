from django.db import models

class User(models.Model):
    mail = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)

    

    def __str__(self):
        return self.mail