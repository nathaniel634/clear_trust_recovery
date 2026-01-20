from django.urls import path

from . import views

app_name = 'frontend'
urlpatterns = [
    path('', views.home_view, name="home"),
    path('about-us/', views.about_view, name="about"),
    path('services/', views.services_view, name="services"),
    path('contact-us/', views.contact_view, name="contact"),
    path('file-complaint/', views.file_complaint_view, name="file_complaint"),
]