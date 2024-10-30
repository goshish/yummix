from django.urls import path
from . import views
from .views import AdminMainPageView


urlpatterns = [
    path('admin-main/', AdminMainPageView.as_view(), name='admin-main'),
]