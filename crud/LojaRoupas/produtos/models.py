from django.db import models

class Camisa(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    tamanho = models.CharField(max_length=10)

class Calca(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    tamanho = models.CharField(max_length=10)

class Tenis(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    tamanho = models.CharField(max_length=10)

class Casaco(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    tamanho = models.CharField(max_length=10)