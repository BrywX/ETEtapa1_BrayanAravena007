from django import forms
from django.forms import ModelForm, widgets
from .models import Colab 

class ColabForm(ModelForm):

    class Meta: 
        model = Colab
        fields = ['rut','nombre','pais','region','direccion','telefono','email','imagen','contrasena']

        labels={'rut': 'Rut: ', 'nombre': 'Nombre: ', 'pais': 'Pais: ', 
        'region': 'Region: ','direccion': 'Direccion: ','telefono': 'Telefono: ','email': 'Email: ', 'contrasena': 'Contrasena',
        'imagen': 'Imagen Colaborador: '},


        widgets={
        'rut': forms.TextInput(attrs={'class': 'form-control', 'id': 'rut','name': 'rut','onchance':"CambiarMayusculas()",'onfocus':"CambiaColor(this)"}), 
        'nombre': forms.TextInput(attrs={'class': 'form-control', 'id': 'nombre','name': 'nombre'}), 
        'pais': forms.TextInput(attrs={'class': 'form-control', 'id': 'pais','name': 'pais','onchance':"CambiarMayusculas()",'onfocus':"CambiaColor(this)"}), 
        'region': forms.TextInput(attrs={'class': 'form-control','id': 'region','name': 'region'}),
        'direccion': forms.TextInput(attrs={'class': 'form-control', 'id': 'direccion','name': 'direccion'}), 
        'telefono': forms.TextInput(attrs={'class': 'form-control', 'id': 'telefono','name': 'telefono'}), 
        'email': forms.TextInput(attrs={'class': 'form-control' , 'id': 'email','name': 'email'}),
        'contrasena': forms.TextInput(attrs={'class': 'form-control' , 'id': 'contrasena','name': 'contrasena'}),  
        'imagen': forms.ClearableFileInput(attrs={'class': 'form-control','id': 'imagen','name': 'imagen','accept':"imagen/*"})
        }


