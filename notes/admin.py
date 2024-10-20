from django.contrib import admin
from .models import Note

# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']
    list_filter = ['created_at', 'title']
    search_fields = ['title']