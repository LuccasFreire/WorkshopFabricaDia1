from rest_framework import serializers
from loja.models import Cliente, Produto, Categoria


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        # fields = ('nome', 'username', 'telefone','email', 'endereco')
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'