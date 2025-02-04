from datetime import timezone

from django.shortcuts import render, redirect
from .forms import ReservaForm
from .models import Reserva, Cliente, Mesa, EstadoMesa


from datetime import timezone

from django.shortcuts import render, redirect
from .forms import ReservaForm
from .models import Reserva, Cliente, Mesa, EstadoMesa


from django.shortcuts import render, redirect
from .models import Reserva, Cliente, Mesa, EstadoMesa

def reservar_mesa(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')  # Puede ser None si no está configurado en el formulario.
        fecha = request.POST.get('fecha')  # Cambiado a 'fecha' para coincidir con el formulario HTML.
        hora = request.POST.get('hora')  # Cambiado a 'hora' para coincidir con el formulario HTML.

        # Validar cantidad de personas
        cantidad_personas_str = request.POST.get('personas', '')  # Cambiado a 'personas' para coincidir con el formulario HTML.
        if not cantidad_personas_str.isdigit():  # Comprobar si es un número válido
            return render(request, 'error.html',
                          {'mensaje': 'Cantidad de personas no válida. Por favor, ingrese un número.'})

        # Convertir a entero después de validar
        cantidad_personas = int(cantidad_personas_str)

        # Crear o obtener el cliente
        cliente, created = Cliente.objects.get_or_create(
            defaults={
                'nombre': nombre,
                'cedula_persona': '0000000000',  # Puedes pedir la cédula en el formulario si es necesario
                'telefono': '0000000000'  # Puedes pedir el teléfono en el formulario si es necesario
            }
        )

        # Seleccionar una mesa (sin validar disponibilidad)
        mesa = Mesa.objects.first()  # Selecciona la primera mesa disponible en la base de datos

        # Crear la reserva usando el método del cliente
        try:
            reserva = cliente.hacer_reserva({
                'mesa': mesa,
                'cantidad_personas': cantidad_personas,
                'fecha_reserva': fecha,
                'horario_inicio': f"{fecha}T{hora}"  # Combinar fecha y hora para el campo DateTimeField
            })
        except Exception as e:
            return render(request, 'error.html', {'mensaje': str(e)})

        # Cambiar el estado de la mesa a RESERVADA
        mesa.cambiar_estado(EstadoMesa.RESERVADA.name)

        # Redirigir a una página de éxito
        return redirect('reserva_exitosa')

    # Si no es POST, mostrar el formulario
    return render(request, 'reservas.html')

def reserva_exitosa(request):
    return render(request, 'reserva_exitosa.html')
