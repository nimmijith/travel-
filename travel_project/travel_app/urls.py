from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    path('index.html', views.index, name='index'),
    path('home.html', views.home, name='home'),
    path('news.html', views.news, name='news'),
    path('contact.html', views.contact, name='contact'),
]
