from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tokens =  models.IntegerField(default=0, blank=True)
    # Agrega otros campos adicionales según tus necesidades
    def get_username(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class Paquetes(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    saldo = models.IntegerField()

class videos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videos = models.CharField(max_length= 255, blank=True)
    def get_username(self):
        return self.user.username
