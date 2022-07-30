from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
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
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs


class GenreDetailView(generic.DetailView):
    template_name = 'catalogue/genre_view.html'
    model = models.Genre

    def get_success_url(self):
        return reverse_lazy("cat:genre-det", kwargs= {'pk': self.object.pk})

class GenreAddView(LoginRequiredMixin, generic.CreateView):
    template_name = 'catalogue/genre_add.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.Genre
    form_class = forms.AddGenreForm

    def get_success_url(self):
        return reverse_lazy("cat:genre-list")

class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'catalogue/genre_delete.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.Genre

    def get_success_url(self):
        return reverse_lazy("cat:genre-list")

class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'catalogue/genre_update.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.Genre
    form_class = forms.AddGenreForm
    success_url = reverse_lazy("cat:genre-list")


class SeriesListView(generic.ListView):
    template_name = 'catalogue/series_list.html'
    model = models.Series

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs

class SeriesDetailView(generic.DetailView):
    template_name = 'catalogue/series_view.html'
    model = models.Series

    def get_success_url(self):
        return reverse_lazy("cat:series-det", kwargs= {'pk': self.object.pk})

class SeriesAddView(LoginRequiredMixin, generic.CreateView):
    template_name = 'catalogue/series_add.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.Series
    form_class = forms.AddSeriesForm

    def get_success_url(self):
        return reverse_lazy("cat:series-list")

class SeriesDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'catalogue/series_delete.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.Series

    def get_success_url(self):
        return reverse_lazy("cat:series-list")

class SeriesUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'catalogue/series_update.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.Series
    form_class = forms.AddSeriesForm
    success_url = reverse_lazy("cat:series-list")


class TheAuthorListView(generic.ListView):
    template_name = 'catalogue/author_list.html'
    model = models.TheAuthor

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs

class TheAuthorDetailView(generic.DetailView):
    template_name = 'catalogue/author_view.html'
    model = models.TheAuthor

    def get_success_url(self):
        return reverse_lazy("cat:author-det", kwargs= {'pk': self.object.pk})

class TheAuthorAddView(LoginRequiredMixin, generic.CreateView):
    template_name = 'catalogue/author_add.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.TheAuthor
    form_class = forms.AddTheAuthorForm

    def get_success_url(self):
        return reverse_lazy("cat:author-list")

class TheAuthorDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'catalogue/author_delete.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.TheAuthor

    def get_success_url(self):
        return reverse_lazy("cat:author-list")

class TheAuthorUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'catalogue/author_update.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.TheAuthor
    form_class = forms.AddTheAuthorForm
    success_url = reverse_lazy("cat:author-list")

class PublishingHouseListView(generic.ListView):
    template_name = 'catalogue/publishinghouse_list.html'
    model = models.PublishingHouse

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs

class PublishingHouseDetailView(generic.DetailView):
    template_name = 'catalogue/publishinghouse_view.html'
    model = models.PublishingHouse

    def get_success_url(self):
        return reverse_lazy("cat:publishinghouse-det", kwargs= {'pk': self.object.pk})

class PublishingHouseAddView(LoginRequiredMixin, generic.CreateView):
    template_name = 'catalogue/publishinghouse_add.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.PublishingHouse
    form_class = forms.AddPublishingHouseForm

    def get_success_url(self):
        return reverse_lazy("cat:publishinghouse-list")

class PublishingHouseDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'catalogue/publishinghouse_delete.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.PublishingHouse

    def get_success_url(self):
        return reverse_lazy("cat:publishinghouse-list")

class PublishingHouseUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'catalogue/publishinghouse_update.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.PublishingHouse
    form_class = forms.AddPublishingHouseForm
    success_url = reverse_lazy("cat:publishinghouse-list")
