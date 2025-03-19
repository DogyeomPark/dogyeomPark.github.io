from django.urls import path
from . import views

urlpatterns = [
    path('/main', views.main_view, name='main'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]