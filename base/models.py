from django.db import models

# Create your models here.
class Canal(models.Model):
    appId = models.CharField(max_length=255)
    channel = models.CharField(max_length= 255)
    token = models.CharField(max_length=255)
    uid = models.IntegerField()
class Meta:
        db_table = 'Canal'


class Token(models.Model):
    token = models.CharField(max_length=255)
    uid = models.IntegerField()
    
    def __str__(self):
        return self.token
    




class Stream(models.Model):
    appId = models.CharField(max_length=255)
    channel = models.CharField(max_length= 255)
    token = models.CharField(max_length=255)
    uid = models.IntegerField()

    def __str__(self):
        return self.token


class Estatus(models.Model):
    # Otros campos del canal
    channel = models.CharField(max_length= 255)
    estado = models.CharField(max_length= 255) 
