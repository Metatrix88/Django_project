from django.shortcuts import render
from django.views import generic
from datetime import datetime
from catalogue import models
from catalogue import forms

# Create your views here.

class GenreListView(generic.ListView):
    template_name = 'сatalogue/genre_list.html'
    model = models.Genre

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs

class GenreDetailView(generic.DetailView):
    template_name = 'сatalogue/genre_view.html'
    model = models.Genre

class GenreAddView(generic.CreateView):
    template_name = 'сatalogue/genre_add.html'
    model = models.Genre
    form_class = forms.AddGenreForm

class GenreDeleteView(generic.DeleteView):
    template_name = 'сatalogue/genre_delete.html'
    model = models.Genre
    success_url = '/genre_list/'

class GenreUpdateView(generic.UpdateView):
    template_name = 'сatalogue/genre_update.html'
    model = models.Genre
    form_class = forms.AddGenreForm
    success_url = '/genre_list/'
