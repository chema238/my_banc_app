

from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.main, name='main'),
    path('remesas/', views.remesas, name='remesas'),
    path('remesas/details/<int:id>', views.details, name='details'),
    path('testing/',views.testing, name='testing'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    ]