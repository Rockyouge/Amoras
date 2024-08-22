from django.shortcuts import render

# Create your views here.

#views.py

def minha_views(requeset):
    return HttpResponse("ola, essa é viwes baseada em uma função!")
from django.viwes import viwes 
from django.http  import HttpResponse 
    class minha_views(viwes):
    def get(self,request):("olá, esssa é uma views classe!")