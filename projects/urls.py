from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path(r'^(\d+)/', views.item, name='item'),

] 

urlpatterns += staticfiles_urlpatterns()
