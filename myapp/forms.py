from django import forms
from .models import Student,Note


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['student_number', 'Prenom', 'Nom', 'email', 'Moyenne']
    labels = {
      'student_number': "Numéro d'étudiant",
      'Prenom': 'PRENOM',
      'Nom': 'NOM',
      'email': 'Email',
      'Moyenne': 'MOYENNE'
    }
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
      'Prenom': forms.TextInput(attrs={'class': 'form-control'}),
      'Nom': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'Moyenne': forms.NumberInput(attrs={'class': 'form-control'}),
    }
    
    
class NoteForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ['student_number', 'ADD', 'TS', 'Python', 'Teledetecion']
    labels = {
      'student_number': "Numéro d'étudiant",
      'ADD': 'add',
      'TS': 'ts',
      'Python': 'python',
      'Teledetecion': 'teledetection'
    }
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
      'ADD': forms.TextInput(attrs={'class': 'form-control'}),
      'TS': forms.TextInput(attrs={'class': 'form-control'}),
      'Python': forms.TextInput(attrs={'class': 'form-control'}),
      'Teledetecion': forms.NumberInput(attrs={'class': 'form-control'}),
    }
    
    
