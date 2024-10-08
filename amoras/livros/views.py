# Create your views here.
#views.py
from django.utils.decorators import method_decorator
from django.http  import HttpResponse 
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Livro

import json
from django.http import JsonResponse
from .models import Livro


@method_decorator(csrf_exempt, name='dispatch')
class LivroViews(View):

    def get(self, request):
        livros = Livro.objects.all()
        livros_list = [
            {
                "id": livro.id,
                "título": livro.titulo,
                "autor": livro.autor,
                "publicado_em": livro.publicado_em.strftime('%Y-%m-%d')  # Formato de data, se necessário
            } for livro in livros
        ]
        return JsonResponse(livros_list, safe=False)

    
    def post(self, request):
        try:
            data = json.loads(request.body)
            titulo = data.get('titulo')
            autor = data.get('autor')
            publicado_em = data.get('publicado_em')

            if not titulo or not autor or not publicado_em:
                return HttpResponse('Todos os campos são necessários.', status=400)

            livro = Livro.objects.create(
                titulo=titulo,
                autor=autor,
                publicado_em=publicado_em
            )

            return HttpResponse(f'Livro criado com sucesso! ID: {livro.id}', status=201)
        except Exception as e:
            return HttpResponse(f'Erro inesperado: {str(e)}', status=500)
        
    def put(self, request):
        try:
            data = json.loads(request.body)
            # Acessa dados de formulário
            livro_id = data.get('id')
            if not livro_id:
                return HttpResponse('ID do livro é necessário.', status=400)
                
            livro = Livro.objects.get(id=livro_id)
            livro.titulo = data.get('titulo', livro.titulo)
            livro.autor = data.get('autor', livro.autor)
            livro.publicado_em = data.get('publicado_em', livro.publicado_em)
            livro.save()
            
            return HttpResponse('Livro atualizado com sucesso!')
        except Livro.DoesNotExist:
            return HttpResponse('Livro não encontrado', status=404)
        except Exception as e:
            return HttpResponse(f'Erro inesperado: {str(e)}', status=500)
      

    def delete(self, request):
        try:
            data = json.loads(request.body)
            # Acessa dados de formulário
            livro_id = data.get('id')
            if not livro_id:
                return HttpResponse('ID do livro é necessário.', status=400)

            livro = Livro.objects.get(id=livro_id)
            livro.delete()
            
            return HttpResponse('Livro deletado com sucesso!', status=204)
        
        except Livro.DoesNotExist:
            return HttpResponse('Livro não encontrado', status=404)
        except Exception as e:
            return HttpResponse(f'Erro inesperado: {str(e)}', status=500)