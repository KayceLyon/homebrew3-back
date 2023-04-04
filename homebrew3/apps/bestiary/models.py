from django.db import models

# Create your models here.

class Creature(models.Model):
    name = models.CharField(max_length=64)

class Keeper(models.Model):
    name = models.CharField(max_length=64)

class Aberration(models.Model):
    name = models.CharField(max_length=64)

class Beast(models.Model):
    name = models.CharField(max_length=64)

class Celestial(models.Model):
    name = models.CharField(max_length=64)

class Construct(models.Model):
    name = models.CharField(max_length=64)

class Dragon(models.Model):
    name = models.CharField(max_length=64)

class Elemental(models.Model):
    name = models.CharField(max_length=64)

class Fey(models.Model):
    name = models.CharField(max_length=64)

class Fiend(models.Model):
    name = models.CharField(max_length=64)

class Giant(models.Model):
    name = models.CharField(max_length=64)

class Humanoid(models.Model):
    name = models.CharField(max_length=64)

class Monstrositie(models.Model):
    name = models.CharField(max_length=64)

class Ooze(models.Model):
    name = models.CharField(max_length=64)

class Plant(models.Model):
    name = models.CharField(max_length=64)

class SwarmOfLargeBeast(models.Model):
    name = models.CharField(max_length=64)

class SwarmOfLargeUndead(models.Model):
    name = models.CharField(max_length=64)

class SwarmOfMediumBeast(models.Model):
    name = models.CharField(max_length=64)

class SwarmOfMediumConstruct(models.Model):
    name = models.CharField(max_length=64)

class Undead(models.Model):
    name = models.CharField(max_length=64)

class Vehicle(models.Model):
    name = models.CharField(max_length=64)
