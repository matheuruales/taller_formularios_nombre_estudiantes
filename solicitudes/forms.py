from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'nombre_solicitante',
            'documento_identidad',
            'correo_electronico',
            'telefono_contacto',
            'tipo_solicitud',
            'asunto',
            'descripcion_detallada',
            'fecha_solicitud',
            'archivo_adjunto',
        ]
        widgets = {
            'nombre_solicitante': forms.TextInput(attrs={'placeholder': 'Ej. María López Torres'}),
            'documento_identidad': forms.TextInput(attrs={'placeholder': 'Ej. 1234567890'}),
            'correo_electronico': forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com'}),
            'telefono_contacto': forms.NumberInput(attrs={'placeholder': 'Ej. 3001234567'}),
            'tipo_solicitud': forms.Select(),
            'asunto': forms.TextInput(attrs={'placeholder': 'Resumen breve de la solicitud'}),
            'descripcion_detallada': forms.Textarea(attrs={
                'placeholder': 'Describe detalladamente tu solicitud...',
                'rows': 5,
            }),
            'fecha_solicitud': forms.DateInput(attrs={'type': 'date'}),
            'archivo_adjunto': forms.ClearableFileInput(),
        }
