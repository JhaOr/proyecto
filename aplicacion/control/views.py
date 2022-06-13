from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def controlCL(request):
    return render(request, 'aplicacion/control/plantillas/control/control.html')
