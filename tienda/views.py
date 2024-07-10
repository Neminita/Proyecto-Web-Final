from django.shortcuts import render, redirect, get_object_or_404
from .models import Vinilo
from .models import Jazz
from .models import Clasica
from .models import Rock
from .forms import ViniloForm


# Create your views here.

def home(request):
    return render(request, 'tienda/inicio.html')

def carrito(request):
    return render(request, 'tienda/vCarrito.html')

def clasica(request):
    vinilos = Vinilo.objects.all()
    data = {"vinilos" : vinilos}
    return render(request, 'tienda/vclasica.html', data)

def contacto(request):
    return render(request, 'tienda/vContacto.html')

def inisesion(request):
    return render(request, 'tienda/vInicioSesion.html')

def jazz(request):

    vinilos = Vinilo.objects.all()
    data = {"vinilos" : vinilos}

    return render(request, 'tienda/vjazz.html', data)

def nosotros(request):
    return render(request, 'tienda/vNosotros.html')
    
def registro(request):
    return render(request, 'tienda/vRegistro.html')

def rock(request):
    vinilos = Vinilo.objects.all()
    data = {"vinilos" : vinilos}
    return render(request, 'tienda/vrock.html', data) 

def agregar_producto(request):
    data = {'form' : ViniloForm()}
    if request.method == 'POST':
        formulario = ViniloForm(data=request.POST, files=request.FILES) 
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request, 'tienda/vinilo/agregar.html', data)

def listar_producto(request):
    vinilos = Vinilo.objects.all()
    data = {"vinilos" : vinilos}
    
    return render(request, 'tienda/vinilo/listar.html', data)

def modificar_producto(request, id):
    vinilos = get_object_or_404(Vinilo, id=id)
    data= {"form" : ViniloForm(instance=vinilos)}
    if request.method == 'POST':
        formulario = ViniloForm(data=request.POST, instance= vinilos, files=request.FILES) 
        if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "Modificado Correctamente"
                return redirect(to="listar_producto")    
    return render(request, 'tienda/vinilo/modificar.html', data)

def eliminar_producto(request, id):
    vinilos=get_object_or_404(Vinilo, id=id)
    vinilos.delete()
    return redirect(to="listar_producto")