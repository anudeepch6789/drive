from django.db import models
#from django.contrib.auth.models import User


# Create your models here.

'''creating database '''
class userinfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)

    def __str__(self):
        return self.username