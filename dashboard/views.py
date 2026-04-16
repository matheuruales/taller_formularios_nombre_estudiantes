from django.shortcuts import render
from asistencia.models import Asistencia
from solicitudes.models import Solicitud


def dashboard(request):
    asistencias = Asistencia.objects.all().order_by('-fecha_asistencia')
    solicitudes = Solicitud.objects.all().order_by('-fecha_solicitud')

    total_asistencias = asistencias.count()
    total_presentes = asistencias.filter(presente=True).count()
    total_ausentes = asistencias.filter(presente=False).count()
    total_solicitudes = solicitudes.count()

    solicitudes_por_tipo = {
        'Académica': solicitudes.filter(tipo_solicitud='academica').count(),
        'Administrativa': solicitudes.filter(tipo_solicitud='administrativa').count(),
        'Técnica': solicitudes.filter(tipo_solicitud='tecnica').count(),
        'Otra': solicitudes.filter(tipo_solicitud='otra').count(),
    }

    context = {
        'asistencias': asistencias,
        'solicitudes': solicitudes,
        'total_asistencias': total_asistencias,
        'total_presentes': total_presentes,
        'total_ausentes': total_ausentes,
        'total_solicitudes': total_solicitudes,
        'solicitudes_por_tipo': solicitudes_por_tipo,
    }
    return render(request, 'dashboard/index.html', context)
