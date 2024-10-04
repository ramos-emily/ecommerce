from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import produto # preciso importar oq usarei, sendo nome da pasta e do que eu quero importar
from .serializer import produtoSerializer
from rest_framework import status
from rest_framework.response import Response #Resposta

@api_view(['GET', 'POST']) # get vai cadastrar um produto e mandar pro banco #post
def listar_produtos(request): #funçao que chama o "listar produtos"
    if request.method == 'GET': #pqgando os dados para mostrar na tela GET = pegar
        queryset = produto.objects.all() #tabela produto inteira, quadrada
        serializer = produtoSerializer(queryset, many=True) #pega o queryset e transforma tudo em json e joga no serializer
        return Response(serializer.data)  #retornar a resposta, tras os dados, aquela janela do f12 no browser
    elif request.method == 'POST': #enviando 
        serializer = produtoSerializer(data = request.data) #serializer variavel temporaria
        serializer.is_valid()
        serializer.save() #salvar
        return Response(serializer.data, status=status.HTTP_201_CREATED) #retornar a resposta se foi criado
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST) #fala que nao foi criado