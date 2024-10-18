from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('create/', views.note_create, name="create"),
    path('edit-note/', views.note_update),
    path('notes/', views.notes_list, name ="notes"),

]
