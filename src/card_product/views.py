from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from catalogue.models import TheAuthor
from . import models
from . import forms
# Create your views here.

class BookListView(generic.ListView):
    template_name = 'card_product/book_list.html'
    model = models.Book

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs


class BookDetailView(generic.DetailView):
    template_name = 'card_product/book_view.html'
    model = models.Book

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    # def get_context_data(self, *args, **kwards):

    #     def author_and_genre(value):
    #         text=''
    #         if len(value) == 1:
    #             text = value[0].name
    #         else:
    #             for author in value:
    #                 text += str(author.name) + '; '
    #         return text

    #     context = super().get_context_data(*args, **kwards)

    #     book = models.Book.objects.get(pk = self.object.pk)
    #     context['author'] = author_and_genre(book.author.all())
    #     context['genre'] = author_and_genre(book.genre.all())

    #     return context

    def get_success_url(self):
        return reverse_lazy("card:book-det", kwargs= {'pk': self.object.pk})

class BookAddView(LoginRequiredMixin, generic.CreateView):
    template_name = 'card_product/book_add.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.Book
    form_class = forms.AddBookForm

    def get_success_url(self):
        return reverse_lazy("card:book-list")

class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'card_product/book_delete.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.Book

    def get_success_url(self):
        return reverse_lazy("card:book-list")

class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'card_product/book_update.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = models.Book
    form_class = forms.AddBookForm
    success_url = reverse_lazy("card:book-list")
