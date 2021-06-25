from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index),
    path('create_user', views.create),
]