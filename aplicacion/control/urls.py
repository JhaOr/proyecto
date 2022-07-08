from django.urls import path

from aplicacion.control.views import controlCL, controlPI, controlMR, camera

urlpatterns = [
     path('home/camera/camera/', camera, name='vista0'),
    path('home/infoCL/controlCL/', controlCL, name='vista5'),
    path('home/infoPI/controlPI/', controlPI, name='vista6'),
    path('home/infoMR/controlMR/', controlMR, name='vista7'),
]
