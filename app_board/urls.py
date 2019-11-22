from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:project_id>', views.detail, name="detail"),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('edit/<int:project_id>', views.edit, name="edit"),
    path('update/<int:project_id>', views.update, name="update"),
    path('delete/<int:project_id>', views.delete, name="delete"),
]