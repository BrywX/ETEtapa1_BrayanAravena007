from django.urls import path
from .views import del_colab, index, colaboradores, contact, new_colab, mod_colab, del_colab

urlpatterns=[ 
    path('', index, name="index"),
    path('colaboradores', colaboradores, name="colaboradores"),
    path('contact', contact, name="contact"),
    path('new_colab', new_colab, name="new_colab"),
    path('mod_colab/<id>', mod_colab, name="mod_colab"),
    path('del_colab/<id>', del_colab, name="del_colab"),


]