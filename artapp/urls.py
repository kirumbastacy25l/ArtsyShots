
from django.contrib import admin
from django.urls import path

from artapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about, name='about'),
    path('gallery/',views.gallery, name='gallery' ),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('gallery-single/', views.single, name='gallery-single'),
    path('show/', views.show, name='show'),
    path('hiring/', views.hire, name='hiring'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit, name='edit'),

]
