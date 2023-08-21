from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="inicio" ),

    path('about/', about, name="about"),
    path('blog/', blog, name="blog"),
    path('cafe/', cafe, name="cafe"),
    path('contacto/', contacto, name="contacto"),

    path('crear_cafe/', crear_cafe, name='crear_cafe'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('crear_sucursal/', crear_sucursal, name='crear_sucursal'),

    path('lista_sucursales/', lista_sucursales, name='lista_sucursales'),
    path('lista_pedidos/', lista_pedidos, name='lista_pedidos'),
    path('buscar_sucursales/', buscar_sucursales, name='buscar_sucursales'),
    
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="miaplicacion/logout.html"), name="logout"),
    path('register/', register, name="register"),

    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
    path('perfil/', perfil, name="perfil"),

    path('empleados/', empleados, name="empleados"),

    path('comprar/', comprar, name="comprar"),
    path('pedido_exitoso/', pedido_exitoso, name='pedido_exitoso'),
    path('crear_comprador/', crear_comprador, name='crear_comprador'),
    path('lista_compradores/', lista_compradores, name='lista_compradores'),
  
  
]