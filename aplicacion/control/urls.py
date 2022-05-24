from django.urls import path

from aplicacion.control.views import control1

urlpatterns = [
    path('home/info1/control1/', control1, name='vista5'),
]
