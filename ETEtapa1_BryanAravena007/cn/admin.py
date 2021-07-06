from django.contrib import admin
from .models import Colab, inicio_sesion

# Register your models here.

admin.site.register(inicio_sesion)
admin.site.register(Colab)
