from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('create', views.create, name='create'),
    path('submit_blog', views.submit_blog, name='submit_blog'),
]
