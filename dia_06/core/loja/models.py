from django.db import models

# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length=50, default = 'True')
    def __str__(self):
        return self.name

class Produto(models.Model):
    Categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    name = models.CharField(max_length=50, default = 'True')    
    price = models.IntegerField(max_length=50, default = 'True')
    created = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Cliente(models.Model):
    name = models.CharField(max_length=50, default = 'True')
    address = models.CharField(max_length=200, default = 'True')
    phone = models.CharField(max_length=50, default = 'True')
    cpf = models.CharField(max_length=50, default = 'True')
    
    def __str__(self):
        return self.name