from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('Nome', max_length=50)
    login = models.CharField('Login', max_length=15, unique=True)
    password = models.CharField('Senha', max_length=15)
    ema*il = models.CharField('email', max_length=35)
    sex = models.CharField('Sexo', max_length=1, choices=(('M','Masculino'),('F','Feminino')), default='Masculino')

class Formulario(models.Model):
    pass