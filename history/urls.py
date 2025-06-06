from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.add_event, name='add_event'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]
