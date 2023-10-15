

# appname/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_contact/', views.create_contact, name='create_contact'),
    path('update_contact/', views.update_contact, name='update_contact'),
    path('delete_contact/', views.delete_contact, name='delete_contact'),
    path('read_contact/', views.read_contact, name='read_contact'),
    path('display_info/', views.display_info, name='display_info'),
    path('failure/', views.failure, name='failure'),
    path('menu/', views.menu, name='menu'),
]


 