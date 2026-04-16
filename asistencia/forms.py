from django import forms
from .models import Asistencia


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = [
            'nombre_completo',
            'documento_identidad',
            'correo_electronico',
            'fecha_asistencia',
            'hora_ingreso',
            'hora_salida',
            'presente',
            'observaciones',
        ]
