from django.db import models

# Create your models here.

# Categorías de discos: #

class Categoria(models.Model):
    titulo = models.CharField(max_length = 70) 

    def __str__(self):
        return self.titulo

#Discos en sí: #

class Vinilo(models.Model):
    valor = models.IntegerField()
    portada = models.ImageField(upload_to = "vinilos", null = True)
    autor = models.CharField(max_length = 30)
    nombre = models.CharField(max_length = 30)
    Categoria = models.ForeignKey(Categoria, on_delete = models.PROTECT)

    def __str__(self):
        return self.nombre
    
class Rock(models.Model):
    valorR = models.IntegerField()
    portadaR = models.ImageField(upload_to = "rocks", null = True)
    autorR = models.CharField(max_length = 30)
    nombreR = models.CharField(max_length = 30)
    CategoriaR = models.ForeignKey(Categoria, on_delete = models.PROTECT)

    def __str__(self):
        return self.nombreR
    
class Clasica(models.Model):
    valorC = models.IntegerField()
    portadaC = models.ImageField(upload_to = "clasicas", null = True)
    autorC = models.CharField(max_length = 30)
    nombreC = models.CharField(max_length = 30)
    CategoriaC = models.ForeignKey(Categoria, on_delete = models.PROTECT)

    def __str__(self):
        return self.nombreC    
    
class Jazz(models.Model):
    valorJ = models.IntegerField()
    portadaJ = models.ImageField(upload_to = "jazzs", null = True)
    autorJ = models.CharField(max_length = 30)
    nombreJ = models.CharField(max_length = 30)
    CategoriaJ = models.ForeignKey(Categoria, on_delete = models.PROTECT)

    def __str__(self):
        return self.nombreJ    
       
