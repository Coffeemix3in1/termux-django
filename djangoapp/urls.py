from django.urls import path #importing the necessary documents

from . import views

app_name ='djangoapp'

urlpatterns = [
path('', views.index, name='index'),
]


