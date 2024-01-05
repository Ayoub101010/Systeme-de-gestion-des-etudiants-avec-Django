from django.db import models

# Create your models here.
class Student(models.Model):
  student_number = models.PositiveIntegerField()
  Prenom = models.CharField(max_length=50)
  Nom = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  Moyenne = models.FloatField()

  def __str__(self):
    return f'Student: {self.Prenom} {self.Nom}'
  
  
  
class Note(models.Model):
  student_number = models.PositiveIntegerField()

  ADD = models.FloatField()
  TS = models.FloatField()
  Python = models.FloatField()
  Teledetecion = models.FloatField()
  
class Utilisateur(models.Model):
  User_number = models.PositiveIntegerField()
  Prenom = models.CharField(max_length=50)
  Nom = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  CIN = models.CharField(max_length=50)
  
  
  
