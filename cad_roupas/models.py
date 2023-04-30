from django.db import models

# Create your models here.

#------- Seção Feminino --------------------------------------
class VestidoNoiva(models.Model):
    nomeDoVestido = models.CharField(max_length=200)
    tamanhoDoVestido = models.CharField(max_length=100)
    valorDoVestido = models.FloatField(default=0)
    descricaoVestido = models.TextField(max_length=1000)
    imagemCat = models.TextField(default='img/noiva.jpg')
    
    def __str__(self):
        return self.nomeDoVestido
    
class VestidoFormatura(models.Model):
    nomeDoVestido = models.CharField(max_length=200)
    tamanhoDoVestido = models.CharField(max_length=100)
    valorDoVestido = models.FloatField(default=0)
    descricaoVestido = models.TextField(max_length=1000)
    imagemCat = models.TextField(default='img/formatura.jpg')
    
    def __str__(self):
        return self.nomeVestidoFormatura
    
class VestidoFesta(models.Model):
    nomeDoVestido = models.CharField(max_length=200)
    tamanhoDoVestido = models.CharField(max_length=100)
    valorDoVestido= models.FloatField(default=0)
    descricaoVestido = models.TextField(max_length=1000)
    imagemCat = models.TextField(default='img/festa.jpg')
    
    def __str__(self):
        return self.nomeVestidoFesta
    
    
#----- Seção Masculino ---------------------------------------------------   
    
class TernoNoivo(models.Model):
    nomeTernoNoivo = models.CharField(max_length=200)
    tamanhoTernoNoivo = models.CharField(max_length=100)
    valorTernoNoivo = models.FloatField(default=0)
    descricaoTernoNoivo = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.nomeTernoNoivo
    
    
class Smoking(models.Model):
    nomeSmoking = models.CharField(max_length=200)
    tamanhoSmoking = models.CharField(max_length=100)
    valorSmoking = models.FloatField(default=0)
    descricaoSmoking = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.nomeSmoking
    
    
class Blazer(models.Model):
    nomeBlazer = models.CharField(max_length=200)
    tamanhoBlazer = models.CharField(max_length=100)
    valorBlazer = models.FloatField(default=0)
    descricaoBlazer = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.nomeBlazer
    
 



#---------------------------------------------------------------------   
class Cliente(models.Model):
    nomeDoCliente = models.CharField(max_length=200)
    senhaDoCliente = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nomeDoCliente