from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from django.template import Context
from django.db.models import Q
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {'current_page': 'inicio'}
    return render(request, "miaplicacion/index.html", context)

def blog(request):
    return render(request, "miaplicacion/blog.html")

def cafe(request):
    cafes = Cafe.objects.all()
    return render(request, "miaplicacion/cafe.html", {'cafes': cafes})

def contacto(request):
    return render(request, "miaplicacion/contacto.html")

def about(request):
    return render(request, "miaplicacion/about.html")

@login_required
def crear_cafe(request):
    if request.method == 'POST':
        form = CafeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cafe')  
    else:
        form = CafeForm()
    
    return render(request, 'miaplicacion/crear_cafe.html', {'form': form})

@login_required
def crear_sucursal(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_sucursales')  
    else:
        form = SucursalForm()
    
    return render(request, 'miaplicacion/crear_sucursal.html', {'form': form})

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  
    else:
        form = ClienteForm()
    
    return render(request, 'miaplicacion/crear_cliente.html', {'form': form})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_producto')  
    else:
        form = ProductoForm()
    
    return render(request, 'miaplicacion/crear_producto.html', {'form': form})

@login_required
def crear_pedido(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            producto = form.cleaned_data['producto']

            cliente, created = Cliente.objects.get_or_create(
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono
            )

            pedido = Pedido(cliente=cliente)
            pedido.save()
            pedido.productos.add(producto)

            return redirect('lista_pedidos')
    else:
        form = CompraForm()
    
    return render(request, 'miaplicacion/crear_pedido.html', {'form': form})


def lista_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'miaplicacion/lista_sucursales.html', {'sucursales': sucursales})

@login_required
def lista_pedidos(request):
    pedidos = Pedido_compra.objects.all()
    return render(request, 'miaplicacion/lista_pedidos.html', {'pedidos': pedidos})


def buscar_sucursales(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            sucursales = Sucursal.objects.filter(
                Q(nombre__icontains=busqueda) |
                Q(direccion__icontains=busqueda) |
                Q(zona__icontains=busqueda) |
                Q(telefono__icontains=busqueda) |
                Q(horario_atencion__icontains=busqueda)
            )
        else:
            sucursales = Sucursal.objects.all()
    else:
        form = BusquedaForm()
        sucursales = Sucursal.objects.all()

    context = {'current_page': 'buscar_sucursales'}
    return render(request, 'miaplicacion/buscar_sucursales.html', {'form': form, 'sucursales': sucursales})


# CREO EMPLEADOS PARA ALOJAR LINKS UTILES PARA LOS MISMOS:
@login_required
def empleados(request):
    return render(request, 'miaplicacion/empleados.html')

#LOGIN, REGISTRO y EDITAR PERFIL

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, "miaplicacion/index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "miaplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "miaplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})

    miForm = AuthenticationForm()

    return render(request, "miaplicacion/login.html", {"form":miForm})    

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST) 
        if form.is_valid():  
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "miaplicacion/index.html", {"mensaje":"Usuario Creado"})        
    else:
        form = RegistroUsuariosForm() 

    return render(request, "miaplicacion/registro.html", {"form": form})    

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "miaplicacion/index.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "miaplicacion/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "miaplicacion/editarPerfil.html", {'form': form, 'usuario':usuario.username})


# CREO PERFIL PARA ALOJAR LINKS DE EDITAR PERFIL Y CAMBIAR AVATAR:
@login_required
def perfil(request):
    return render(request, 'miaplicacion/perfil.html')

# AVATARES

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0: 
                avatarViejo[0].delete()

            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "miaplicacion/index.html")
    else:
        form = AvatarFormulario()
    return render(request, "miaplicacion/agregarAvatar.html", {'form': form})


# PARA REEMPLAZAR A CREAR PEDIDO

from django.contrib import messages

def comprar(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            producto = form.cleaned_data['producto']

            comprador, created = Comprador.objects.get_or_create(
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono
            )

            pedido_compra = Pedido_compra.objects.create(comprador=comprador, producto=producto)

            messages.success(request, 'Pedido creado con éxito.')

            return redirect('pedido_exitoso')  
    else:
        form = CompraForm()

    return render(request, 'miaplicacion/comprar.html', {'form': form})

def pedido_exitoso(request):
    return render(request, 'miaplicacion/pedido_exitoso.html')

@login_required
def crear_comprador(request):
    if request.method == 'POST':
        form = CompradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_compradores')
    else:
        form = CompradorForm()
    return render(request, 'miaplicacion/crear_comprador.html', {'form': form})

@login_required
def lista_compradores(request):
    compradores = Comprador.objects.all()
    return render(request, 'miaplicacion/lista_compradores.html', {'compradores': compradores})