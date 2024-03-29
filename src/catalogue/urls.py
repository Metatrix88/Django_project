from django.urls import path
from . import views
app_name = 'cat'

urlpatterns = [
    path('genre_list/', views.GenreListView.as_view(), name="genre-list"),
    path('genre/<int:pk>/', views.GenreDetailView.as_view(), name="genre-det"),
    path('genre_add/', views.GenreAddView.as_view(), name="genre-add"),
    path('genre_delete/<int:pk>/', views.GenreDeleteView.as_view(), name="genre-del"),
    path('genre_edit/<int:pk>/', views.GenreUpdateView.as_view(), name="genre-edit"),

    path('series_list/', views.SeriesListView.as_view(), name="series-list"),
    path('series/<int:pk>/', views.SeriesDetailView.as_view(), name="series-det"),
    path('series_add/', views.SeriesAddView.as_view(), name="series-add"),
    path('series_delete/<int:pk>/', views.SeriesDeleteView.as_view(), name="series-del"),
    path('series_edit/<int:pk>/', views.SeriesUpdateView.as_view(), name="series-edit"),

    path('author_list/', views.TheAuthorListView.as_view(), name="author-list"),
    path('author/<int:pk>/', views.TheAuthorDetailView.as_view(), name="author-det"),
    path('author_add/', views.TheAuthorAddView.as_view(), name="author-add"),
    path('author_delete/<int:pk>/', views.TheAuthorDeleteView.as_view(), name="author-del"),
    path('author_edit/<int:pk>/', views.TheAuthorUpdateView.as_view(), name="author-edit"),

    path('publishinghouse_list/', views.PublishingHouseListView.as_view(), name="publishinghouse-list"),
    path('publishinghouse/<int:pk>/', views.PublishingHouseDetailView.as_view(), name="publishinghouse-det"),
    path('publishinghouse_add/', views.PublishingHouseAddView.as_view(), name="publishinghouse-add"),
    path('publishinghouse_delete/<int:pk>/', views.PublishingHouseDeleteView.as_view(), name="publishinghouse-del"),
    path('publishinghouse_edit/<int:pk>/', views.PublishingHouseUpdateView.as_view(), name="publishinghouse-edit"),

    path('status_list/', views.StatusListView.as_view(), name="status-list"),
    path('status/<int:pk>/', views.StatusDetailView.as_view(), name="status-det"),
    path('status_add/', views.StatusAddView.as_view(), name="status-add"),
    path('status_delete/<int:pk>/', views.StatusDeleteView.as_view(), name="status-del"),
    path('status_edit/<int:pk>/', views.StatusUpdateView.as_view(), name="status-edit"),
]
