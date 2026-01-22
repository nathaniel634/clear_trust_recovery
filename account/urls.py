from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('reports/<int:pk>/', views.report_detail, name='report_detail'),
    path('report/<int:pk>/reviewed/', views.mark_as_reviewed, name='mark_as_reviewed'),
]