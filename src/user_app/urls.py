from django.urls import path
from . import views
app_name = 'user_app'

urlpatterns = [
    path('login', views.LogView.as_view(), name="login"),
]
