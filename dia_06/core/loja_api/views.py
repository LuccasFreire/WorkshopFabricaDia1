from django.shortcuts import render
from loja.models import Cliente, Produto, Categoria
from loja.serializers import ClienteSerializer, ProdutoSerializer, CategoriaSerializer
from rest_framework import generics, pagination
import rest_framework.pagination
# Create your views here.

class ClienteLista(generics.ListCreateAPIView):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProdutoLista(generics.ListCreateAPIView):

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class CategoriaLista(generics.ListCreateAPIView):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class BasicPagination(pagination.PageNumberPagination):
    page_size_query_param = 2