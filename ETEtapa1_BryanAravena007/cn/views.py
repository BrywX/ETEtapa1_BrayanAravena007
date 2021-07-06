from django.shortcuts import render, redirect, get_object_or_404
from .models import Colab
from .forms import ColabForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def colaboradores(request):
    colaboradores = Colab.objects.all()
    return render(request, 'colaboradores.html',context={'colaboradores':colaboradores})

def contact(request):
    return render(request, 'contact.html')



def new_colab(request):
    if request.method =='POST':
        colab_new=ColabForm(request.POST, request.FILES)
        clave=request.POST['rut'][:2]+request.POST['nombre'][:2].upper()+request.POST['pais'][:2]+request.POST['telefono'][-2:]
        colab_new.data=colab_new.data.copy()
        colab_new.data['contrasena']=clave
        if colab_new.is_valid():
            colab_new.save()
            return redirect('colaboradores')
    else: 
        colab_new=ColabForm()
    return render(request, 'cn/new_colab.html', {'colab_new': colab_new})

def mod_colab(request, id):
    colab = get_object_or_404(Colab, rut=id)
    datos ={'form': ColabForm(instance=colab)}
    if request.method == 'POST': 
        formulario = ColabForm(request.POST, request.FILES, instance = colab)
        if formulario.is_valid: 
            formulario.save()
            return redirect('colaboradores')
    return render(request, 'cn/mod_colab.html', datos)

def del_colab(request, id):
    colab = get_object_or_404(Colab, rut=id)
    colab.delete()
    return redirect('colaboradores')


    


