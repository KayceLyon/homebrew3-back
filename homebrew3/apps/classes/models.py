from django.db import models

# Create your models here.

class Archetype(models.Model):
    name = models.CharField(max_length=64)

class Classe(models.Model):
    name = models.CharField(max_length=64)

class Subclasse(models.Model):
    name = models.CharField(max_length=64)
