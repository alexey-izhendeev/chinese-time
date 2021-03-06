from django.urls import path
from . import views


app_name = 'hours'

urlpatterns = [
    path('', views.coordinates, name='coordinates'),
    path('result_page/', views.result_page, name='result'),


]
