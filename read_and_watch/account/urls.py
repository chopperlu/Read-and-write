from dj_rest_auth.views import LoginView, LogoutView
from django.urls import path

from account import views

urlpatterns = [
    # .../api/v1/accounts/register/ POST
    path('register/', views.UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', views.CustomLogoutView.as_view()),
    path('', views.UserListView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view()),
]