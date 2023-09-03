from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente
from .serializers import ClienteSerializer
import json
# Create your views here.

@api_view(['GET', 'PUT'])
def get_clientes(request):
    #Este metodo pega todos os objetos clientes no banco de dados e serializa eles na classe serializer
    #apos isso retorna a data serializada

    if request.method == 'GET':
        clientes = Cliente.objects.all()  

        serializer = ClienteSerializer(clientes, many=True) 

        return Response(serializer.data)
  
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
# metodo que pega o objeto que possui o username, serializa-o e da um retorno dos dados serializados
def get_pelo_username(request, nick):
    try:
        cliente = Cliente.objects.get(pk = nick)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status= status.HTTP_400_BAD_REQUEST)

# Metodo de gerenciamento possuindo GET, PUT, DELETE E POST
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def geren_cliente(request):
    
    #PEGAR OS DADOS - GET

    if request.method == 'GET':
        try:
          if request.GET['user']:
              username = request.GET['user']
              try:
                  cliente = Cliente.objects.get(pk=username)
              except:
                  return Response(status= status.HTTP_404_NOT_FOUND)

              serializer = ClienteSerializer(cliente)
              return Response(serializer.data)
          else:
              return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
          return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    # CRIACAO DE DADOS OPERACAO POST, serializa o novo objeto pego a partir do request, valida e salva 
    if request.method == 'POST':
        novo_cliente = request.data
        serializer = ClienteSerializer(data = novo_cliente)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    # EDITA DADOS OPERACAO PUT
    if request.method == 'PUT':
        username = request.data['username']
        try:
          clienteAtt = Cliente.objects.data['pk=username']
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            serializer.save()
            return(Response(clienteAtt, data=request.data))
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
    

    # DELETAR DADOS - busca o objeto a partir do username, se realizado com sucesso deleta do banco o objeto
    if request.method == 'DELETE':
        try:
            cliente_ser_delet = Cliente.objects.get(pk=request.data['username'])
            cliente_ser_delet.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            

        



 