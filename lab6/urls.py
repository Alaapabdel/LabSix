from django.urls import path
from . import views

app_name = "lab6"
urlpatterns = [
    path('', views.index, name='index'),
    path('feedback', views.feedback, name='feedback'),
    path('search', views.search, name='search'),
]
