from django.urls import path

from book import views

urlpatterns = [
    path('', views.BookListCreateView.as_view()),
    # path('<int:pk>/', views.BookDetailView.as_view()),
]