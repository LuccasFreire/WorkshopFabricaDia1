from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)
    nome = models.CharField(max_length=100, default='')
    preco = models.CharField(max_length=100, default='')
    descricao = models.TextField()
    comprado = models.DateTimeField(auto_now_add=True)

class Cliente(models.Model):
    # produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, default='')
    username = models.CharField(primary_key=True, max_length=100, default='')
    telefone = models.CharField(max_length=100, default='')
    email = models.EmailField()
    endereco = models.TextField(max_length=100, default='')
    def __str__(self) -> str:
        return self.username