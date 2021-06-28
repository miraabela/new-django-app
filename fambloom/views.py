from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Person

class IndexView(generic.ListView):
    template_name = 'fambloom/index.html'
    context_object_name = 'person_list'
    def get_queryset(self):
        """Return the all persons."""
        return Person.objects.all()


class CreateView(generic.edit.CreateView):
    template_name = 'fambloom/create.html'
    model = Person
    fields = ['firstName', 'lastName', 'gender']
    success_url = reverse_lazy('fambloom:index')

class UpdateView(generic.edit.UpdateView):
    template_name = 'fambloom/update.html'
    model = Person
    fields = ['firstName', 'lastName', 'gender']
    success_url = reverse_lazy('fambloom:index')
  
class DeleteView(generic.edit.DeleteView):
    template_name = 'fambloom/delete.html' # override default 
    model = Person
    success_url = reverse_lazy('fambloom:index')