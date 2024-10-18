from django.shortcuts import render,redirect,get_object_or_404
from .models import Note
from .forms import NoteForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

#note creation view
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})

#note update view
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)  
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_form.html', {'form': form})

#note lists
def notes_list(request):
    return render(request, 'notes_list.html')