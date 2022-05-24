from smtplib import SMTPResponseException
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def principal(request):
    return render(request, 'aplicacion/homepage/plantillas/home/home.html')


def info1(request):
    return render(request, 'aplicacion/homepage/plantillas/PreLabs/info.html')
