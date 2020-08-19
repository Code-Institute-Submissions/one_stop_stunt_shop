from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_stuntkit, name='view_stuntkit'),
    path('stuntkit', views.view_stuntkit_detail, name='view_stuntkit_detail')
]