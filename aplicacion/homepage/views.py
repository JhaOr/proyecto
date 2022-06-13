from smtplib import SMTPResponseException
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def principal(request):
    return render(request, 'aplicacion/homepage/plantillas/home/home.html')


def infoCL(request):
    return render(request, 'aplicacion/homepage/plantillas/PreLabs/infoCL.html')
