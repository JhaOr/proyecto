from django.urls import path

from aplicacion.homepage.views import principal, infoCL, infoPI, infoMR

# urls de la aplicaccion
urlpatterns = [
    path('home/', principal, name='vista1'),
    path('home/infoCL/', infoCL, name='vista2'),
    path('home/infoPI/', infoPI, name='vista3'),
    path('home/infoMR/', infoMR, name='vista3'),
]
