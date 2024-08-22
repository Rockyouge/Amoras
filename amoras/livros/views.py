# Create your views here.
#views.py
from django.utils.decorators import method_decorator
from django.http  import HttpResponse 
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class LivroViews(View):
    def get(self, request):
        return HttpResponse("ola, amoras! Metodo get chamado com sucesso!")
    def post(self, request):
        return HttpResponse("ola, amoras! Metodo POST chamado com sucesso!")
    def put(self, request):
        return HttpResponse("ola, amoras! Metodo PUT chamado com sucesso!")
    def delete(self, request):
        return HttpResponse("ola, amoras! Metodo DELETE chamado com sucesso!")
