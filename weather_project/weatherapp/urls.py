from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Default route for the app
]
