from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('', views.registrar_solicitud, name='formulario'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
]
