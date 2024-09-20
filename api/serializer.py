from rest_framework import serializers
from .models import produto

class produtoSerializer (serializers.modelSerializer):
    class Meta: #propriedades dos dados
        model = produto
        fields = [
            'id', 
            'codigoProduto',
            'tituloProduto',
            'preco',
            'descricao',
            'imagemProduto',
            'categoriaProduto',
            'classProduto',
            'exibirHome',
            ]
