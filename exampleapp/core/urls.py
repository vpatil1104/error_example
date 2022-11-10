from django.urls import path, include
from . import views

urlpatterns = [
    path('admin-form', views.admin_vali,name='admin_vali'),
]
