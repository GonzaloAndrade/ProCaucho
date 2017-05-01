# coding: utf8
from django.http import HttpResponse
from django.template import Context, loader
from django import forms
from django.shortcuts import render_to_response
from django.core.mail import send_mail
import datetime
import json

# Create your views here.
def contact(request):
    if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            textarea = request.POST.get('textarea')

            text = "Usuario: "+name +" Telefono: " +phone+ " Mensaje: " + textarea +" Email: " + email
            response_data = name

            # Enviar correo
            send_mail("Formulario de Contacto ProCaucho", text, "ventas@procaucho.com.ec", ['ventas@procaucho.com.ec'],
                      fail_silently=False)
            return HttpResponse(json.dumps("success"), content_type="application/json")


