from django.contrib.auth import views as auth_views
from django.urls import path 

from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='msuTracking/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/<int:id>', views.delete_data, name='delete'),
    path('custom', views.custom, name="custom")
]