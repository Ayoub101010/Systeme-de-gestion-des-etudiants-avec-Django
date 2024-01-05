from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib import messages 
from .models import Student, Note,Utilisateur
from .forms import StudentForm, NoteForm,UtilisateurForm




def myapp(request):
  
  if request.method == 'POST': 
    username = request.POST['username']
    pswrd = request.POST['pswrd']
    
    user = authenticate(username=username, password=pswrd)
    
    if user is not None: 
      login(request, user)
      return render(request,"Index.html",{
    'students': Student.objects.all()
  })

    
    else : 
      messages.error(request, "bad credentials")
      return redirect('home')
  return render(request, 'Login.html')

def base(request): 
  return render(request,'base.html')

def Index(request):
  return render(request, 'Index.html', {
    'students': Student.objects.all()
  })

def view_student(request, id):
  return HttpResponseRedirect(reverse('Index'))

def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_Prenom = form.cleaned_data['Prenom']
      new_Nom = form.cleaned_data['Nom']
      new_email = form.cleaned_data['email']
      new_moyenne = form.cleaned_data['Moyenne']

      new_student = Student(
        student_number=new_student_number,
        Prenom=new_Prenom,
        Nom=new_Nom,
        email=new_email,
        Moyenne=new_moyenne
      )
      new_student.save()
      return render(request, 'add.html', {
        'form': StudentForm(),
        'success': True
      })
    return redirect('myapp') 
  else:
    form = StudentForm()
  return render(request, 'add.html', {
    'form': StudentForm()
  })
  
def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'edit.html', {
    'form': form
  })
  
def edit_note(request, id):
  if request.method == 'POST':
    note = Note.objects.get(pk=id)
    form = NoteForm(request.POST, instance=note)
    if form.is_valid():
      form.save()
      return render(request, 'edit_note.html', {
        'form': form,
        'success': True
      })
  else:
    note = Note.objects.get(pk=id)
    form = NoteForm(instance=note)
  return render(request, 'edit_note.html', {
    'form': form
  })
  
def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('Index'))


def delete_note(request, id):
  if request.method == 'POST':
    note = Note.objects.get(pk=id)
    note.delete()
  return HttpResponseRedirect(reverse('Notes'))

def myapp_logout(request):
    # Logique de déconnexion
    logout(request)

    # Rediriger vers l'URL spécifiée après la déconnexion (par exemple, la page d'accueil)
    return redirect(reverse('myapp'))
  
def Notes(request):
  return render(request, 'notes.html', {
    'Notes': Note.objects.all()
  })
  

def add_notes(request):
  if request.method == 'POST':
    form = NoteForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_ADD = form.cleaned_data['ADD']
      new_TS = form.cleaned_data['TS']
      new_Python = form.cleaned_data['Python']
      new_Teledetecion = form.cleaned_data['Teledetecion']

      new_note = Note(
        student_number=new_student_number,
        ADD=new_ADD,
        TS=new_TS,
        Python=new_Python,
        Teledetecion=new_Teledetecion
      )
      new_note.save()
      return render(request, 'add_notes.html', {
        'form': NoteForm(),
        'success': True
      })
    return redirect('myapp') 
  else:
    form = NoteForm()
  return render(request, 'add_notes.html', {
    'form': NoteForm()
  }) 

  
def addUser(request):
  if request.method == 'POST':
    form = UtilisateurForm(request.POST)
    if form.is_valid():
      new_User_number = form.cleaned_data['User_number']
      new_Prenom = form.cleaned_data['Prenom']
      new_Nom = form.cleaned_data['Nom']
      new_email = form.cleaned_data['email']
      new_cin = form.cleaned_data['CIN']

      new_utilisateur = Utilisateur(
        User_number=new_User_number,
        Prenom=new_Prenom,
        Nom=new_Nom,
        email=new_email,
        CIN=new_cin
      )
      new_utilisateur.save()
      return render(request, 'addUser.html', {
        'form': UtilisateurForm(),
        'success': True
      })
    return redirect('myapp') 
  else:
    form = UtilisateurForm()
  return render(request, 'add_User.html', {
    'form': UtilisateurForm()
  })

