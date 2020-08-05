from django.urls import path
from . import views # . because file in same folder

urlpatterns = [
    path('', views.index, name='index'),
]