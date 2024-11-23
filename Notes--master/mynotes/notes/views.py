from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .forms import NoteForm
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notes
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

# Create your views here.

class NoteList(LoginRequiredMixin,ListView):
    model = Notes
    template_name = 'notes/note_list.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        context = Notes.objects.filter(user=self.request.user)
        return context
    
class NoteDetail(LoginRequiredMixin,DetailView):
    model = Notes

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to access this note.")
        return obj


class NoteCreate(LoginRequiredMixin,CreateView):
    model = Notes
    form_class = NoteForm
    template_name = 'notes/notes_create.html'
    success_url = reverse_lazy('notes:note-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Note successfully created!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error creating the note ! Please correct the errors below.")
        return super().form_invalid(form)

class NoteUpdate(LoginRequiredMixin,UpdateView):
    model = Notes
    form_class = NoteForm
    success_url = reverse_lazy('notes:note-list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to update this note.")
        return obj


class NoteDelete(LoginRequiredMixin,DeleteView):
    model = Notes
    success_url = reverse_lazy('notes:note-list')
    context_object_name = 'notes'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this note.")
        return obj
