from django.urls import path
from . import views


app_name = 'hours'

urlpatterns = [
    path('', views.functional_page, name='functional_page'),
]
