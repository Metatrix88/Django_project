from django.urls import reverse_lazy
from django.views import generic
from datetime import datetime
from card_product import models

class HomePage(generic.TemplateView):
    template_name = 'main_page/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        context['book_list'] = models.Book.objects.all()[:5]
        return context