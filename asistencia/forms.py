from django import forms
from .models import Asistencia


class AsistenciaForm(forms.ModelForm):
    presente = forms.BooleanField(required=False)

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
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'placeholder': 'Ej. Juan Pérez García'}),
            'documento_identidad': forms.TextInput(attrs={'placeholder': 'Ej. 1234567890'}),
            'correo_electronico': forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com'}),
            'fecha_asistencia': forms.DateInput(attrs={'type': 'date'}),
            'hora_ingreso': forms.TimeInput(attrs={'type': 'time'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time'}),
            'observaciones': forms.Textarea(attrs={'placeholder': 'Escribe aquí cualquier observación...', 'rows': 4}),
        }
