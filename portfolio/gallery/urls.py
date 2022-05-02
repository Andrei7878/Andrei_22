from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_index, name='gallery_index'),
    path('<int:pk>/', views.gallery_detail, name='gallery_detail'),
    path('<category>/', views.gallery_category, name='gallery_category'),
]