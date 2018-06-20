from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('logo/', views.logopage, name='logo')
]
