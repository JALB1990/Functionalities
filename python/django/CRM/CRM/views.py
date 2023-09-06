from django.http import HttpResponse
import requests
from django.template import Template, Context
from django.shortcuts import render
import gestion_usuarios.password_manage as password_manage

def login_view(request): #primer vista
 doc_externo = open(r'C:\Users\Ionock_Issha\Dropbox\Python\CRM\CRM\templates\login.html')
 plt = Template(doc_externo.read())
 doc_externo.close()
 ctx=Context()
 documento=plt.render(ctx)
 return HttpResponse(documento)

def register_user_view(request):
 doc_externo = open(r'C:\Users\Ionock_Issha\Dropbox\Python\CRM\CRM\templates\register_user.html')
 plt = Template(doc_externo.read())
 doc_externo.close()
 ctx=Context()
 documento=plt.render(ctx)
 return HttpResponse(documento)

