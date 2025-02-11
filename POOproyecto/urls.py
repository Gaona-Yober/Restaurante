"""
URL configuration for POOproyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from mesas import views as mesas_views
from inventario import views as inventario_views
from menus import views as menus_views



def home(request):
    return render(request, 'sitio_admin.html')

urlpatterns = [
    path('', home, name='home'),  # Página de inicio
    path('admin/', admin.site.urls),  # Administración
    path('reserva/', mesas_views.reserva_mesa, name='reserva_mesa'),
    path('reserva_exito/', mesas_views.reserva_exitosa, name='reserva_exitosa'),
    path('modificar_reserva/<int:reserva_id>/', mesas_views.modificar_reserva, name='modificar_reserva'),
    path('iniciosecion/', mesas_views.iniciar_sesion, name='iniciar_sesion'),
    path('inventariofacturacion/', inventario_views.inventario_facturacion, name='inventariofacturacion'),
    path('insumos/', inventario_views.lista_insumos, name='lista_insumos'),
    path('agregar-insumo/', inventario_views.agregar_insumo, name='agregar_insumo'),
    path('realizar-operacion/', inventario_views.realizar_operacion, name='realizar_operacion'),
    path('reserva/', mesas_views.reserva, name='reserva'),
    path('guardar_persona/', mesas_views.guardar_persona, name='guardar_persona'),


    path('menus/', menus_views.mostrar_menus, name='menus'),
    path('lista_menus/', menus_views.lista_menus, name='lista_menus'),
    path('agregar_menu/', menus_views.agregar_menu, name='agregar_menu'),
    path('gestionar_menu/', menus_views.gestionar_menu, name='gestionar_menu'),
    path('agregar_menu/', menus_views.agregar_menu, name='agregar_menu'),
    path('gestionar_menu/<int:menu_id>/', menus_views.gestionar_menu, name='gestionar_menu'),
    path('lista_menus/', menus_views.lista_menus, name='lista_menus'),
    path('editar_menu/<int:menu_id>/', menus_views.editar_menu, name='editar_menu'),
    path('eliminar_menu/<int:menu_id>/', menus_views.eliminar_menu, name='eliminar_menu'),

    path('agregar_categoria/<int:menu_id>/', menus_views.agregar_categoria, name='agregar_categoria'),
    path('agregar_producto/<int:categoria_id>/', menus_views.agregar_producto, name='agregar_producto'),


]