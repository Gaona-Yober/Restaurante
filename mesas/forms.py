from django import forms
from django.utils import timezone as tz
from .models import Reserva
from django.utils.timezone import get_current_timezone
from django.utils.timezone import make_aware

class ReservaForm(forms.ModelForm):
    hora_inicio = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Reserva
        fields = ['identificador', 'cliente', 'mesa', 'cantidad_personas', 'fecha_reserva', 'hora_inicio']
        widgets = {
            'fecha_reserva': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_reserva = cleaned_data.get('fecha_reserva')
        hora_inicio = cleaned_data.get('hora_inicio')

        if fecha_reserva and hora_inicio:
            if fecha_reserva < tz.now().date():
                raise forms.ValidationError("La fecha de la reserva no puede ser anterior a la fecha actual.")

            fecha_hora_naive = tz.datetime.combine(fecha_reserva, hora_inicio)

            current_timezone = get_current_timezone()
            fecha_hora = make_aware(fecha_hora_naive, current_timezone)

            if fecha_hora < tz.now():
                raise forms.ValidationError("La hora de la reserva no puede ser anterior a la hora actual.")

            cleaned_data['horario_inicio'] = fecha_hora

        return cleaned_data



