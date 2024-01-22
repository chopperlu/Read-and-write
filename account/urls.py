from dj_rest_auth.views import LoginView, LogoutView
from django.urls import path

from account import views
from account.views import UserMylibrariesView

urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', views.CustomLogoutView.as_view()),
    path('', views.UserListView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view()),
    path('mylibraries/', UserMylibrariesView.as_view()),
]