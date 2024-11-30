from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
]
