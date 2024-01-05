from django.contrib import admin
from .models import Student,Note,Utilisateur 

# Register your models here.

admin.site.register(Student)
admin.site.register(Note)
admin.site.register(Utilisateur)