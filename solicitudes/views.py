from django.shortcuts import render, redirect
from .forms import SolicitudForm


def registrar_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('solicitudes:confirmacion')
    else:
        form = SolicitudForm()
    return render(request, 'solicitudes/formulario.html', {'form': form})


def confirmacion(request):
    return render(request, 'solicitudes/confirmacion.html')
