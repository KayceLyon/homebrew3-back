from django.db import models

# Create your models here.

class Cantrip(models.Model):
    name = models.CharField(max_length=64)

class LevelOneSpell(models.Model):
    name = models.CharField(max_length=64)

class LevelTwoSpell(models.Model):
    name = models.CharField(max_length=64)

class LevelThreeSpell(models.Model):
    name = models.CharField(max_length=64)

class LevelFourSpell(models.Model):
    name = models.CharField(max_length=64)

class LevelFiveSpell(models.Model):
    name = models.CharField(max_length=64)

class LevelSixSpell(models.Model):
    name = models.CharField(max_length=64)

class LevelSevenSpell(models.Model):
    name = models.CharField(max_length=64)

class LevelEightSpell(models.Model):
    name = models.CharField(max_length=64)

class LevelNineSpell(models.Model):
    name = models.CharField(max_length=64)
