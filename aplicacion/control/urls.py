from django.urls import path

from aplicacion.control.views import controlCL

urlpatterns = [
    path('home/infoCL/controlCL/', controlCL, name='vista5'),
]
