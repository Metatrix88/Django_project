"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from catalogue import views as catalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre_list/', catalog.GenreListView.as_view()),
    path('genre/<int:pk>/', catalog.GenreDetailView.as_view()),
    path('genre_add/', catalog.GenreAddView.as_view()),
    path('genre_delete/<int:pk>/', catalog.GenreDeleteView.as_view()),
    path('genre_edit/<int:pk>/', catalog.GenreUpdateView.as_view()),

    path('series_list/', catalog.SeriesListView.as_view()),
    path('series_add/', catalog.SeriesAddView.as_view()),
    path('series/<int:pk>/', catalog.SeriesDetailView.as_view()),
    path('series_edit/<int:pk>/', catalog.SeriesUpdateView.as_view()),
    path('series_delete/<int:pk>/', catalog.SeriesDeleteView.as_view()),

    path('author_list/', catalog.TheAuthorsListView.as_view()),
    path('author_add/', catalog.TheAuthorsAddView.as_view()),
    path('author/<int:pk>/', catalog.TheAuthorsDetailView.as_view()),
    path('author_edit/<int:pk>/', catalog.TheAuthorsUpdateView.as_view()),
    path('author_delete/<int:pk>/', catalog.TheAuthorsDeleteView.as_view()),

    path('publishinghouse_list/', catalog.PublishingHouseListView.as_view()),
    path('publishinghouse_add/', catalog.PublishingHouseAddView.as_view()),
    path('publishinghouse/<int:pk>/', catalog.PublishingHouseDetailView.as_view()),
    path('publishinghouse_edit/<int:pk>/', catalog.PublishingHouseUpdateView.as_view()),
    path('publishinghouse_delete/<int:pk>/', catalog.PublishingHouseDeleteView.as_view()),

]
