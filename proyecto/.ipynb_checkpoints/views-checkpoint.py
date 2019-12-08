from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from . import formulario as r
from . import  models as m
from django.http import HttpResponseRedirect

def redirect_root(request):
      return HttpResponseRedirect('/usuarios/inicio/')

def inicio(request):
    return render(request,'usuarios/inicio.html',{})

def registro_view(request):
    if request.method == 'POST':
        registro_form = r.RegistroForm(request.POST or None, request.FILES or None)
        if registro_form.is_valid():
            username = registro_form.cleaned_data['username']
            
            
            password = registro_form.cleaned_data['password']

            usuarioNuevo = User(username=username)
            usuarioNuevo.set_password(password)
            usuarioNuevo.save()
            login(request,usuarioNuevo)
            return redirect(inicio)

    else:
         registro_form = r.RegistroForm()
    return render(request,'usuarios/registro.html',{'RegistroForm': registro_form})

def salir_view(request):
    logout(request)
    return redirect(acceso_view)

def acceso_view(request):
    if request.method == 'POST':
        ingresar_form = r.IngresarForm(request.POST)
        if ingresar_form.is_valid():
            username = ingresar_form.cleaned_data['username']
            print(username)
            password = ingresar_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                return render(request,'usuarios/acceso.html',{'form': ingresar_form})
            login(request,user)
            return redirect(inicio)
    else:
        ingresar_form = r.IngresarForm()
    return render(request,'usuarios/acceso.html',{'IngresarForm': ingresar_form})
    
    next = request.POST.get('next', '')
    return HttpResponseRedirect(next)