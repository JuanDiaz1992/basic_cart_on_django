from django.db import models

class Users(models.Model):
    name = models.TextField(max_length=80)
    email = models.EmailField()
    user = models.TextField(max_length=20)
    password = models.TextField(max_length=200)

    def __str__(self):
        return self.name

