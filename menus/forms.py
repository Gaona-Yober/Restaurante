from django import forms
from .models import Menu, Categoria, Producto

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['nombre', 'estado']  # Campos que se pueden editar


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'disponibilidad']