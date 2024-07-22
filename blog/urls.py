from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.post_details, name='post-detail-page'),
]
