from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('info', views.info, name='info'),
    path('Create', views.create, name='Create')
]
