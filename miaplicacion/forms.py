from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['nombre', 'region', 'aroma', 'sabor']

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'direccion', 'zona', 'telefono', 'horario_atencion']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email', 'nro_cuenta_pesos']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['cafe', 'nombre', 'descripcion', 'precio']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente_nombre', 'cliente_direccion', 'cliente_zona', 'cliente_telefono', 'productos']
    cliente_nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del cliente'}))
    cliente_direccion = forms.CharField(label='Direccion', widget=forms.TextInput(attrs={'placeholder': 'Ingrese la dirección del cliente'}))
    cliente_zona = forms.CharField(label='Zona', widget=forms.TextInput(attrs={'placeholder': 'Ingrese la zona del cliente'}))
    cliente_telefono = forms.CharField(label='Telefono', widget=forms.TextInput(attrs={'placeholder': 'Ingrese el teléfono del cliente'}))
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all(), widget=forms.Select())


class BusquedaForm(forms.Form):
    busqueda = forms.CharField(label='Buscar', max_length=100)

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}    

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)


    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name' ]
        help_texts = { k:"" for k in fields}

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True) 

# Correciones: Nuevo modelo compra para sustituir a pedido. 

class CompraForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    telefono = forms.CharField(max_length=20)
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())


class CompradorForm(forms.ModelForm):
    class Meta:
        model = Comprador
        fields = ['nombre', 'apellido', 'email', 'telefono']