from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Clientes
from django.contrib.auth.views import LoginView
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

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
  
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context,request))
