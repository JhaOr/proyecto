from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def controlCL(request):
    return render(request, 'aplicacion/control/plantillas/control/controlCL.html')

def controlPI(request):
    return render(request, 'aplicacion/control/plantillas/control/controlPI.html') 

def controlMR(request):
    return render(request, 'aplicacion/control/plantillas/control/controlMR.html') 
