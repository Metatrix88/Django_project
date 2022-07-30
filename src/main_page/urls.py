from django.urls import path
from . import views
app_name = 'buk'

urlpatterns = [
    path('buk/', views.HomePage.as_view(), name="buk-home"),

]
