from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_wish/', views.add_wish, name='add_wish' ),
    path('<int:wish_id>/delete/', views.delete, name='delete'),
]