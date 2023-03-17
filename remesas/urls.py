from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('',views.main, name='main'),
    path('remesas/', views.remesas, name='remesas'),
    path('remesas/details/<int:id>', views.details, name='details'),
    path('testing/',views.testing, name='testing'),
    path('login/', CustomLoginView.as_view(), name='login'),
]