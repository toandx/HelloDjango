from django.db import models

class KeyWord(models.Model):
    name = models.CharField(max_length=50)
    des = models.CharField(max_length=200)
    
class Data(models.Model):
    name = models.CharField(max_length=50)
    des = models.CharField(max_length=200)

class User(models.Model):
    name = models.CharField(max_length=50)
    division = models.CharField(max_length=100)
    usr_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
