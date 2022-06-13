from django.urls import path

from aplicacion.homepage.views import principal, infoCL

# urls de la aplicaccion
urlpatterns = [
    path('home/', principal, name='vista1'),
    path('home/infoCL/', infoCL, name='vista4'),
]
