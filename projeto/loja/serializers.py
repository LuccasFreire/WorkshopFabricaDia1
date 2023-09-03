from rest_framework import serializers
from loja.models import Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        # fields = ('nome', 'username', 'telefone','email', 'endereco')
        fields = '__all__'
