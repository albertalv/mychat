from django.contrib import admin

# Register your models here.
from .models import Paquetes, videos

admin.site.register(Paquetes)
admin.site.register(videos)