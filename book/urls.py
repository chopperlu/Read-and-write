from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book import views
from book.views import UserBookRelationView

router = DefaultRouter()
router.register('', views.BookViewSet)
router.register('book_relation', UserBookRelationView)



urlpatterns = [
    path('', include(router.urls)),

 ]