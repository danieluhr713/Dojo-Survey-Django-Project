from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index),
    path('create_user', views.create),
    path('dojo_dash', views.dashboard)
]
