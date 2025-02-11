from datetime import datetime
from datetime import timezone
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Reserva, Persona
from .forms import ReservaForm

def reserva_mesa(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            # Validar o asignar 'horario_inicio'
            if not reserva.horario_inicio:
                reserva.horario_inicio = datetime.now(timezone.utc)
            reserva.save()
            return redirect('reserva_exitosa')
    else:
        form = ReservaForm()

    return render(request, 'sitio_reserva.html', {'form': form})
def reserva_exitosa(request):
    return render(request, 'reserva_exitosa.html')


def modificar_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva_exito')
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'modificar_reserva.html', {'form': form, 'reserva': reserva})


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'yobergaona21' and password == 'yober1234':
            return redirect('/inventariofacturacion/')
        else:
            error_message = "Usuario o contraseña incorrectos"
            return render(request, 'login.html', {'error': error_message})
    return render(request, 'login.html')

def reserva(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cedula = request.POST.get('cedula')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')


        Persona.objects.create(
            nombre=nombre,
            cedula_persona=cedula,
            email=email,
            telefono=telefono
        )

        return redirect('reserva_exitosa')

    return render(request, 'reserva.html')


@csrf_exempt
def guardar_persona(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cedula = request.POST.get('cedula')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        try:
            Persona.objects.create(
                nombre=nombre,
                cedula_persona=cedula,
                email=email,
                telefono=telefono
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Método no permitido'})