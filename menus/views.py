#from itertools import product

from django.shortcuts import render, get_object_or_404, redirect
from menus.models import Producto, Categoria, Menu
from .forms import MenuForm, ProductoForm, CategoriaForm


# Create your views here.
def index(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'index.html',
                  context={'p': productos, 'c': categorias})


def mostrar_menus(request):
    platos = [
        {'nombre': 'Arroz con pollo', 'precio': 2.50, 'imagen': 'images/arroz_pollo.jpg'},
        {'nombre': 'Sopa de verduras', 'precio': 1.75, 'imagen': 'images/sopa_verduras.jpg'},
        {'nombre': 'Arroz con carne', 'precio': 3.00, 'imagen': 'images/arroz_carne.jpg'},
        {'nombre': 'Motepillo', 'precio': 2.50, 'imagen': 'images/motepillo.jpg'},
        {'nombre': 'Tamal', 'precio': 1.50, 'imagen': 'images/tamal.jpg'}
    ]
    return render(request, 'menus.html', {'platos': platos})





def lista_menus(request):
    menus = Menu.objects.all()
    return render(request, 'lista_menus.html', {'menus': menus})



def editar_menu(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)  # Obtiene el menú o devuelve 404 si no existe
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)  # Crea un formulario con los datos enviados
        if form.is_valid():
            form.save()  # Guarda los cambios en la base de datos
            return redirect('lista_menus')  # Redirige a la lista de menús
    else:
        form = MenuForm(instance=menu)  # Crea un formulario con los datos actuales del menú
    return render(request, 'editar_menu.html', {'form': form, 'menu': menu})

def eliminar_menu(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)  # Obtiene el menú o devuelve 404 si no existe
    if request.method == 'POST':
        menu.delete()  # Elimina el menú de la base de datos
        return redirect('lista_menus')  # Redirige a la lista de menús
    return render(request, 'eliminar_menu.html', {'menu': menu})

def gestionar_menu(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    categorias = menu.categorias.all()
    return render(request, 'gestionar_menu.html', {'menu': menu, 'categorias': categorias})

def agregar_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)  # Crea un formulario con los datos enviados
        if form.is_valid():
            form.save()  # Guarda el nuevo menú en la base de datos
            return redirect('lista_menus')  # Redirige a la lista de menús
    else:
        form = MenuForm()  # Crea un formulario vacío para agregar un nuevo menú
    return render(request, 'agregar_menu.html', {'form': form})

def agregar_categoria(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.menu = menu
            categoria.save()
            return redirect('gestionar_menu', menu_id=menu.id)
    else:
        form = CategoriaForm()
    return render(request, 'agregar_categoria.html', {'form': form, 'menu': menu})

# Vista para agregar un producto a una categoría
def agregar_producto(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.categoria = categoria
            producto.save()
            return redirect('gestionar_menu', menu_id=categoria.menu.id)
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form, 'categoria': categoria})

# Vista para gestionar un menú (mostrar categorías y productos)

