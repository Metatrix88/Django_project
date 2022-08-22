from django.urls import path
from . import views
app_name = 'orders'

urlpatterns = [
    path('add-to-cart', views.AddToCart.as_view(), name="add-to-cart"),
    path('delete-from-cart/<int:pk>/', views.DeleteFromCart.as_view(), name="delete-from-cart"),
    path('update-cart/', views.UpdateCart.as_view(), name="update-cart"),
    path('order-list/', views.OrderListView.as_view(), name="order-list"),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name="order-det")
]
