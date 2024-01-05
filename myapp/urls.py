from django.urls import path
from . import views

urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('<int:id>', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
    path('Index/', views.Index, name='Index'),
    path('base/' , views.base, name='base'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('edit_note/<int:id>/', views.edit_note, name='edit_note'),

    path('delete/<int:id>/', views.delete, name='delete'),
    path('delete_note/<int:id>/', views.delete_note, name='delete_note'),

    path('logout/', views.myapp_logout, name='myapp_logout'),
    path('Notes/', views.Notes, name='Notes'),
    path('add_notes/', views.add_notes, name='add_notes'),





    



]