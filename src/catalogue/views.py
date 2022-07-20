from django.shortcuts import render
from django.views import generic
from datetime import datetime
from catalogue import models
from catalogue import forms

# Create your views here.

class GenreListView(generic.ListView):
    template_name = 'catalogue/genre_list.html'
    model = models.Genre

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs

class GenreDetailView(generic.DetailView):
    template_name = 'catalogue/genre_view.html'
    model = models.Genre

class GenreAddView(generic.CreateView):
    template_name = 'catalogue/genre_add.html'
    model = models.Genre
    form_class = forms.AddGenreForm
    success_url = '/genre_list/'

class GenreDeleteView(generic.DeleteView):
    template_name = 'catalogue/genre_delete.html'
    model = models.Genre
    success_url = '/genre_list/'

class GenreUpdateView(generic.UpdateView):
    template_name = 'catalogue/genre_update.html'
    model = models.Genre
    form_class = forms.AddGenreForm
    success_url = '/genre_list/'


class SeriesListView(generic.ListView):
    template_name = 'catalogue/series_list.html'
    model = models.Series

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs

class SeriesAddView(generic.CreateView):
    template_name = 'catalogue/series_add.html'
    model = models.Series
    form_class = forms.AddSeriesForm
    success_url = '/series_list/'

class SeriesDetailView(generic.DetailView):
    template_name = 'catalogue/series_view.html'
    model = models.Series

class SeriesUpdateView(generic.UpdateView):
    template_name = 'catalogue/series_update.html'
    model = models.Series
    form_class = forms.AddSeriesForm
    success_url = '/series_list/'

class SeriesDeleteView(generic.DeleteView):
    template_name = 'catalogue/series_delete.html'
    model = models.Series
    success_url = '/series_list/'

    class SeriesListView(generic.ListView):
        template_name = 'catalogue/series_list.html'
    model = models.Series

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs


class TheAuthorsListView(generic.ListView):
    template_name = 'catalogue/author_list.html'
    model = models.TheAuthors

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs
class TheAuthorsAddView(generic.CreateView):
    template_name = 'catalogue/author_add.html'
    model = models.TheAuthors
    form_class = forms.AddTheAuthorsForm
    success_url = '/author_list/'

class TheAuthorsDetailView(generic.DetailView):
    template_name = 'catalogue/author_view.html'
    model = models.TheAuthors

class TheAuthorsUpdateView(generic.UpdateView):
    template_name = 'catalogue/author_update.html'
    model = models.TheAuthors
    form_class = forms.AddTheAuthorsForm
    success_url = '/author_list/'
class TheAuthorsDeleteView(generic.DeleteView):
    template_name = 'catalogue/author_delete.html'
    model = models.TheAuthors
    success_url = '/author_list/'

class PublishingHouseListView(generic.ListView):
    template_name = 'catalogue/publishinghouse_list.html'
    model = models.PublishingHouse

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs

class PublishingHouseAddView(generic.CreateView):
    template_name = 'catalogue/publishinghouse_add.html'
    model = models.PublishingHouse
    form_class = forms.AddPublishingHouseForm
    success_url = '/publishinghouse_list/'

class PublishingHouseDetailView(generic.DetailView):
    template_name = 'catalogue/publishinghouse_view.html'
    model = models.PublishingHouse

class PublishingHouseUpdateView(generic.UpdateView):
    template_name = 'catalogue/publishinghouse_update.html'
    model = models.PublishingHouse
    form_class = forms.AddPublishingHouseForm
    success_url = '/publishinghouse_list/'

class PublishingHouseDeleteView(generic.DeleteView):
    template_name = 'catalogue/publishinghouse_delete.html'
    model = models.PublishingHouse
    success_url = '/publishinghouse_list/'
