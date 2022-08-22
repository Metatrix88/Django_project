from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from card_product.models import Book
from . models import Cart, BookInCart, Order
# Create your views here.

def get_cart(view):
    cart_id = view.request.session.get('cart')
    if not cart_id:
        if view.request.user.is_anonymous:
            customer = None
        else:
            customer = view.request.user
        cart = Cart.objects.create(
            customer = customer
        )
        view.request.session['cart'] = cart.pk
    else:
        cart = Cart.objects.get(pk=cart_id)
    return cart

class DeleteFromCart(generic.DeleteView):
    template_name = 'orders/delete-item.html'
    model = BookInCart
    success_url = reverse_lazy('orders:update-cart')

class UpdateCart(generic.DetailView):
    template_name = 'orders/cart.html'
    model = BookInCart

    def get_object(self, **kwargs):
        cart = get_cart(self)
        for good in self.request.GET.keys():
            if good[:5] == 'good_':
                good_in_cart_pk = good.split('_')[1]
                book_in_cart = BookInCart.objects.get(pk=int(good_in_cart_pk))
                book_in_cart.quantity = int(self.request.GET.get(good))
                book_in_cart.price = book_in_cart.book.price * book_in_cart.quantity
                book_in_cart.save()
        action_type = self.request.GET.get('action_type')
        if action_type == 'Order':
            order = Order.objects.create(
                cart=book_in_cart.cart,
                name_and_surname = self.request.GET.get('name_and_surname'),
                phone = self.request.GET.get('phone'),
                delivery_address = self.request.GET.get('delivery_address'),
                additional_information = self.request.GET.get('additional_information')
            )
            self.request.session.delete('cart')
        return cart

    def render_to_response(self, context, **response_kwargs):
        action_type = self.request.GET.get('action_type')
        if action_type == 'Order':
            return HttpResponseRedirect("/buk/buk/")
        return super().render_to_response(context, **response_kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AddToCart(generic.TemplateView):
    template_name = 'orders/cart.html'
    def get_context_data(self, **kwargs):
        cart_id = self.request.session.get('cart')
        book_id = self.request.GET.get('book_id')

        cart = get_cart(self)

        if book_id:
            # add a book to the cart
            quantity = int(self.request.GET.get('quantity'))
            book = Book.objects.get(pk=book_id)
            price = book.price * quantity
            book_in_cart, created = BookInCart.objects.get_or_create(
                cart=cart,
                book=book,
                defaults={
                    'quantity': quantity,
                    'price': price
                }
            )
            if not created:
                book_in_cart.quantity = book_in_cart.quantity + quantity
                book_in_cart.price = book_in_cart.quantity * book.price
                book_in_cart.save()

        context = super().get_context_data(**kwargs)
        context['cart'] = cart
        return context

class OrderListView(LoginRequiredMixin, generic.ListView):
    template_name = 'orders/order_list.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = Order

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs

class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'orders/order_view.html'
    login_url = reverse_lazy("user_app:login")
    redirect_field_name = 'next'
    model = Order

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy("orders:order-det", kwargs= {'pk': self.object.pk})
