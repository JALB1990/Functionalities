from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from django.template import Template, Context
from gestion_usuarios import password_manage
from gestion_usuarios import models
from django.views.decorators.csrf import csrf_exempt
from gestion_usuarios import email_check

# Create your views here.

#desde el name
def adduser(request):
    hash = password_manage.password_generator(request.GET["psw"])
    user = request.GET["uname"]
    email = request.GET["email"]
    useradd = models.users.objects.create(username=user,password=hash,email=email)
    return HttpResponse(user,hash)

def emailcheck(request):
    if request.accepts and request.method == "POST":
        emailtext = request.POST.get('email')
        if email_check.check(emailtext):
            print("valid email")
            queryset = models.users.objects.filter(email=emailtext)
            if queryset.exists():
                print("exist")
                return JsonResponse({"reach":True,"valid":True,"exist":True}, status = 200)
            else:
                print("no exist")
                return JsonResponse({"reach":True,"valid":True,"exist":False}, status = 200)
        elif not email_check.check(emailtext):
            print("invalid email")
            return JsonResponse({"reach":True,"valid":False}, status = 200)
    return JsonResponse({"reach":False}, status = 400)

def unamecheck(request):
    if request.accepts and request.method == "POST":
        unametext = request.POST.get('uname')
        queryset = models.users.objects.filter(username=unametext)
        if queryset.exists():
            print("exist")
            return JsonResponse({"reach":True,"valid":True,"exist":True}, status = 200)
        else:
            print("no exist")
            return JsonResponse({"reach":True,"valid":True,"exist":False}, status = 200)
    return JsonResponse({"reach":False}, status = 400)


def testcall(request):
    if request.accepts and request.method == "POST":
        emailcheck = request.POST.get('text')
        print(emailcheck)
        queryset = models.users.objects.filter(email=emailcheck)
        if queryset.exists():
            print("si esta")
            print(JsonResponse({"exist":'true'}, status = 200))
            return JsonResponse({"exist":'true'}, status = 200)
        else:
            print("no esta")
            return JsonResponse({"valid":"No hay"}, status = 200)
        
        
    return JsonResponse({}, status = 400)
    
#sopas@email.com