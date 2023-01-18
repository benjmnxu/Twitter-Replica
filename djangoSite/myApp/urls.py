
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('viewer/', views.viewer, name='viewer'),
    path('yourprofile/', views.yourprofile, name='yourprofile'),
    path('/profiles', views.profiles, name='profiles'),
    path('', views.home, name='home'),

]