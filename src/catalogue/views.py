from django.urls import reverse_lazy
from django.views import generic
from datetime import datetime
from . import models
from . import forms

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

    def get_success_url(self):
        return reverse_lazy("cat:genre-det", kwargs= {'pk': self.object.pk})

class GenreAddView(generic.CreateView):
    template_name = 'catalogue/genre_add.html'
    model = models.Genre
    form_class = forms.AddGenreForm

    def get_success_url(self):
        return reverse_lazy("cat:genre-list")

class GenreDeleteView(generic.DeleteView):
    template_name = 'catalogue/genre_delete.html'
    model = models.Genre

    def get_success_url(self):
        return reverse_lazy("cat:genre-list")

class GenreUpdateView(generic.UpdateView):
    template_name = 'catalogue/genre_update.html'
    model = models.Genre
    form_class = forms.AddGenreForm
    success_url = reverse_lazy("cat:genre-list")


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

class SeriesDetailView(generic.DetailView):
    template_name = 'catalogue/series_view.html'
    model = models.Series

    def get_success_url(self):
        return reverse_lazy("cat:series-det", kwargs= {'pk': self.object.pk})

class SeriesAddView(generic.CreateView):
    template_name = 'catalogue/series_add.html'
    model = models.Series
    form_class = forms.AddSeriesForm

    def get_success_url(self):
        return reverse_lazy("cat:series-list")

class SeriesDeleteView(generic.DeleteView):
    template_name = 'catalogue/series_delete.html'
    model = models.Series

    def get_success_url(self):
        return reverse_lazy("cat:series-list")

class SeriesUpdateView(generic.UpdateView):
    template_name = 'catalogue/series_update.html'
    model = models.Series
    form_class = forms.AddSeriesForm
    success_url = reverse_lazy("cat:series-list")


class TheAuthorListView(generic.ListView):
    template_name = 'catalogue/author_list.html'
    model = models.TheAuthor

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs

class TheAuthorDetailView(generic.DetailView):
    template_name = 'catalogue/author_view.html'
    model = models.TheAuthor

    def get_success_url(self):
        return reverse_lazy("cat:author-det", kwargs= {'pk': self.object.pk})

class TheAuthorAddView(generic.CreateView):
    template_name = 'catalogue/author_add.html'
    model = models.TheAuthor
    form_class = forms.AddTheAuthorForm

    def get_success_url(self):
        return reverse_lazy("cat:author-list")

class TheAuthorDeleteView(generic.DeleteView):
    template_name = 'catalogue/author_delete.html'
    model = models.TheAuthor

    def get_success_url(self):
        return reverse_lazy("cat:author-list")

class TheAuthorUpdateView(generic.UpdateView):
    template_name = 'catalogue/author_update.html'
    model = models.TheAuthor
    form_class = forms.AddTheAuthorForm
    success_url = reverse_lazy("cat:author-list")

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

class PublishingHouseDetailView(generic.DetailView):
    template_name = 'catalogue/publishinghouse_view.html'
    model = models.PublishingHouse

    def get_success_url(self):
        return reverse_lazy("cat:publishinghouse-det", kwargs= {'pk': self.object.pk})

class PublishingHouseAddView(generic.CreateView):
    template_name = 'catalogue/publishinghouse_add.html'
    model = models.PublishingHouse
    form_class = forms.AddPublishingHouseForm

    def get_success_url(self):
        return reverse_lazy("cat:publishinghouse-list")

class PublishingHouseDeleteView(generic.DeleteView):
    template_name = 'catalogue/publishinghouse_delete.html'
    model = models.PublishingHouse

    def get_success_url(self):
        return reverse_lazy("cat:publishinghouse-list")

class PublishingHouseUpdateView(generic.UpdateView):
    template_name = 'catalogue/publishinghouse_update.html'
    model = models.PublishingHouse
    form_class = forms.AddPublishingHouseForm
    success_url = reverse_lazy("cat:publishinghouse-list")
