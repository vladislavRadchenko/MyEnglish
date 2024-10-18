from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import views as auth_views

from users import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('vocabulary/', views.vocabulary_view, name='vocabulary'),
    path('vocabulary/edit/<int:phrase_id>/', views.vocabulary_view, name='vocabulary_edit'),
    path('login/', views.custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', lambda request: redirect('login')),
]
