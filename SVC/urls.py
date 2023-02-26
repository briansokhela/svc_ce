from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('', views.Dashboard.as_view(), name='home'),
]
