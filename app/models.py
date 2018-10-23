"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    periodo = models.CharField(max_length=75)
    instituicao = models.CharField(max_length=200)
class Vestibular(models.Model):
nome = models.CharField(max_length=200)
