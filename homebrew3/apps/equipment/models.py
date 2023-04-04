from django.db import models

# Create your models here.

class ArmorAndShield(models.Model):
    name = models.CharField(max_length=64)

class Weapon(models.Model):
    name = models.CharField(max_length=64)

class AdventuringGear(models.Model):
    name = models.CharField(max_length=64)

class WonderousItem(models.Model):
    name = models.CharField(max_length=64)

class CoinsAndGemstone(models.Model):
    name = models.CharField(max_length=64)

