from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Clientes
from django.contrib.auth.views import LoginView
from django.views import generic
# Create your views here.

class login(generic.LoginView):
  def login(request):
    if request.method == 'POST':
        form =AuthenticationForm(request, request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect ('login1')
                                          
    else:
        form =AuthenticationForm()
    return render(request, 'login.html',{'form': form})                
  

def remesas(request):
    myclientes= Clientes.objects.all().values()
    template =loader.get_template('all_clientes.html')
    context = {
    'myclientes': myclientes,
  }
    return HttpResponse(template.render(context, request))

def details(request,id):
    myclientes= Clientes.objects.get(id=id)
    template=loader.get_template('details.html')
    context = {
    'myclientes': myclientes,
  }
    return HttpResponse(template.render(context, request))

def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    return HttpResponse(template.render())