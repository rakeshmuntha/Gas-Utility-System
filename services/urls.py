from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),         
    path('customer/', views.customer, name='customer'),  
    path('admin-login/', views.admin_login, name='admin_login'),
    path('login/', views.user_login, name='login'), 
    path('register/', views.register, name='register'),
    path('request-options/', views.request_options, name='request_options'),
    path('submit-request/', views.submit_request, name='submit_request'),
    path('track-request/', views.track_request, name='track_request'),
    path('submut/', views.submut, name='submut')

]
