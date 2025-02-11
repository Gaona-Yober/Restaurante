from django.shortcuts import render, redirect
from .models import Insumo, Operacion, Historial, Alerta


def lista_insumos(request):
    insumos = Insumo.objects.all()
    return render(request, 'lista_insumos.html', {'insumos': insumos})


def agregar_insumo(request):
    if request.method == 'POST':
        identificador = request.POST['identificador']
        nombre = request.POST['nombre']
        cantidadDisponible = request.POST['cantidadDisponible']
        unidadMedida = request.POST['unidadMedida']
        nivelReorden = request.POST['nivelReorden']
        precioUnitario = request.POST['precioUnitario']
        ubicacion = request.POST['ubicacion']

        Insumo.objects.create(
            identificador=identificador,
            nombre=nombre,
            cantidadDisponible=cantidadDisponible,
            unidadMedida=unidadMedida,
            nivelReorden=nivelReorden,
            precioUnitario=precioUnitario,
            ubicacion=ubicacion
        )
        return redirect('lista_insumos')
    return render(request, 'agregar_insumo.html')


def realizar_operacion(request):
    if request.method == 'POST':
        tipo = request.POST['tipo']
        insumo_id = request.POST['insumo']
        cantidad = request.POST['cantidad']
        observaciones = request.POST['observaciones']

        insumo = Insumo.objects.get(id=insumo_id)
        Operacion.objects.create(
            tipo=tipo,
            insumo=insumo,
            cantidad=cantidad,
            observaciones=observaciones
        )
        return redirect('lista_insumos')
    insumos = Insumo.objects.all()
    return render(request, 'realizar_operacion.html', {'insumos': insumos})


def inventario_facturacion(request, menu_id=None):
    menus_id = request.GET.getlist('menus')
    return render(request, 'inventario_facturacion.html', {'menus_id': menus_id})

