from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('register/', views.register, name='register'),
    path('faq/', views.faq, name='faq'),
]
