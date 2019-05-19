from django.urls import path
from . import views



urlpatterns = [
    path('', views.ProvidersView, name='ProvidersView'),
    #path('providers/', views.providers),
]
