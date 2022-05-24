from django.urls import path

from aplicacion.homepage.views import principal, info1

# urls de la aplicaccion
urlpatterns = [
    path('home/', principal, name='vista1'),
    path('home/info1/', info1, name='vista4'),
]
